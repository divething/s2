# s2

## Instructions for creating a GRASS Location/Mapset
Suppose you have rasters in the European LAEA projection (EPSG:3035), and you want to use them in GRASS.
Use the CRS of one of the rasters to create the new Location and start grass in one go.
Create a new Location using this command:
```bash
grass -c /home/micha/GIS/Europe/Corine_Land_Cover/2012/g100_clc12_V18_5.tif /home/micha/grassdata/LAEA_EU/
# grass = command to initialize GRASS environment
# -c = create new Location
# CRS is taken from the Geotiff file 
# Last is the location for your new GRASSDBASE and LOCATION

grass -c /home/tamir/Documents/sentinel_images_for_burn/processed/indices_products/ari/S2A_MSIL2A_20170511T082011_N0205_R121_T36RXV_20170511T082011_resampled_BandMath.tif /home/tamir/Documents/sentinel_images_for_burn/grass




```
You are now in a GRASS session. Check the projection info and current mapset:
```bash
g.proj -p
g.mapset -p
```
Now create a new working mapset called 'Europe' and check again:
```bash
# Create new mapset
g.mapset -c Europe

g.mapset -c burn

# List all mapsets in Location LAEA_EU
g.mapsets -l
# show current mapset
g.mapset -p
```
Now you can run the python script 'extract_raster_values.py', i.e.:
```bash
./extract_raster_values.py help
```

/home/tamir/Documents/drive/github/s2/extract_raster_values.py input=/home/tamir/Documents/sentinel_images_for_burn/gis_tamir/selected_plots_only_epsg32636.shp /home/tamir/Documents/sentinel_images_for_burn/processed/indices_products/ari /home/tamir/Documents/sentinel_images_for_burn/processed/indices_products/ari/ari_output


drive/github/s2/extract_raster_values.py input=sentinel_images_for_burn/gis_tamir/selected_plots_only_epsg32636.shp tiff_dir=sentinel_images_for_burn/processed/indices_products/ari output_csv=sentinel_images_for_burn/processed/indices_products/ari/output.csv


drive/github/s2/extract_raster_values.py input=sentinel_images_for_burn_2run/gis_tamir/selected_plots_only_epsg32636.shp tiff_dir=sentinel_images_for_burn/processed/indices_products/ari output_csv=sentinel_images_for_burn/processed/indices_products/ari/ari_output.csv












