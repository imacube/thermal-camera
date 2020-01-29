This repo draws heavily on the code provided by Seeed Studio and utilizes their MLX90640 110 degree Thermal Camera.

The frame rate setting for the camera in this code was chosen based on initial experiences with a Raspberry Pi Zero W.

The camera uses a 32x24 array but the data feed is all one line.

# Setup
## Wiring

The Seeed Studio Grove Thermal Imaging Camera IR Array uses 3 to 6V. I connected mine to the 3.3V DC
on my Raspberry Pi Zero W. Current consumption of approximately 18mA.

Match the *SDA* and *SCL* pins on the camera to those on the Pi. 

- Camera SDA -> GPIO 2 (SDA)
- Camera SCL -> GPIO 3 (SCL)

## Software

1. Install `grove.py`.
    ```shell script
    curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -
    ```
1. Install the driver. 
    ```shell script
    pip3 install seeed-python-mlx90640
   ```
   If you need to run with sudo.
   ```shell script
    sudo pip3 install seeed-python-mlx90640
    ```
1. Check for i2c number. This should return a device.
    ```shell script
    ls /dev/i2c*
    ```
1. Check for the camera as an i2c device. Its address is `0x33`.
    ```shell script
    i2cdetect -y -r 1
    ```
1. Give it a try! :D

### Refresh Rate

I found that `REFRESH_2_HZ` worked on a Raspberry Pi Zero W with `stream.py`. Higher ones might work, especially for
`time-lapse.py`.

This code is an example of how to create the device and set the refresh rate. This was found 
on [Seed Studio Wiki for their Thermal Imaging Camera](http://wiki.seeedstudio.com/Grove-Thermal-Imaging-Camera-IR-Array/). 

```python
import seeed_mlx90640
mlx = seeed_mlx90640.grove_mxl90640()
mlx.refresh_rate = seeed_mlx90640.RefreshRate.REFRESH_8_HZ  # The fastest for raspberry 4 
# REFRESH_0_5_HZ = 0b000  # 0.5Hz
# REFRESH_1_HZ = 0b001  # 1Hz
# REFRESH_2_HZ = 0b010  # 2Hz
# REFRESH_4_HZ = 0b011  # 4Hz
# REFRESH_8_HZ = 0b100  # 8Hz
# REFRESH_16_HZ = 0b101  # 16Hz
# REFRESH_32_HZ = 0b110  # 32Hz
# REFRESH_64_HZ = 0b111  # 64Hz
```

# Streaming

Run the `stream.py` script to host a small website with Flask that streams what the thermal camera sees.

# Thermal Image Capturing

Run `time-lapse.py` or write a simple script to call `thermal.py` to capture the thermal data.

# Time Lapse Images

Run `time-lapse.py`. Data is written to `thermal.csv`. Images are captured as raw numeric data from the camera 
every 10 seconds and stored in the CSV file. Use `thermal-to-images.py` to convert the raw data into PNG images.

The data is formatted as one line per image.

## Converting Images to Video

I found that I needed an image that is `images/img0000.png` for this to work. I don't know if everything has to

```shell script
ffmpeg -r 5 -i images/img%04d.png -vcodec libx264 -pix_fmt yuv420p -y movie.mp4
```

# Sources

* [Seeed Studio Thermal Camera Wiki](http://wiki.seeedstudio.com/Grove-Thermal-Imaging-Camera-IR-Array/)
* [Seeed Studio Thermal Camera Product Page](https://www.seeedstudio.com/Grove-Thermal-Imaging-Camera-IR-Array-MLX90640-110-degree-p-4334.html)
* [Video Streaming with Flask Source Code](https://github.com/miguelgrinberg/flask-video-streaming)
* [Video Streaming with Flask](https://blog.miguelgrinberg.com/post/video-streaming-with-flask)
  * `Video Streaming with Flask.pdf`
* [Flask Video Streaming Revisited](https://blog.miguelgrinberg.com/post/flask-video-streaming-revisited) 
  * `Flask Video Streaming Revisited.pdf`