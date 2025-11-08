"""
This file hosts the client that retrieves the shapefile from the web.

(C) Eric J. Drewitz 2025
"""

import urllib.request
import os
import sys

from shapeography.census.urls import get_census_url 
from shapeography.noaa.urls import get_noaa_url
from shapeography.usda.urls import get_usda_url
from shapeography.nifc.urls import get_nifc_url
from shapeography.calfire.urls import get_calfire_url

from shapeography.census.demarcations import census_demarcations
from shapeography.noaa.demarcations import noaa_demarcations
from shapeography.usda.demarcations import usda_demarcations
from shapeography.nifc.demarcations import nifc_demarcations
from shapeography.calfire.demarcations import calfire_demarcations

from shapeography.utils.geometry import get_geometry
from shapeography.utils.unzip import extract_zipped_files

def get_census_borders(demarcation,
                       resolution,
                       save_location='default'):
    
    """
    This function scans for the shapefiles associated with the census demarcations specified by the user.
    
    If the shapefiles exist on the local PC in the specified path (save_location), the function will then pass the
    downloading and unzipping of the files. Otherwise, the client will download and unzip the files and then read the 
    geometries.
    
    Required Arguments:
    
    1) demarcation (String) - The border demarcation.
    
    You can find more information regarding census demarcations at:
    
    https://www2.census.gov/geo/tiger/GENZ2024/2024_file_name_def.pdf
    
    Border Demarcations
    -------------------
    
    1) 'American Indian Alaska Native Native Hawaiian Areas'
    2) 'American Indian Tribal Subdivision'
    3) 'Alaska Native Regional Corporation'
    4) 'Block Group'
    5) 'Congressional District (119th Congress)'
    6) 'Consolidated City'
    7) 'County'
    8) 'Portion of county within a congressional district'
    9) 'County Subdivision'
    10) 'National Division (Subdivisions of Regions)'
    11) 'Elementary School District'
    12) 'Estate subminor civil division (sub-MCD) in U.S. Virgin Islands'
    13) 'National outline'
    14) 'Place' 
    15) 'National Region (Northeast, Southeast, Midwest and West)'  
    16) 'Secondary School District' 
    17) 'School District Administrative Area'
    18) 'State Legislative District Lower Chamber'
    19) 'State Legislative District Upper Chamber'
    20) 'State and Equivalent'
    21) 'Subbarrio Legally defined subdivisions of county'
    22) 'Tribal Block Group'
    23) 'Census Tract' 
    24) 'Tribal Census Tract'
    25) 'Unified School District'
    
    2) resolution (String) - The resolution of the borders.
    
        Resolution
        ----------
        1) '500k'
        2) '5m'
        3) '20m'
        
        Resolution Scale
        ------------------    
        o 500k = 1:500,000
        o 5m = 1:5,000,000
        o 20m = 1:20,000,000
     
    Optional Arguments: 
    
    1) save_location (String) - Default='default'. The path specified by the user to save the shapefiles.
       If 'default' is selected, the shapefiles will be saved to f:demarcation
    
    Returns
    -------
    
    The geometries in the shapefile.    
    """
    
    resolutions = ['500k',
                   '5m',
                   '20m']
    
    if resolution not in resolutions:
        print(f"Error: User entered an invalid resolution of {resolution}.\nDefaulting to 500k")
        resolution = '500k'
        
    else:
        pass
    
    if save_location == 'default':
        path = f"{demarcation}/{resolution}"
    else:
        path = save_location
        
    try:
        os.mkdirs(f"{path}")
    except Exception as e:
        pass
    
    folder = census_demarcations(demarcation,
                                 resolution)
    
    download = False
    if os.path.exists(f"{path}/{folder}"):
        if len(os.listdir(f"{path}/{folder}")) == 0:
            download = True
        else:
            pass
    else:
        pass
        
    
    if download == True:
    
        url = get_census_url(demarcation,
                            resolution)
        
        urllib.requests.urlretrieve(f"{url}", f"{path}/{folder}")
        
    
    
    

 