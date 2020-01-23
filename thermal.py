import colorsys
import io

import seeed_mlx90640
from PIL import Image


class Thermal:

    def __init__(self):
        self.mlx = seeed_mlx90640.grove_mxl90640()

    @staticmethod
    def mapValue(value, curMin, curMax, desMin, desMax):
        curDistance = value - curMax
        if curDistance == 0:
            return desMax
        curRange = curMax - curMin
        direction = 1 if curDistance > 0 else -1
        ratio = curRange / curDistance
        desRange = desMax - desMin
        value = desMax + (desRange / ratio)
        return value

    @staticmethod
    def constrain(value, down, up):
        value = up if value > up else value
        value = down if value < down else value
        return value

    @staticmethod
    def isDigital(value):
        try:
            if value == "nan":
                return False
            else:
                float(value)
            return True
        except ValueError:
            return False

    def process_data(self, hetData):
        maxHet = 0
        minHet = 500
        tempData = []
        nanCount = 0

        if len(hetData) < 768:
            return

        for i in range(0, 768):
            curCol = i % 32
            newValueForNanPoint = 0
            curData = None

            if i < len(hetData) and self.isDigital(hetData[i]):
                curData = float(hetData[i])
            else:
                interpolationPointCount = 0
                sumValue = 0
                # print("curCol",curCol,"i",i)

                abovePointIndex = i - 32
                if (abovePointIndex > 0):
                    if hetData[abovePointIndex] is not "nan":
                        interpolationPointCount += 1
                        sumValue += float(hetData[abovePointIndex])

                belowPointIndex = i + 32
                if (belowPointIndex < 768):
                    print(" ")
                    if hetData[belowPointIndex] is not "nan":
                        interpolationPointCount += 1
                        sumValue += float(hetData[belowPointIndex])

                leftPointIndex = i - 1
                if (curCol != 31):
                    if hetData[leftPointIndex] is not "nan":
                        interpolationPointCount += 1
                        sumValue += float(hetData[leftPointIndex])

                rightPointIndex = i + 1
                if (belowPointIndex < 768):
                    if (curCol != 0):
                        if hetData[rightPointIndex] is not "nan":
                            interpolationPointCount += 1
                            sumValue += float(hetData[rightPointIndex])

                curData = sumValue / interpolationPointCount
                # For debug :
                # print(abovePointIndex,belowPointIndex,leftPointIndex,rightPointIndex)
                # print("newValueForNanPoint",newValueForNanPoint," interpolationPointCount" , interpolationPointCount ,"sumValue",sumValue)
                nanCount += 1

            tempData.append(curData)
            maxHet = tempData[i] if tempData[i] > maxHet else maxHet
            minHet = tempData[i] if tempData[i] < minHet else minHet

        if maxHet == 0 or minHet == 500:
            return
        # For debug :
        # if nanCount > 0 :
        #     print("____@@@@@@@ nanCount " ,nanCount , " @@@@@@@____")

        return {
            "frame": tempData,
            "maxHet": maxHet,
            "minHet": minHet
        }

    def get_data(self):

        data = [0] * 768

        while True:
            try:
                self.mlx.getFrame(data)
            except ValueError:
                continue
            break

        # with open('thermal2.csv') as csvfile:
        #     data = list(csv.reader(csvfile))[0]  # 768 values

        # Make some RGB values.
        # # Cycle through hue vertically & saturation horizontally
        # colors = []
        # for i in data:
        #     # Convert color from HSV to RGB
        #     rgb = colorsys.hsv_to_rgb(float(i) / 360, 1, 1)
        #     rgb = [int(0.5 + 255 * u) for u in rgb]
        #     colors.extend(rgb)
        #
        # # Convert list to bytes
        # colors = bytes(colors)
        # img = Image.frombytes('RGB', (32, 24), colors)
        # img.show()
        # img.save('hues.png')

        frame = self.process_data(data)

        maxHet = frame["maxHet"]
        minHet = frame["minHet"]
        frame = frame["frame"]

        pixelSize = 15
        width = 480
        height = 360
        minHue = 180
        maxHue = 360

        # tempData = constrain(mapValue(frame[index], minHet, maxHet, minHue, maxHue), minHue, maxHue)

        colors = []
        for i in frame:
            # Convert color from HSV to RGB
            tempData = self.constrain(self.mapValue(i, minHet, maxHet, minHue, maxHue), minHue, maxHue)
            rgb = colorsys.hsv_to_rgb(tempData / 360, 1.0, 1.0)
            rgb = [int(0.5 + 255 * u) for u in rgb]
            colors.extend(rgb)

        # Convert list to bytes
        colors = bytes(colors)
        img = Image.frombytes('RGB', (32, 24), colors)
        img = img.rotate(90)
        img = img.resize((width, height))
        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format=img.format)
        imgByteArr = imgByteArr.getvalue()
        return imgByteArr
        # img.show()
        # img.save('hues2.png')
