gdal_translate SENTINEL2_L2A:/vsizip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.zip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.SAFE/MTD_MSIL2A.xml:10m:EPSG_32636 10m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2

gdal_translate SENTINEL2_L2A:/vsizip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.zip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.SAFE/MTD_MSIL2A.xml:20m:EPSG_32636 20m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2

gdal_translate SENTINEL2_L2A:/vsizip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.zip/S2B_MSIL2A_20190225T081919_N0211_R121_T36RXV_20190225T125206.SAFE/MTD_MSIL2A.xml:60m:EPSG_32636 60m.tif -co TILED=YES --config GDAL_CACHEMAX 1000 --config GDAL_NUM_THREADS 2
       
    
