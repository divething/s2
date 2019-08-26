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
        """
        ==================================================================
        TC: Exercise 1
        Can you explain the indices [1] and [0] below?
        >>>>>>>>>>>>>
        hey i already answered that in the previous code
        (and implimented it as a show off.....)
        t is the file with its path and everthing....
         '/home/tamir/Documents/sentinel_images_for_burn/originals/temp/S2A_MSIL2A_20180416T081601_N0207_R121_T36RXV_20180416T103632.SAFE
        split breaks it into path and file.
        so [1] relates o the secon place which is the name of the file
        os.path.split(t)[1] is the name of the file but with the format suffix
        os.path.splitext(os.path.split(t)[1])[0]
        is the same but without the suffix
        (the zero tells the splitext to keep the first component....)
        ==================================================================
        """
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
        """
        ==================================================================
        TC: Exercise 2
        The col_name variable below is simply a string with
        the incremented index 'i', formatted with two leading zeros.
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # one....  two digits all tofether - eg
        i = 1
        col_name = "tiff_" + str(i).zfill(2)
        Out[21]: 'tiff_01'
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        Change the code to make the col_name variable below
        as a substring of the tiff filename
        ==================================================================

        MS:
            How would you improve the column names?
            Don't you want each column to contain i.e. the data of the image?
            Try to extract the date from the S2 file name,
            and use that to set the col_name variable

        """
        
#        namesplit = (s2_file_components[4].split("_"))
#        s2_file_components = ((s2_file_components + namesplit))
           
        
        
        
        
        col_name = "tiff_" + str(i).zfill(2)
        gscript.run_command('v.what.rast',
                            map_=vect_name, raster=rast_name, column=col_name)
        # Remove the raster
        gscript.run_command('g.remove',
                            type_="rast", name=rast_name, flags="f")

    # Loop complete, now export vector attrib table to CSV
    gscript.run_command('v.out.ogr',
                        input_=vect_name, output=output_csv, format="CSV")
    """
    ==================================================================
    TC: Exercise 3
    Change the line above to use the v.out.ascii grass command
    What are the differences?  (Use the "c" flag to v.out.ascii)
    >>>>>>>>>>>>>
    so the site said -
        Convert a GRASS binary vector map to a GRASS ASCII vector map
    i guss that what it means is that you get an output (vector file)
        that is grass ready.
    i don't remember if i ever used an ascii file specifically...
    not sure how and where to drop in the flag but it should look like this
    (i added the option type to specify point output
    but im not sure its nessesary).

    MS:
        Not necessary. The old "standard" ASCII format is used
        only in some unusual situations,
        The default is "point".

    gscript.run_command('v.out.ascii',
                        input_=vect_name, -c , format="point", columns="*")

    MS:
    flags are added to a "run_command" call with: flags="c"
    so:
        gscript.run_command('v.out.ascii',
                        input_=vect_name, flags="c" ,
                        format="point", columns="*")
    Also: careful with the separator. GRASS, by default, uses "|"
    If I want CSV I have to do:
        gscript.run_command('v.out.ascii',
                            input_=vect_name, flags="c" ,
                            format="point", columns="*",
                            separator="comma")


    or just this?
    gscript.run_command('v.out.ascii',
                        input_=vect_name, -c , format="standard")

    i couldnt find anywhere a written example using this flag...
    (http://wgbis.ces.iisc.ernet.in/grass/grass71/manuals/v.out.ascii.html)

    i will be happy for a 2min reminder on how to apply syntex like that...
    ==================================================================
    """
    # Starting
    t1 = DT.now()
    ttl_secs = (t1 - t0).seconds
    print("\n   %s - Process complet after %d seconds" % (t0, ttl_secs))


if __name__ == "__main__":
    options, flags = gscript.parser()
    sys.exit(main())
