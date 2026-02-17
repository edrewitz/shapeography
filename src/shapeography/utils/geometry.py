"""
This file hosts the functions that extract the geometries from either the shapefile or geojson and return those geometries to the user.

(C) Eric J. Drewitz 2026
"""
import geopandas as _gpd
import cartopy.crs as _ccrs
import cartopy.io.shapereader as _shapereader
import cartopy.feature as _cfeature

from fastkml import(
    kml as _kml, 
)
from fastkml.utils import find_all as _find_all

def _parse_kml_features(element):
    """Recursively yields features from KML elements (Document, Folder, Placemark)"""
    if not hasattr(element, 'features'):
        return
    for feature in element:
        if isinstance(feature, _kml.Placemark):
            yield feature
        else:
            yield from _parse_kml_features(feature)
            
            


def get_kml_geometry(file_path):
    
    """
    This function returns the geometry of a KML file.
    
    Required Arguments:
    
    1) file_path (String) - The path to the KML file
    
    Returns
    -------
    
    The geometry of the KML file    
    """


    with open(file_path, 'rb') as f:
        k = _kml.KML()
        k.from_string(f.read())

    for placemark in _parse_kml_features(k):
        print(f"* Name: {placemark.name}")
        if placemark.geometry:
            print(f"  Geometry Type: {placemark.geometry.geom_type}")
            print(f"  Coordinates: {list(placemark.geometry.coords)}")

def get_geojson_geometry(file_path):
    
    """
    This function extracts the geometries from the geojson and returns those geometries to the user.
    
    Required Arguments: 
    
    1) file_path (String) - The full filepath to the geojson
    
    Optional Arguments: None
    
    Returns
    -------
    
    The geometry of the geojson    
    """
    
    crs = _ccrs.PlateCarree()
    gdf = _gpd.read_file(file_path)
    gdf_reproj = gdf.to_crs(crs.proj4_init)
    
    shapes = gdf_reproj['geometry']
    
    return shapes


def get_shapefile_geometry(file_path,
                           edgecolor='black'):
    
    """
    This function extracts the geometries from the shapefile and returns those geometries to the user.
    
    Required Arguments: 
    
    1) file_path (String) - The full filepath to the shapefile. 
    
    Optional Arguments: 
    
    1) edgecolor (String) - Default='black'. The color of the bordr demarcations on the map. 
    
    Returns
    -------
    
    The geometry of the shapefile    
    """   
    
    shape_feature = _cfeature.ShapelyFeature(_shapereader.Reader(file_path).geometries(),
                                   crs=_ccrs.PlateCarree(), facecolor=(0,0,0,0), edgecolor=edgecolor)
    
    return shape_feature


def convert_shapefile_crs(file_path,
                          crs='EPSG:4326'):
    
    """
    This function converts the shapefile geometries to a CRS specified by the user using geopandas.
    
    Required Arguments: 
    
    1) file_path (String) - The full filepath to the shapefile. 
    
    Optional Arguments:
    
    1) crs (String) - Default='EPSG:4326' (PlateCarree) - The coordinate reference system the user wants the geometry coordinates in.  
    
    Returns
    -------
    
    The geometry of the shapefile in the CRS specified by the user.
    """
    
    gdf = _gpd.read_file(f"{file_path}")
    
    gdf = gdf.to_crs(crs)
    
    return gdf['geometry']
    
    

