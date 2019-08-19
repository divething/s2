#!/usr/bin/python
"""
Description: Loop through a directory of image files,
    extract raster value at given point locations

Requirements:   Must be run withing a GRASS GIS session,

Command line parameters: input: full path to vector shapefile of points
                        tiff_dir: full path to directory containing GeoTiffs
                        output: Full path to output CSV

Author:     Micha Silver
Date:       19/08/2019
Revisions:
"""

#%module
#% description: Extract raster values of many images at point locations
#%end

#%option G_OPT_V_INPUT
#% key: input
#% description: Path to input point shapefile 
#% required: yes
#%end

#%option
#% key: tiff_dir
#% description: Directory containing Geotiff files
#% required: no
#%end

#%option 
#% key: output_csv
#% type: string
#% description: Full path to output CSV file
#% required: yes
#%end

import os
import sys
from glob import glob
import grass.script as gscript
from datetime import datetime as DT


def main():
    if "GISBASE" not in os.environ:
        gscript.message("""You must be in GRASS GIS to run this program.
                        Exiting...""")
        sys.exit(1)

    # Starting
    t0 = DT.now()
    print("\n   %s - Beginning process" % t0)

    # Import vector
    input_vect = options['input']
    tiff_dir = options['tiff_dir']
    output_csv = options['output_csv']
    vect_name = os.path.splitext(os.path.split(input_vect)[1])[0]
    # Make sure no invalid characters in file name
    vect_name = vect_name.replace(" ", "").replace(".", "_")
    gscript.run_command('v.import',
                        input_=options['input'],
                        output=vect_name, overwrite=True)

    # Assume Geotiffs are named with tif extension (lowercase)
    i = 0
    for t in glob(tiff_dir + "*.tif"):
        # Import one tiff
        rast_name = os.path.splitext(os.path.split(t)[1])[0]
        # Make sure no invalid characters in file name
        rast_name = rast_name.replace(" ", "").replace(".", "_")
        rast_name.replace("-", "_")
        gscript.run_command('r.import',
                            input_=t, output=rast_name, overwrite=True)
        # Always set the region
        gscript.run_command('g.region',
                            rast=rast_name, flags="a")
        # Extract value for all points in vector
        col_name = "tiff_" + str(i)
        i += 1
        gscript.run_command('v.what.rast',
                            map_=vect_name, raster=rast_name, column=col_name)
        # Remove the raster
        gscript.run_command('g.remove',
                            type_="rast", name=rast_name, flags="f")

    # Loop complete, now export vector attrib table to CSV
    gscript.run_command('v.out.ogr',
                        input_=vect_name, output=output_csv, format="CSV")

    # Starting
    t1 = DT.now()
    ttl_secs = (t1 - t0).seconds
    print("\n   %s - Process complet after %d seconds" % (t0, ttl_secs))


if __name__ == "__main__":
    options, flags = gscript.parser()
    sys.exit(main())
