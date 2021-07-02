# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
 Open ASTER L1T HDF-EOS and Export as GeotIFF Tool
 How To Tutorial
 This tool imports ASTER L1T HDF-EOS files, georeferences, and  exports as 
 GeoTIFF files.
-------------------------------------------------------------------------------
 Author: Cole Krehbiel
 Contact: LPDAAC@usgs.gov  
 Organization: Land Processes Distributed Active Archive Center
 Date last modified: 03-06-2017
-------------------------------------------------------------------------------
 DESCRIPTION:
 This script takes an ASTER L1T HDF-EOS file (.hdf) as an input and outputs 
 georeferenced tagged image file format (GeoTIFF) files for each of the VNIR,
 SWIR, and TIR science datasets contained in the original ASTER L1T file.

 Results from this tutorial are output in Universal Transverse Mercator (UTM)
 with WGS84 as GeoTIFF files. The output GeoTIFFs for each band include:
 1. Original_AST_L1T_Filename_ImageDataband#.tif
 Data is At-Sensor radiance stored as Digital Numbers(DN).The script will batch 
 process ASTER L1T files if more than 1 is located in the working directory.
 Output file directory will be 'inputfiledirectory'+'/output/'

 This tool was specifically developed for ASTER L1T HDF-EOS files and should 
 only be used for those data products.
-------------------------------------------------------------------------------
 PREREQUISITES:
 Discaimer: This script was tested in the following environments:
   -  Python: Version 3.4.5 and Version 2.7.12 (Anaconda 4.1.1) on Windows OS
   -  Geospatial Data Abstraction Library (GDAL): Version 2.0.0 and 2.1.0

 Python Packages/Modules:
 osgeo with gdal and osr – 2.0.0, 2.1.0 
 numpy – 1.11.1, 1.12.0
 argparse - 1.1
 os, glob, sys, getopt 
-------------------------------------------------------------------------------
 ADDITIONAL INFORMATION:
 LP DAAC ASTER L1T Product Page: 
 https://lpdaac.usgs.gov/dataset_discovery/aster/aster_products_table/ast_l1t
 LP DAAC ASTER L1T User Guide: 
 https://lpdaac.usgs.gov/sites/default/files/public/product_documentation/
 aster_l1t_users_guide.pdf
 
 Search for other tools at https://lpdaac.usgs.gov/
-------------------------------------------------------------------------------
PROCEDURES:
 1. Copy/clone ASTERL1T_hdf2tif.py from LP DAAC Recipes & Tutorials Repository
 2. Download ASTER L1T data from the LP DAAC to a local directory
 3. Open a Command Prompt window and navigate to the directory where you 
    downloaded the ASTERL1T_hdf2tif.py script
 4. Activate python in the Command Prompt window
     1. > activate [python environment name]
 5. Once activated, run the script with this command in your Command Prompt:
     1. > python ASTERL1T_hdf2tif.py [insert input dir with AST_L1T files here]
             1.	Example of input directory: C:/users/johndoe/ASTERL1T/
