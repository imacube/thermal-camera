import csv

from thermal_data import ThermalData

data = None

with open('thermal.csv') as in_file:
    data = [x for x in csv.reader(in_file)]

img_count = 0
img_output_index = 0
thermal = ThermalData()

for h in data:
    if 3150 < img_count < 3368:
        pass
    else:
        img_count += 1
        continue
    try:
        img = thermal.get_data(h)
    except TypeError:
        continue

    img.save('images-person/img{0:04}.png'.format(img_output_index))
    img_count += 1
    img_output_index += 1
