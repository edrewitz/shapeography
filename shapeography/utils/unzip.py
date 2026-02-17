"""
This file hosts the functions responsible for unzipping the shapefiles

(C) Eric J. Drewitz 2026
"""

import os as _os
import gzip as _gzip

from zipfile import ZipFile as _ZipFile
    
def extract_gzipped_files(file_directory):
    
    """
    This function extracts shapefiles that are zipped in a .gz file
    
    Required Arguments:
    
    1) file_directory (String) - The path of the directory to the initial .gz file. 
    
    Optional Arguments: None
    
    Returns
    -------
    
    A directory of unzipped shapefiles. 
    """

    try:
        for f in _os.listdir(f"{file_directory}"):
            extraction_folder = f.split('.', 1)[0]
            with _gzip.open(f"{file_directory}/{f}", 'rb') as f_in:
                with open(f"{file_directory}/{extraction_folder}", 'wb') as f_out:
                    f_out.write(f_in.read())
    except Exception as e:
        pass
    
    try:
        for f in _os.listdir(f"{file_directory}/{extraction_folder}"):
            ex_folder = f.split('.', 1)[0]
            with _gzip.open(f"{file_directory}/{extraction_folder}/{f}", 'rb') as f_in:
                with open(f"{file_directory}/{extraction_folder}/{ex_folder}", 'wb') as f_out:
                    f_out.write(f_in.read()) 
    except Exception as e:
        pass     
    
    try:    
        for f in _os.listdir(f"{file_directory}"):
            if f.endswith(".gz"):
                _os.remove(f"{file_directory}/{f}")
    except Exception as e:
        pass
    
    try:    
        for f in _os.listdir(f"{file_directory}/{extraction_folder}"):
            if f.endswith(".gz"):
                _os.remove(f"{file_directory}/{extraction_folder}/{f}")
    except Exception as e:
        pass     
    
def extract_files(file_directory):

    """
    This function extracts shapefiles that are zipped in a .zip file
    
    Required Arguments:
    
    1) file_directory (String) - The path of the directory to the initial .zip file. 
    
    Optional Arguments: None
    
    Returns
    -------
    
    A directory of unzipped shapefiles. 
    """
    
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
    try:    
        for f in _os.listdir(f"{file_directory}"):
            if f.endswith(".zip"):
                _os.remove(f"{file_directory}/{f}")
    except Exception as e:
        pass
    
    try:    
        for f in _os.listdir(f"{file_directory}/{extraction_folder}"):
            if f.endswith(".zip"):
                _os.remove(f"{file_directory}/{extraction_folder}/{f}")
    except Exception as e:
        pass