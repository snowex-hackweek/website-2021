def gdal_corners(filename):
    '''
    a function  that can be used to determine the boundary of a raster / tif file.
    '''
    #http://stackoverflow.com/questions/2922532/obtain-latitude-and-longitude-from-a-geotiff-file
    from osgeo import gdal            # https://www.lfd.uci.edu/~gohlke/pythonlibs/
    ds = gdal.Open(filename)
    width = ds.RasterXSize
    height = ds.RasterYSize
    gt = ds.GetGeoTransform()
    minx = gt[0]
    miny = gt[3] + width*gt[4] + height*gt[5]
    maxx = gt[0] + width*gt[1] + height*gt[2]
    maxy = gt[3]
    return (minx,miny,maxx,maxy)
                
def join_files(file_list):
    
    '''
        a method for merging raster/tif data along the band dimension using 
        rioxarray. this method does not save data to storage.
    '''
    
    import rioxarray as rxr
    import xarray as xr
    
    # initialize band names
    var_names = []
    
    # loop over bands, append to a rasterio xarray
    for file in file_list:
        
        xmin,ymin,xmax,ymax=tuple(gdal_corners(file))
        cda=rxr.open_rasterio(file,chunks=(1,1200,1200))
        cda=cda.sel(x=slice(xmin,xmax),y=slice(ymax,ymin))
        
        if file == file_list[0]:
            da = cda
        else:
            da = xr.concat([da, cda], "band")
            
        # extract frequency / polarization band
        var_name = file.split('_')[5]
        var_name = var_name[0:2] + var_name[5:]
        var_names.append(var_name)

    # change band names for reading
    da = da.assign_coords({'band' : var_names})
    return da


def join_sar_radiom(da, radiom):
    ''' 
    
    input
        da - rioxarray containing SWESARR SAR data. 6 channels expected.
        radiom - pandas array containing radiometer data. 3 channels expected.
        
    output
        data_p - pandas data series intended for plotting with hvplot's "groupby" feature. 
                sadly, all measurement data is crammed into a single column, making this 
                difficult to use outside of hvplot functionality.
        out_data - pandas data series that is readable. intended for use in student exercise.
        
    TO-DO / IMPROVEMENTS :
        implementing this with xarray would be much more RAM efficient. 
        however, i find pandas arrays to be easier to conceptualize than xarrays.
        i feel its best to go with pandas arrays for the tutorial.
            ( with great shame, i admit i find it harder to visualize
              N-dimensional data rather than 2-dimensional data )
            
    '''
    from geopy.distance import distance
    import numpy as np
    import pandas as pd
    import datetime
    
    # first, convert the data from the SAR's meter-based, 
    # universal transverse mercator (UTM) coordinate system
    # to the radiometer's old-fashioned 
    # latitude/longitude coordinate system
    sar_geo = da.rio.reproject("EPSG:4326")
    
    # get latidue and longitude from SAR data
    lat_sar = sar_geo.y.data
    lon_sar = sar_geo.x.data

    # radiometer latitude/longitude values as numpy arrays
    lat_rad = radiom['Latitude (deg)'].to_numpy()
    lon_rad = radiom['Longitude (deg)'].to_numpy()

    # loop over latitude and longitude
    frames = []
    k = -1
    for lat, lon in zip(lat_rad, lon_rad):
        k+=1

        # get the difference between latitude and longitude pairs
        # for SAR and radiometer data
        lat_m = np.abs(lat_sar - lat).tolist()
        lon_m = np.abs(lon_sar - lon).tolist()

        # use python's built-in functions to find minimum index
        ind_lat = lat_m.index(min(lat_m))
        ind_lon = lon_m.index(min(lon_m))

        # write sar lat and lon
        s_lat = lat_sar[ind_lat]
        s_lon = lon_sar[ind_lon]

        # get distance between the estimated sar and radiometer center positions
        # using vincenty's formula from the geopy library
        dis = distance( (lat, lon), (s_lat, s_lon) ).m

        # construct data dictionary
        data_d = {'sar_lat': s_lat, 'sar_lon' : s_lon, 
                  'rad_lat' : lat, 'rad_lon' : lon, 
                  'ind_lat' : ind_lat, 'ind_lon' : ind_lon,
                  'dist_m' : dis}

        # make a pandas dataframe based on the above data!
        df = pd.DataFrame(data_d, index = [k])
        
        # throw it in an array for good measure
        frames.append(df)

    # use "list comprehension" syntax to merge the pandas dataframes together
    location_data = pd.concat( data for data in frames )
    del frames, df, data_d
    
    # now lets store our SAR data based on our filtered results
    sar_data = []

    for in1, in2 in zip( location_data['sar_lon'].tolist(), location_data['sar_lat'].tolist()):
        # access the dask array storing our results
        d = sar_geo.sel( x=in1, y=in2 ).compute().data.tolist()
        # append to our list
        sar_data.append(d)

    # convert both arrays array to a numpy array for easy merging
    data = np.array(sar_data)
    radiom_d = radiom.iloc[:,4:7].to_numpy()

    # insert the radiometer data to the SAR data as a column vector
    for i in range(np.size(radiom_d,1)):
        data = np.insert( data, np.size(data,1), radiom_d[:,i], axis=1 )
    del radiom_d

    # the following section is for plotting with hvplot while including a label only.
    #
    # use list operations paired with pandas series to repeat the lat/lon data
    lon_ser = pd.Series( location_data['sar_lon'].to_list() * (6)\
                        + location_data['rad_lon'].to_list() * (3) )
    lat_ser = pd.Series( location_data['sar_lat'].to_list() * (6)\
                        + location_data['rad_lat'].to_list() * (3) )
    
    # flatten MATLAB/*F*ortran style. (Default flattens as row vectors)
    data_ser = data.flatten(order='F')

    # get series length, create IDs for plotting
    # all series have the same length, so this shouldn't matter.
    sl = len(radiom['TB X (K)'])
    id_ser = pd.Series(
        ['09VV SAR']*sl + ['09VH SAR']*sl + ['13VV SAR']*sl + ['13VH SAR']*sl + \
            ['17VV SAR']*sl + ['17VH SAR']*sl + \
        ['X-band Rad']*sl + ['K-band Rad']*sl + ['Ka-band Rad']*sl, name="ID"
         )
    
    # the final frame used only for plotting by groups with hvplot
    frame = {'Longitude (deg)' : lon_ser, 'Latitude (deg)' : lat_ser,
             'Measurements' : data_ser, 'ID' : id_ser}
    data_p = pd.DataFrame(frame)
    
    # convert swesarr numpy data to dataframe
    swesarr_df = pd.DataFrame(data = data, 
                        columns = ["09VV SAR", "09VH SAR", 
                                   "13VV SAR", "13VH SAR",
                                   "17VV SAR", "17VH SAR",
                                   'X-band Rad', 'Ku-band Rad', 
                                   'Ka-band Rad'])
    
    # Convert UTC string to date time array
    times = radiom.UTC.to_frame()
    times = times['UTC'].to_list()

    # convert to datetime
    times = [datetime.datetime.strptime(time_str, '%Y%m%d-%H:%M:%S.%f') for time_str in times]

    radiom.UTC = times

    
    # combine time data with swesarr measurements
    out_data = pd.concat( [radiom.UTC.to_frame(), swesarr_df], axis=1)

    # return the variable used for plotting and its more user-friendly variant.
    return data_p, out_data

if __name__ == '__main__':
    print('name is main!')