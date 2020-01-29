"""Time lapse photography with the thermal camera."""

import csv
import time

import seeed_mlx90640


def main():
    limit = 0
    start = time.time()
    mlx = seeed_mlx90640.grove_mxl90640()
    mlx.refresh_rate = seeed_mlx90640.RefreshRate.REFRESH_4_HZ  # The fastest for Raspberry Pi Zero W
    with open('thermal.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        while limit < 300:
            try:
                frame = [0] * 768
                mlx.getFrame(frame)
                csvwriter.writerow(frame)
                #limit += 1
            except ValueError:
                continue
            #time.sleep(10)

    print(time.time() - start)

if __name__ == '__main__':
    main()
