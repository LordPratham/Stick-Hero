from ppadb import client

adb = client.Client(host = '127.0.0.1', port = 5037)

devices = adb.devices()

if len(devices)  == 0:
    print("There Are No Devices")

    quit()

# phn = input("Enter Phone Number :  ")

device = devices[0]

# device.shell(f"input keyevent 26")
# device.shell(f"input swipe 100 1000 100 500")
# device.shell(f"input keyevent 3")
# device.shell(f"am start -a android.settings.SETTINGS'")
# device.shell(f"input swipe 100 1000 100 500")
# device.shell(f"input swipe 100 1000 100 500")
# device.shell(f"input tap 500 1080")
device.shell(f"input tap 500 1080")
# device.shell(f"input tap 900 100")
# device.shell(f"input text 'open%ssettings'")

print("hi")
# for i in phn:
#     device.shell(f"input keyevent {int(i)+7}")
# device.shell(f"input keyevent 5")


