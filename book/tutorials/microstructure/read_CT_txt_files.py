# function to read all microCT data in
#    by Mike Durand June 2021

from numpy import empty,argsort
import os

def read_CT_txt_files(DataDir):
        
    filenames = (f for f in os.scandir(DataDir) if not f.name.startswith('.'))
    n=len(list(filenames)) #to preallocate S    
    
    SSA=empty([n])
    height_min=empty([n])
    height_max=empty([n])
    
    filenames = (f for f in os.scandir(DataDir) if not f.name.startswith('.'))
    
    count=0
    
    for entry in filenames:

        fname=DataDir + entry.name                
        
        #parse depth range
        split_name=fname.split('_')
        height_range=split_name[1]
        height_min_max=height_range[0:-2].split('-')            
        height_max[count]=float(height_min_max[0])
        height_min[count]=float(height_min_max[1])                   
                        
        with open(fname,"r",encoding='iso-8859-1') as datafile:            
            for line in datafile:                
                if 'Object surface / volume ratio' in line:                
                    split_line=line.split(',')                                        
                    SSA[count]=float(split_line[2])
                    count+=1                    

    #convert from 1/mm to m^2/kg 
    SSA*=1000./917. 
    
    # sort data
    isort=argsort(height_min)
    height_min=height_min[isort]
    height_max=height_max[isort]
    SSA=SSA[isort]
 
    return SSA,height_min,height_max