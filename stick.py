from ppadb.client import Client as AdbClient
from PIL import Image
import numpy
import time

adb = AdbClient(host = '127.0.0.1', port = 5037)

devices = adb.devices()

if len(devices)  == 0:
    print("There Are No Devices")

    quit()


device = devices[0]
j = 0
while j < 101:
    j+=1
    time.sleep(2.5)
    image = device.screencap()
    with open('screen.png', 'wb') as f:
        f.write(image)

    image = Image.open('screen.png')
    image = numpy.array(image, dtype= numpy.uint8)

    pixels = [list(i[:3]) for i in image[1800]]

    transitions = []

    ignore = True
    black = True

    for i, pixel in enumerate(pixels):
        r, g, b = [int(i) for i in pixel]

        if ignore and (r+g+b) !=0:
            continue

        ignore = False

        if black and (r+g+b) != 0:
            black = not black
            transitions.append(i)
            continue

        if not black and (r+g+b) == 0:
            black = not black
            transitions.append(i)
            continue

    print(transitions)

    start, target1 , target2 = transitions

    gap = target1 - start
    target = target2 - target1
    distance = round((gap+1 + (target+1)/2)*1.04, 3)
    print(distance)

    device.shell(f"input touchscreen swipe 500 500 500 500 {int(distance)}")

