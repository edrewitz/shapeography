# Client Module

The shapeography `client` module hosts the function `get_shapefiles()` that acts as the client to retrieve shapefiles/GEOJSON files at a specified URL and then manage those files locally.

The `get_shapefiles()` has support for users on VPN/PROXY connections. 

***def get_shapefiles(url,
             path,
             filename,
             proxies=None,
             chunk_size=8192,
             notifications='on',
             refresh=True):***

This function is the client that downloads and locally manages shapefiles and GEOJSON files. 

This client supports VPN/PROXY connections. 

Required Arguments:

1) url (String) - The download URL to the file. 

2) path (String) - The directory where the file is saved to. 

3) filename (String) - The name the user wishes to save the file as. 

Optional Arguments:

1) proxies (dict or None) - Default=None. If the user is using proxy server(s), the user must change the following:

       proxies=None ---> proxies={
                           'http':'http://url',
                           'https':'https://url'
                        } 
                        
        get_shapefiles(url, path, filename, proxies=proxies)
                    
2) chunk_size (Integer) - Default=8192. The size of the chunks when writing the GRIB/NETCDF data to a file.

3) notifications (String) - Default='on'. Notification when a file is downloaded and saved to {path}

4) refresh (Boolean) - Default=True. When set to True, the branch that hosts the shapefiles/GEOJSON files is completely
   cleaned out and a new set of shapefiles/GEOJSON is downloaded with each run. This is recommended for those using 
   shapeography in automated tasks to account for periodic shapefile/GEOJSON updates on the servers that host the shapefiles/GEOJSONs.

**Returns**

Zipped Shapefile and/or GEOJSON to f:{path}/{filename} 
