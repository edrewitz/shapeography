"""
This file hosts the various different border demarcations.

(C) Eric J. Drewitz 2025
"""

def census_demarcations(demarcation,
                        resolution):
    
    """
    This function maps the plain language demarcation the user inputs to the URL filename
    
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
     
    Optional Arguments: None
    
    Returns
    -------
    
    The folder name of the zipped folder to be downloaded from census.gov
    """
    
    if resolution == '500k':
        
        demarcations = {
            
            'American Indian Alaska Native Native Hawaiian Areas':'cb_2024_us_aiannh_500k.zip',
            'American Indian Tribal Subdivision':'cb_2024_us_aitsn_500k.zip',
            'Alaska Native Regional Corporation':'cb_2024_02_anrc_500k.zip',
            'Block Group':'cb_2024_us_tbg_500k.zip',
            'Congressional District (119th Congress)':
            'Consolidated City'
            'County'
            'Portion of county within a congressional district'
            'County Subdivision'
            'National Division (Subdivisions of Regions)'
            'Elementary School District'
            'Estate subminor civil division (sub-MCD) in U.S. Virgin Islands'
            'National outline'
            'Place' 
            'National Region (Northeast, Southeast, Midwest and West)'  
            'Secondary School District' 
            'School District Administrative Area'
            'State Legislative District Lower Chamber'
            'State Legislative District Upper Chamber'
            'State and Equivalent'
            'Subbarrio Legally defined subdivisions of county'
            'Tribal Block Group'
            'Census Tract' 
            'Tribal Census Tract'
            'Unified School District'
            
        }
        
        



return demarcations[demarcation]