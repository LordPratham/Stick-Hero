from ppadb import client
import time
from PIL import Image
import numpy
import random

adb = client.Client(host = '127.0.0.1', port = 5037)
devices = adb.devices()


if len(devices)  == 0:
    print("There Are No Devices")

    quit()

device = devices[0]


for i in range(4509,4513):

    device.shell('input keyevent KEYCODE_POWER')
    device.shell('input touchscreen swipe 100 720 100 200')
    device.shell(f'input text {i}')
    print(f'input text {i}')
    time.sleep(2)
    # time.sleep()

    image = device.screencap()
    with open("ss.png","wb") as f:
        f.write(image)
    image = Image.open('screen.png')
    image = numpy.array(image, dtype= numpy.uint8)
    pixels = [list(i[:3]) for i in image[1900]]
    print(pixels)
    pixel = pixels[100]
    r, g, b =[int(i) for i in pixel]
    print(r,g,b)
    if (r+g+b) == 399:
        device.shell("input keyevent KEYCODE_POWER")
