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

"""
The commented lines below  (beginning with '#%'are for the GRASS parser.
This is how command line arguments are defined for python scripts in GRASS.
Three CLI arguments are defined: input, tiff_dir and output_csv
All are required.
The command on line 133 reads the arguments using g.parser
and fills two string arrays: 'options' and 'flags'
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
#% type: string
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
from datetime import datetime as DT
try:
    import grass.script as gscript
except ImportError:
    print("""You must be in a running GRASS GIS session.
          Exiting...""")
    sys.exit(1)


def main():
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
                        input_=input_vect,
                        output=vect_name, overwrite=True)

    # Assume Geotiffs are named with tif extension (lowercase)
    tiff_list = glob(os.path.join(tiff_dir, "*.tif"))
    for i in range(len(tiff_list)):
        # ahhhha thats how you set up a loop - i is the counter
        # and i guess len is the firet dimention of tiff_list

        """
        MS:
            Exactly.
            Just to note that in python, lists are indexed from 0
            so the first element of tiff_list is tiff_list[0]
            and "range(len(a_list))" goes from 0 to (length-1)
        """

        # Import one tiff
        t = tiff_list[i]

        rast_name = os.path.splitext(os.path.split(t)[1])[0]
        # Make sure no invalid characters in file name
        rast_name = rast_name.replace(" ", "").replace(".", "_")
        rast_name.replace("-", "_")  # replace - with _
        gscript.run_command('r.import',
                            input_=t, output=rast_name, overwrite=True)
        # Always set the region
        gscript.run_command('g.region',
                            rast=rast_name, flags="a")

        # Extract value for all points in vector
	# =============================================================================
	#   now extract file name procedure
	# =============================================================================
	#        col_name = "tiff_" + str(i).zfill(2)   
    
        
        components = rast_name.split("_")
        
        
        
# =============================================================================
#   make the column name
# =============================================================================
        col = (components[0], components[2])
        col_name = "_".join(col)        
# =============================================================================
#   here is the important stuff
# =============================================================================
       
        

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