-------------------------------------------------------------------------------
"""
# Load necessary packages into Python
from osgeo import gdal, osr
import numpy as np
import os, glob, sys, getopt, argparse
#------------------------------------------------------------------------------
# Define Script and handle errors
def main(argv):
    parser = argparse.ArgumentParser()
    try:
        opts, args = getopt.getopt(argv,"hi:",["input_directory"])   
        if len(sys.argv[1:])==0:
            class MyParser(argparse.ArgumentParser):
                def error(self, message):
                    sys.stderr.write('error: %s\n' % message)
                    self.print_help()
                    sys.exit(2)
            parser=MyParser()
            parser.add_argument('input_directory', nargs='+')
            args=parser.parse_args()
        elif "'" in sys.argv[1] or '"' in sys.argv[1]:
            parser.error('error: Do not include quotes in input directory argument')
        elif len(sys.argv) > 2:
            parser.error('error: Only 1 Argument is allowed (input_directory)')
        elif sys.argv[1][-1] != '/' and sys.argv[1][-1] != '\\':
            parser.error('error: Please end your directory location with / or \\')
    except getopt.GetoptError:
        print('error: Invalid option passed as argument')      
        print('ASTERL1T_DN2REF.py <input_directory>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('ASTERL1T_DN2REF.py <input_directory>')
            sys.exit()
    try:
        os.chdir(sys.argv[1])
    except FileNotFoundError:
        print('error: input_directory provided does not exist or was not found')
        sys.exit(2)
#------------------------------------------------------------------------------
#|                    Batch Process files from directory:                     |
#------------------------------------------------------------------------------

# Set input/current working directory, user NEEDS to change to directory where 
# files will be downloaded to.
    in_dir = sys.argv[1]
    # at the end of final directory location
    os.chdir(in_dir)
    
    # Create and set output directory
    out_dir = os.path.normpath((os.path.split(in_dir)[0] + os.sep + 
    	'output/' ))+ '\\'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
            
    # Create a list of ASTER L1T HDF files in the directory
    file_list = glob.glob('AST_L1T_**.hdf')
    if len(file_list) == 0:
        print('Error: no ASTER L1T hdf files were found in this directory')
        sys.exit(2)
    # Loop through all ASTER L1T hdf files in the directory
    for k in range(len(file_list)):
        
        # Maintains original filename convention    
        file_name = file_list[k]    
        
        print('Processing File: ' + file_name + ' (' + str(k+1) + ' out of ' 
        + str(len(file_list)) + ')')
        # Read in the file and metadata
        aster = gdal.Open(file_name)
        aster_sds = aster.GetSubDatasets()
        meta = aster.GetMetadata()
        
        # Define UL, LR, UTM zone    
        ul = [np.float(x) for x in meta['UPPERLEFTM'].split(', ')]
        lr = [np.float(x) for x in meta['LOWERRIGHTM'].split(', ')]
        utm = np.int(meta['UTMZONENUMBER'])
        n_s = np.float(meta['NORTHBOUNDINGCOORDINATE'])
        
        # Create UTM zone code numbers    
        utm_n = [i+32600 for i in range(60)]
        utm_s = [i+32700 for i in range(60)]
        
        # Define UTM zone based on North or South
        if n_s < 0:
            utm_zone = utm_s[utm]
        else:
            utm_zone = utm_n[utm]
        
        del utm_n, utm_s, utm, meta
        # Loop through all ASTER L1T SDS (bands)    
        for i in range(len(aster_sds)):
    
            # Maintain original dataset name    
            gname = str(aster_sds[i])
            aster_sd = gname.split(',')[0]
            
            # Only process VNIR, SWIR, and TIR datasets        
            if len(aster_sd) > 80:        
                
                # Generate output name for tif            
                aster_sd2 = aster_sd.split('(')[1]
                aster_sd3 = aster_sd2[1:-1]
                band = aster_sd3.split(':')[-1]
                band_3N =  band.split('N')[0]           
                band_num = np.int(band_3N.split('ta')[-1])
                out_filename = out_dir + file_name.split('.hdf')[0] + '_' + \
                band + '.tif'
                
                # Define extent and provide offset for UTM South zones            
                if n_s < 0:
                    ul_y = ul[0] + 10000000
                    ul_x = ul[1]
                
                    lr_y = lr[0] + 10000000
                    lr_x = lr[1]
    
                # Define extent for UTM North zones            
                else:
                    ul_y = ul[0] 
                    ul_x = ul[1]
                
                    lr_y = lr[0] 
                    lr_x = lr[1]  
                    
               # Open SDS and create array            
                band_ds = gdal.Open(aster_sd3, gdal.GA_ReadOnly)
                
                if band_num < 10:
                    sds = band_ds.ReadAsArray().astype(np.byte)
        
                    # Query raster dimensions & calculate raster x/y resolution            
                    ncol, nrow = sds.shape            
                    y_res = -1 * round((max(ul_y, lr_y)-min(ul_y, lr_y))/ncol)
                    x_res = round((max(ul_x, lr_x)-min(ul_x, lr_x))/nrow)
                
                    # Define UL x and y coordinates based on spatial resolution           
                    ul_yy = ul_y - (y_res/2)
                    ul_xx = ul_x - (x_res/2)                
                    # Generate output Geotiff file
                    driver = gdal.GetDriverByName('GTiff')
                    ds = driver.Create(out_filename, nrow, ncol, 1, gdal.GDT_Byte)
              
                else:
                    sds = band_ds.ReadAsArray().astype(np.uint16)
        
                    # Query raster dimensions & calculate raster x/y resolution            
                    ncol, nrow = sds.shape            
                    y_res = -1 * round((max(ul_y, lr_y)-min(ul_y, lr_y))/ncol)
                    x_res = round((max(ul_x, lr_x)-min(ul_x, lr_x))/nrow)
                
                    # Define UL x and y coordinates based on spatial resolution           
                    ul_yy = ul_y - (y_res/2)
                    ul_xx = ul_x - (x_res/2)                    
                    # Generate output Geotiff file
                    driver = gdal.GetDriverByName('GTiff')
                    ds = driver.Create(out_filename, nrow, ncol, 1, 
                                       gdal.GDT_UInt16)            
                # Define output GeoTiff CRS and extent properties
                srs = osr.SpatialReference()
                srs.ImportFromEPSG(utm_zone)
                ds.SetProjection(srs.ExportToWkt())
                ds.SetGeoTransform((ul_xx, x_res, 0., ul_yy, 0., y_res))
                
                # Write SDS array to output GeoTiff
                outband = ds.GetRasterBand(1)
                outband.SetNoDataValue(0)
                outband.WriteArray(sds)
                ds = None
                del aster_sd,aster_sd2,aster_sd3,band, band_3N, band_num, gname
if __name__ == "__main__":
   main(sys.argv[1:])                
###############################################################################