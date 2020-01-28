"""Time lapse photography with the thermal camera."""

import csv
import time

import seeed_mlx90640


def main():
    mlx = seeed_mlx90640.grove_mxl90640()
    mlx.refresh_rate = seeed_mlx90640.RefreshRate.REFRESH_2_HZ  # The fastest for Raspberry Pi Zero W
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
