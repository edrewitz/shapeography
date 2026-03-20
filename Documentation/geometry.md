# Geometry Module

**Table of Contents**

1) [`cartopy_shapefeature()`](https://github.com/edrewitz/shapeography/blob/main/Documentation/geometry.md#1-cartopy_shapefeature)
2) [`get_geometries()`](https://github.com/edrewitz/shapeography/blob/main/Documentation/geometry.md#2-get_geometries)
3) [`geodataframe()`](https://github.com/edrewitz/shapeography/blob/main/Documentation/geometry.md#3-geodataframe)


The shapeography `geometry` module hosts the functions for the following:

#### 1) `cartopy_shapefeature()` 

***def cartopy_shapefeature(file_path,
                           edgecolor='black',
                           crs=_ccrs.PlateCarree()):***

This function extracts the geometries from the shapefile and returns those geometries to the user.

Required Arguments: 

1) file_path (String) - The full filepath to the shapefile. 

Optional Arguments: 

1) edgecolor (String) - Default='black'. The color of the bordr demarcations on the map. 

2) crs (cartopy.crs) - Default=ccrs.PlateCarree(). The coordinate reference system of the shape feature. 
    Most cases, PlateCarree() (lat/lon) is the preferred coordinate reference system. For those who need to
    use a different coordinate reference system, you will need to import cartopy into your script, define your
    own coordinate reference system with cartopy.crs and pass the reference system object as crs=crs. Please
    see cartopy.crs documentation for more information regarding cartopy coordinate reference systems.
    
  **Returns**
    
A cartopy.shapefeature from the data inside the shapefile.    

#### 2) `get_geometries()`

***def get_geometries(file_path,
                  crs='EPSG:4326'):***

This function converts the shapefile geometries to a CRS specified by the user using geopandas.

Required Arguments: 

1) file_path (String) - The full filepath to the shapefile. 

Optional Arguments:

1) crs (String) - Default='EPSG:4326' (ccrs.PlateCarree()) - The coordinate reference system the user wants the geometry coordinates in.  

**Returns**

A gpd.GeoDataFrame of the geometry data of the shapefile/GEOJSON in the CRS specified by the user.

#### 3) `geodataframe()`

***def geodataframe(file_path,
                crs='EPSG:4326'):***

This function extracts a gpd.GeoDataFrame from the shapefile/GEOJSON. 

Required Arguments: 

1) file_path (String) - The full filepath to the shapefile. 

Optional Arguments:

1) crs (String) - Default='EPSG:4326' (ccrs.PlateCarree()) - The coordinate reference system the user wants the geometry coordinates in.  

**Returns**

A gpd.GeoDataFrame hosting all the data in the shapefile/GEOJSON. 


