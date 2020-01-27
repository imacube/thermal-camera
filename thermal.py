import io

import seeed_mlx90640

from thermal_data import ThermalData


class Thermal:

    def __init__(self):
        self.mlx = seeed_mlx90640.grove_mxl90640()
        self.mlx.refresh_rate = seeed_mlx90640.RefreshRate.REFRESH_2_HZ

        self.thermal_data = ThermalData()

    def get_serial_data(self):

        data = [0] * 768

        while True:
            try:
                self.mlx.getFrame(data)
            except ValueError:
                continue
            break

        img = self.thermal_data(data)
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format='PNG')
        imgByteArr = imgByteArr.getvalue()

        return imgByteArr
