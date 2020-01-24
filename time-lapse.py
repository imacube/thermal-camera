import colorsys
import io
import os
import time
import csv

import seeed_mlx90640
from PIL import Image


def main():
    mlx = seeed_mlx90640.grove_mxl90640()
    mlx.refresh_rate = seeed_mlx90640.RefreshRate.REFRESH_2_HZ  # The fastest for raspberry 4
    with open('thermal.csv', 'a') as csvfile:
        while True:
            frame = [0] * 768
            try:
                mlx.getFrame(frame)
            except ValueError:
                continue
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(frame)
            time.sleep(10)


if __name__ == '__main__':
    main()
