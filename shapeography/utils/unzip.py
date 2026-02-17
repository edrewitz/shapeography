"""
This file hosts the functions responsible for unzipping the shapefiles

(C) Eric J. Drewitz 2026
"""

import os as _os
from zipfile import ZipFile as _ZipFile
    
def extract_files(file_path):

    """
    This function extracts zipped files into an extraction folder. 
    
    Required Arguments:
    
    1) file_path (String) - The path to the zipped shapefiles
    
    Optional Arguments: None
    
    Returns
    -------
    
    Unzipped shapefiles into an unzipped extraction folder
    """
    
    try:
        for f in _os.listdir(f"{file_path}"):
            extraction_folder = f.split('.', 1)[0]
            with _ZipFile(f"{file_path}/{f}", 'r') as zObject:
                zObject.extractall(f"{file_path}/{extraction_folder}")
            zObject.close()
    except Exception as e:
        pass
    
    try:    
        for f in _os.listdir(f"{file_path}/{extraction_folder}"):
            ex_folder = f.split('.', 1)[0]
            with _ZipFile(f"{file_path}/{extraction_folder}/{f}", 'r') as zObject:
                zObject.extractall(f"{file_path}/{extraction_folder}/{ex_folder}")
            zObject.close()   
    except Exception as e:
        pass     
    try:    
        for f in _os.listdir(f"{file_path}"):
            if f.endswith(".zip"):
                _os.remove(f"{file_path}/{f}")
    except Exception as e:
        pass
    
    try:    
        for f in _os.listdir(f"{file_path}/{extraction_folder}"):
            if f.endswith(".zip"):
                _os.remove(f"{file_path}/{extraction_folder}/{f}")
    except Exception as e:
        pass