"""
This file hosts the functions that extract data from the shapefiles/GEOJSON files and return that data.
This file also has a geopandas wrapper to extract GeoDataFrames

(C) Eric J. Drewitz 2026
"""
import geopandas as _gpd
import cartopy.crs as _ccrs
import cartopy.io.shapereader as _shapereader
import cartopy.feature as _cfeature

def cartopy_shapefeature(file_path,
                           edgecolor='black',
                           crs=_ccrs.PlateCarree()):
    
    """
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
    
    Returns
    -------
    
    A cartopy.shapefeature from the data inside the shapefile.    
    """   
    
    shape_feature = _cfeature.ShapelyFeature(_shapereader.Reader(file_path).geometries(),
                                   crs=crs, facecolor=(0,0,0,0), edgecolor=edgecolor)
    
    return shape_feature


def get_geometries(file_path,
                  crs='EPSG:4326'):
    
    """
    This function converts the shapefile geometries to a CRS specified by the user using geopandas.
    
    Required Arguments: 
    
    1) file_path (String) - The full filepath to the shapefile. 
    
    Optional Arguments:
    
    1) crs (String) - Default='EPSG:4326' (ccrs.PlateCarree()) - The coordinate reference system the user wants the geometry coordinates in.  
    
    Returns
    -------
    
    A gpd.GeoDataFrame geometry data of the shapefile/GEOJSON in the CRS specified by the user.
    """
    
    gdf = _gpd.read_file(f"{file_path}")
    
    gdf = gdf.to_crs(crs)
    
    return gdf['geometry']


def geodataframe(file_path,
                crs='EPSG:4326'):
    
    """
    This function extracts a gpd.GeoDataFrame from the shapefile/GEOJSON. 
    
    Required Arguments: 
    
    1) file_path (String) - The full filepath to the shapefile. 
    
    Optional Arguments:
    
    1) crs (String) - Default='EPSG:4326' (ccrs.PlateCarree()) - The coordinate reference system the user wants the geometry coordinates in.  
    
    Returns
    -------
    
    A gpd.GeoDataFrame hosting all the data in the shapefile/GEOJSON. 
    """
    
    gdf = _gpd.read_file(f"{file_path}")
    
    gdf = gdf.to_crs(crs)
    
    return gdf
    
    

