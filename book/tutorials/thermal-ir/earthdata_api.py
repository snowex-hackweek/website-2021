import requests
import io
import pandas as pd

def earthdata_granule_search(product, version, bounding_box, timestampsUTC, search_time_window=1, search_time_window_units='h', list_filepath=None, ext=None):
    '''
    Returns a list of data access URLs from the NASA EarthData API for a specific product, version, time window, and location window.
    The URLs can be then used for downloading with wget.
    (Steven Pestana, spestana@uw.edu, 2020)

      Parameters:
              product (str): product id
              version (str): product version
              bounding_box (list of ints): [lower left longitude, lower left latitude, upper right longitude, upper right latitude]
              timestampsUTC (list of pd.Timestamp or datetime): time and date in UTC to search for data product
              search_time_window (int): how far out from each timestampsUTC to search for data products (for pd.timedelta())
              search_time_window_units (str): time units of search_time_window, e.g. 'h' for hours or 'd' for days (for pd.timedelta())
              list_filepath (str): (optional) filepath for a text file to save a list of the access URLs to
              ext (str): (optional) file extension to search for (e.g. "tif" or "hdf")
      
      Returns:
              data_url_list (list): list of 'Online Access URLs' (strings) for each search result
    '''
    
    # set the base URL for searching granules through the EarthData API
    url = "https://cmr.earthdata.nasa.gov/search/granules.csv?"
    
    # compose search strings for data product and version
    shortname_id_str = "short_name={}".format(product)
    version_str = "version={}".format(version)
    
    # compose search string for bounding box
    bounding_box_str = "bounding_box[]={ll_lon},{ll_lat},{ur_lon},{ur_lat}".format(ll_lon=bounding_box[0], 
                                                                                ll_lat=bounding_box[1], 
                                                                                ur_lon=bounding_box[2], 
                                                                                ur_lat=bounding_box[3])
    
    # if timestamp provided is not an iterable (such as if it is a single timestamp or datetime object), try to make it a list
    if type(timestampsUTC) != list:
        timestampsUTC = [timestampsUTC]
        
    # create an empty list to hold download URLs
    data_url_list = []
    
    # for each timestamp, use it as the start date for a search
    for i, start_date in enumerate(timestampsUTC):
        
        # make sure we have a pd.Timestamp, this will convert datetime.datetime to pd.Timestamp
        start_date = pd.Timestamp(start_date)
        
        # make the end date for the seearch, incrementing by search_time_window
        end_date = start_date + pd.to_timedelta(search_time_window, unit=search_time_window_units)
        
        # compose the time range string for the request
        start_date_str = "{}:00:00Z".format(start_date.strftime('%Y-%m-%dT%H'))
        end_date_str = "{}:00:00Z".format(end_date.strftime('%Y-%m-%dT%H'))
        time_range_str = "temporal=" + start_date_str + "," + end_date_str
        
        # build the whole request URL and make the request.get
        response = requests.get(url+"&"+shortname_id_str+"&"+version_str+"&"+bounding_box_str+"&"+time_range_str)
        
        # read the response CSV and put in a temporary dataframe
        df = pd.read_csv(io.StringIO(response.text))

        # add the access url from which we can download the file to our list
        for j, data_url in enumerate(df['Online Access URLs']):
            if pd.isnull(data_url):
                print('Online Access URL not available for {}'.format(df['Producer Granule ID'][j]))
            else:
                data_url_list.append(data_url)
    
    # flatten the resulting list (so that we don't have a list of lists)
    flattened_url_list = [url for sublist in [urls.split(',') for urls in data_url_list] for url in sublist]
    
    # if we have a file extension specified
    if ext != None:
        print('Only including {} files in list'.format(ext))
        # overwrite out list with items that only have the extension we want
        flattened_url_list = [url for url in flattened_url_list if url.split('.')[-1]==ext]
        
    # if a filepath was spcified to save the resulting list of URLS to
    if list_filepath != None:
        # open a file there to write to
        print('Writing list of URLs to {}'.format(list_filepath))
        with open(list_filepath, "w") as output:
            for row in flattened_url_list:
                # output each url to a separate line in the file
                output.write(str(row) + '\n')
        
    # return the whole list of access urls
    return flattened_url_list