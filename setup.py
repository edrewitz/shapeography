
import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
  print("ERROR: User is running a version of Python older than Python 3\nTo use shapeography, the user must be using Python 3 or newer.")

setup(
    name = "shapeography",
    version = "0.1",
    packages = find_packages(),
    install_requires=[
        "cartopy>=0.24.0",
        "geopandas>=1.1.0"
    ],
    author="Eric J. Drewitz",
    description="A Client that manages shapefiles and geojsons",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown"

)
