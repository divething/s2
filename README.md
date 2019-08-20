# s2

## Instructions for creating a GRASS Location/Mapset
Suppose you have rasters in the European LAEA projection (EPSG:3035), and you want to use them in GRASS.
Use the CRS of one of the rasters to create the new Location and start grass in one go.
Create a new Location using this command:
```bash
grass -c /home/micha/GIS/Europe/Corine_Land_Cover/2012/g100_clc12_V18_5.tif /home/micha/grassdata/LAEA_EU/
```
You are now in a GRASS session. Check the projection info and current mapset:
```bash
g.proj -p
g.mapset -p
```
Now create a new work mapset called 'Europe' and check again:
```bash
# Create new mapset
g.mapset -c Europe
# List all mapsets in Location LAEA_EU
g.mapsets -l
# show current mapset
g.mapset -p
```
Now you can run the python script 'extract_raster_values.py', i.e.:
```bash
./extract_raster_values.py help
```
