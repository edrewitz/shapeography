"""
This file hosts the client that retrieves the shapefile/geojson from the web.

(C) Eric J. Drewitz 2026
"""

import requests as _requests
import os as _os 
import time as _time
import sys as _sys
import shutil as _shutil

def get_shapefiles(url,
             path,
             filename,
             proxies=None,
             chunk_size=8192,
             notifications='on',
             refresh=True):
    
    """
    This function is the client that retrieves gridded weather/climate data (GRIB2 and NETCDF) files. 
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
                        
    2) chunk_size (Integer) - Default=8192. The size of the chunks when writing the GRIB/NETCDF data to a file.
    
    3) notifications (String) - Default='on'. Notification when a file is downloaded and saved to {path}
    
    4) clear_recycle_bin (Boolean) - (Default=False in WxData >= 1.2.5) (Default=True in WxData < 1.2.5). When set to True, 
        the contents in your recycle/trash bin will be deleted with each run of the program you are calling WxData. 
        This setting is to help preserve memory on the machine. 
    
    Returns
    -------
    
    Gridded weather/climate data files (GRIB2 or NETCDF) saved to {path}    
    """
    
    if refresh == True:
        try:
            _shutil.rmtree(f"{path}")
        except Exception as e:
            pass
    else:
        pass
    
    try:
        _os.makedirs(f"{path}")
    except Exception as e:
        pass

    if proxies == None:
        try:
            with _requests.get(url, stream=True) as r:
                r.raise_for_status() 
                with open(f"{path}/{filename}", 'wb') as f:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        f.write(chunk)
            if notifications == 'on':
                print(f"Successfully saved {filename} to f:{path}")
            else:
                pass
        except _requests.exceptions.RequestException as e:
            for i in range(0, 6, 1):
                if i < 3:
                    print(f"Alert: Network connection unstable.\nWaiting 30 seconds then automatically trying again.\nAttempts remaining: {5 - i}")
                    _time.sleep(30)
                else:
                    print(f"Alert: Network connection unstable.\nWaiting 60 seconds then automatically trying again.\nAttempts remaining: {5 - i}")
                    _time.sleep(60)  
                    
                try:
                    with _requests.get(url, stream=True) as r:
                        r.raise_for_status() 
                        with open(f"{path}/{filename}", 'wb') as f:
                            for chunk in r.iter_content(chunk_size=chunk_size):
                                f.write(chunk)
                    if notifications == 'on':
                        print(f"Successfully saved {filename} to f:{path}")  
                    break
                except _requests.exceptions.RequestException as e:
                    i = i 
                    if i >= 5:
                        print(f"Error - File Cannot Be Downloaded.\nError Code: {e}")    
                        _sys.exit(1)      
                        
        finally:
            if r:
                r.close() # Ensure the connection is closed.
            
    else:
        try:
            with _requests.get(url, stream=True, proxies=proxies) as r:
                r.raise_for_status() 
                with open(f"{path}/{filename}", 'wb') as f:
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        f.write(chunk)
            if notifications == 'on':
                print(f"Successfully saved {filename} to f:{path}")
            else:
                pass
        except _requests.exceptions.RequestException as e:
            for i in range(0, 6, 1):
                if i < 3:
                    print(f"Alert: Network connection unstable.\nWaiting 30 seconds then automatically trying again.\nAttempts remaining: {5 - i}")
                    _time.sleep(30)
                else:
                    print(f"Alert: Network connection unstable.\nWaiting 60 seconds then automatically trying again.\nAttempts remaining: {5 - i}")
                    _time.sleep(60)  
                    
                try:
                    with _requests.get(url, stream=True, proxies=proxies) as r:
                        r.raise_for_status() 
                        with open(f"{path}/{filename}", 'wb') as f:
                            for chunk in r.iter_content(chunk_size=chunk_size):
                                f.write(chunk)
                    if notifications == 'on':
                        print(f"Successfully saved {filename} to f:{path}")  
                    break
                except _requests.exceptions.RequestException as e:
                    i = i 
                    if i >= 5:
                        print(f"Error - File Cannot Be Downloaded.\nError Code: {e}")    
                        _sys.exit(1)    
                        
        finally:
            if r:
                r.close() # Ensure the connection is closed.


    
    
    

 