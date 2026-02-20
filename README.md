# shapeography



<img src="https://github.com/edrewitz/shapeography/blob/main/Thumbnails/86506Livingston-Rev-Base.jpg?raw=true" width="200" alt="Alt text" /> <img src="https://github.com/edrewitz/WxData/blob/1be590e9a16033974a592d8cf99f3cd521f95e0b/icons/python%20logo.png?raw=true" width="200" alt="Alt text" />


[![Conda Recipe](https://img.shields.io/badge/recipe-shapeography-green.svg)](https://anaconda.org/conda-forge/shapeography) [![Conda Version](https://img.shields.io/conda/vn/conda-forge/shapeography.svg)](https://anaconda.org/conda-forge/shapeography) ![PyPI](https://img.shields.io/pypi/v/shapeography?label=pypi%20shapeography)
 [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/shapeography.svg)](https://anaconda.org/conda-forge/shapeography) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/shapeography/badges/latest_release_date.svg)](https://anaconda.org/conda-forge/shapeography) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/shapeography/badges/license.svg)](https://anaconda.org/conda-forge/shapeography) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/shapeography/badges/latest_release_relative_date.svg)](https://anaconda.org/conda-forge/shapeography)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18676844.svg)](https://doi.org/10.5281/zenodo.18676844) 

Anaconda Downloads:

[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/shapeography.svg)](https://anaconda.org/conda-forge/shapeography)

PIP Downloads:

![PyPI - Downloads](https://img.shields.io/pypi/dm/shapeography)



**(C) Eric J. Drewitz 2026**

An open-source Python package that manages shapefiles/GEOJSON files and simplifies the process of working with GIS data in Python.

**How To Install**

Copy and paste either command into your terminal or anaconda prompt:

*Install via Anaconda*

`conda install shapeography`

*Install via pip*

`pip install shapeography`

**How To Update To The Latest Version**

Copy and paste either command into your terminal or anaconda prompt:

*Update via Anaconda*

***This is for users who initially installed WxData through Anaconda***

`conda update shapeography`

*Update via pip*

***This is for users who initially installed WxData through pip***

`pip install --upgrade shapeography`

***Jupyter Lab Examples***

1) [Downloading and Plotting the National Weather Service Public Forecast Zones](https://github.com/edrewitz/shapeography-Jupyter-Lab-Examples/blob/main/nws_public_zones.ipynb)
2) [Downloading and Plotting the NOAA/NWS Climate Prediction Center 6-10 Day Probabilistic Precipitation Outlook](https://github.com/edrewitz/shapeography-Jupyter-Lab-Examples/blob/main/cpc_outlook.ipynb)


***Client Module***

[Documentation](https://github.com/edrewitz/shapeography/blob/main/Documentation/client.md#client-module)

The `client` module hosts the client function `get_shapefiles()` that downloads shapefiles/GEOJSON file from a user-defined URL address into a folder locally on your PC.

The user must specify the path and filename and the file is saved to {path}/{filename}. 

This client is also helpful for those using shapeography in automated scripts. If the user keeps the optional argument `refresh=True` - The directory hosting the shapefiles/GEOJSON file will be refreshed as the old files will be deleted and new files downloaded. This can be helpful in automation due to periodic shapefile updates on the server-side as it ensures that the user will always have the most recent and up to date shapefiles/GEOJSON file. 

This client supports users on a VPN/PROXY connection. 

    **Proxy Example**

    proxies=None ---> proxies={
                           'http':'address:port',
                           'https':'address:port'
                        } 

    shapeography.client.get_shapefiles(url, path, filename, proxies=proxies)

***Unzip Module***

[Documentation](https://github.com/edrewitz/shapeography/blob/main/Documentation/unzip.md#unzip-module)

The `unzip` module hosts the function that unzips the shapefiles/GEOJSON file if the file(s) need to be unzipped.

In nearly all cases, shapefile components are within a zipfile server-side so needing to unzip is very common. 

The function `extract_files()` unzips the shapefiles/GEOJSON into a user-specified extraction folder that is automatically generated. 

Supports the following file extentions: .zip, .gz, .tar, .tar.gz

***Geometry Module***

[Documentation](https://github.com/edrewitz/shapeography/blob/main/Documentation/geometry.md#geometry-module)

The `geometry` module hosts functions that extract data from these shapefiles/GEOJSON file and make it significantly easier to work with this data in Python.

The current functions are: 

1) [`cartopy_shapefeature()`](https://github.com/edrewitz/shapeography/blob/main/Documentation/geometry.md#1-cartopy_shapefeature) - Returns a cartopy.shapefeature from the data inside the shapefile/GEOJSON.
2) [`get_geometries()`](https://github.com/edrewitz/shapeography/blob/main/Documentation/geometry.md#2-get_geometries) - Returns a gpd.GeoDataFrame of the geometry data of the shapefile/GEOJSON in the coordinate reference system (CRS) specified by the user. (Default CRS = 'EPSG:4326' --> `ccrs.PlateCarree()`)
3) [`geodataframe()`](https://github.com/edrewitz/shapeography/blob/main/Documentation/geometry.md#3-geodataframe) - Returns gpd.GeoDataFrame hosting all the data in the shapefile/GEOJSON in the coordinate reference system (CRS) specified by the user. (Default CRS = 'EPSG:4326' --> `ccrs.PlateCarree()`)

# Citations

1) **cartopy**: Phil Elson, Elliott Sales de Andrade, Greg Lucas, Ryan May, Richard Hattersley, Ed Campbell, Andrew Dawson, Bill Little, Stephane Raynaud, scmc72, Alan D. Snow, Ruth Comer, Kevin Donkers, Byron Blay, Peter Killick, Nat Wilson, Patrick Peglar, lgolston, lbdreyer, … Chris Havlin. (2023). SciTools/cartopy: v0.22.0 (v0.22.0). Zenodo. https://doi.org/10.5281/zenodo.8216315
2) **geopandas**: Kelsey Jordahl, Joris Van den Bossche, Martin Fleischmann, Jacob Wasserman, James McBride, Jeffrey Gerard, … François Leblanc. (2020, July 15). geopandas/geopandas: v0.8.1 (Version v0.8.1). Zenodo. http://doi.org/10.5281/zenodo.3946761
3) **requests**: K. Reitz, "Requests: HTTP for Humans". Available: https://requests.readthedocs.io/.
