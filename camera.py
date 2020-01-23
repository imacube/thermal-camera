import time

from base_camera import BaseCamera


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""
    imgs = [open(x, 'rb').read() for x in ['hues.png', 'hues2.png']]

    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            yield Camera.imgs[int(time.time()) % 2]
