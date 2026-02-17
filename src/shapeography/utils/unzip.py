"""
This file hosts the functions responsible for unzipping the shapefiles

(C) Eric J. Drewitz 2026
"""

import os as _os
import gzip as _gzip
import tarfile as _tarfile

from zipfile import ZipFile as _ZipFile
    
def extract_zipped_files(file_directory,
                         file_type='.zip'):

    """
    This function extracts shapefiles that are zipped in a .zip file
    
    Required Arguments:
    
    1) file_directory (String) - The path of the directory to the initial .zip file. 
    
    Optional Arguments: None
    
    Returns
    -------
    
    A directory of unzipped shapefiles. 
    """
    
    file_type = file_type.lower()
    
    if file_type == '.zip':
        try:
            for f in _os.listdir(f"{file_directory}"):
                extraction_folder = f.split('.', 1)[0]
                with _ZipFile(f"{file_directory}/{f}", 'r') as zObject:
                    zObject.extractall(f"{file_directory}/{extraction_folder}")
                zObject.close()
        except Exception as e:
            pass
        
        try:    
            for f in _os.listdir(f"{file_directory}/{extraction_folder}"):
                ex_folder = f.split('.', 1)[0]
                with _ZipFile(f"{file_directory}/{extraction_folder}/{f}", 'r') as zObject:
                    zObject.extractall(f"{file_directory}/{extraction_folder}/{ex_folder}")
                zObject.close()   
        except Exception as e:
            pass 
    
    elif file_type == '.tar.gz':
        try:
            for f in _os.listdir(f"{file_directory}"):
                extraction_folder = f.split('.', 1)[0]
                with _tarfile.open(f"{file_directory}/{f}", "r:gz") as tar:
                    tar.extractall(path=f"{file_directory}/{extraction_folder}")
        except Exception as e:
            pass
        
        try:
            for f in _os.listdir(f"{file_directory}/{extraction_folder}"):
                ex_folder = f.split('.', 1)[0]
                with _tarfile.open(f"{file_directory}/{extraction_folder}/{f}", "r:gz") as tar:
                    tar.extractall(path=f"{file_directory}/{extraction_folder}/{ex_folder}")
        except Exception as e:
            pass
        
    try:    
        for f in _os.listdir(f"{file_directory}"):
            if f.endswith(file_type):
                _os.remove(f"{file_directory}/{f}")
    except Exception as e:
        pass
    
    try:    
        for f in _os.listdir(f"{file_directory}/{extraction_folder}"):
            if f.endswith(file_type):
                _os.remove(f"{file_directory}/{extraction_folder}/{f}")
    except Exception as e:
        pass