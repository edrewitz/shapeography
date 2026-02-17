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


def get_kml_geometry(file_path):
    
    """
    This function returns the geometry of a KML file.
    
    Required Arguments:
    
    1) file_path (String) - The path to the KML file
    
    Returns
    -------
    
    The geometry of the KML file    
    """

    kml_filename = "your_file.kml"

    with open(kml_filename, 'r', encoding='utf-8') as f:
        doc = f.read().encode('utf-8')

    k = _kml.KML()
    k.from_string(doc)

    # Iterate through features (Document, Folder, Placemark, etc.)
    for feature in k.features():
        if isinstance(feature, _kml.Document):
            for sub_feature in feature.features():
                for placemark in sub_feature.features():
                    if placemark.geometry:
                        print(f"Geometry type: {type(placemark.geometry).__name__}")
                        # You can access the coordinates, e.g., for a Point
                        if hasattr(placemark.geometry, 'coords'):
                            print(f"Coordinates: {list(placemark.geometry.coords)}")
                        # For Polygon geometries, you can access the exterior coordinates
                        elif hasattr(placemark.geometry, 'exterior'):
                            print(f"Coordinates: {list(placemark.geometry.exterior.coords)}")

        # Handle cases where placemarks are directly under the KML root or other features
        elif isinstance(feature, _kml.Placemark):
            if feature.geometry:
                print(f"Geometry type: {type(feature.geometry).__name__}")
                if hasattr(feature.geometry, 'coords'):
                    print(f"Coordinates: {list(feature.geometry.coords)}")



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
    
    

