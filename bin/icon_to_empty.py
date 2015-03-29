#!/usr/bin/python3

from PIL import Image
import glob
import re
from io import StringIO
import os

for filename in glob.glob('*.png') :
    png = Image.open(filename)
    width, height = png.size
    print('filename : {0} ({1} x {2})'.format(filename, width, height))
    img = Image.new('RGBA',(width, height))
    img.save(filename, 'PNG')

for filename in glob.glob('*.xpm') :
    # print('filename : {0}'.format(filename))
    with open(filename) as f:
        content = f.readlines()
        content_started = False
        for line in content:
            if (not content_started) :
                if line.startswith('static') :
                    image_name = re.search('(\w+)\[\]', line)
                    image_name = image_name.group(1)
                    # print(image_name)
                    content_started = True
            else :
                # print(line)
                width, height, *rest = line.strip('"').split()
                xpm = StringIO()
                xpm.write('/* XPM *\n')
                xpm.write('static char * {0}[] = {{\n'.format(image_name))
                xpm.write('"{0} {1} 1 1",\n'.format(width, height))
                xpm.write('" 	c None",\n'.format(width, height))
                for i in range(0, int(height) - 1) :
                    xpm.write('"{0}",\n'.format(' ' * int(width)))
                xpm.write('"{0}"}};\n'.format(' ' * int(width)))
                # print(xpm.getvalue())
                xpm_file = open(filename, "w")
                xpm_file.write(xpm.getvalue())
                xpm_file.close()
                break;

    print('filename : {0} ({1} x {2})'.format(filename, width, height))
