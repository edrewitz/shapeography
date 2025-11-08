from zipfile import ZipFile

def extract_zipped_files(file_path, 
                         extraction_folder):

    """
    This function unzips a file in a folder. 

    Required Arguments:

    1) file_path (String) - The path to the file that needs unzipping.

    2) extraction_folder (String) - The folder that the zipped files are located in.

    Returns
    -------
    
    The unzipped shapefiles in the extraction folder. 
    """

    with ZipFile(file_path, 'r') as zObject:
        zObject.extractall(extraction_folder)
    zObject.close()