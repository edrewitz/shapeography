# Unzip Module

The shapeography `unzip` module hosts the function `extract_files()` to unzip shapefiles/GEOJSON files.

***def extract_files(file_directory,
                    file_extension='.zip'):***

This function extracts shapefiles that are zipped in a .zip file

Required Arguments:

1) file_directory (String) - The path of the directory to the initial .zip file. 

Optional Arguments: 

1) file_extension (String) - Default='.zip'. - The extension of the zip file. 

    Supported zip file extentions
    -----------------------------
        
        1) .zip
        2) .gz
        3) .tar.gz
        4) .tar

Returns
-------

A directory of unzipped shapefiles. 
