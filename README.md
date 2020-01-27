# Converting Images to Video

```shell script
ffmpeg -r 5 -i images-person/img%04d.png -vcodec libx264 -pix_fmt yuv420p -y movie.mp4
```

# Sources

* http://wiki.seeedstudio.com/Grove-Thermal-Imaging-Camera-IR-Array/
* https://www.seeedstudio.com/Grove-Thermal-Imaging-Camera-IR-Array-MLX90640-110-degree-p-4334.html
* https://github.com/miguelgrinberg/flask-video-streaming
* https://blog.miguelgrinberg.com/post/video-streaming-with-flask