"""Convert raw image data into PNG images files."""

import csv

from thermal_data import ThermalData

data = None

with open('thermal.csv') as in_file:
    data = [x for x in csv.reader(in_file)]

img_count = 0
img_output_index = 0
thermal = ThermalData()

for h in data:
    try:
        img = thermal.get_data(h)
    except TypeError:
        continue
    except ValueError:
        continue

    img.save('images/img{0:04}.png'.format(img_output_index))
    img_count += 1
    img_output_index += 1
