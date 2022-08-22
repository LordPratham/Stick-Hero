from time import time
import webbrowser
import os
import time

url=["https://www.youtube.com/watch?v=pH5uKjcP5GE", "https://www.youtube.com/watch?v=N1Tii31kAFI"]

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

for i in range(len(url)):
    webbrowser.get(chrome_path).open(url[i])
    time.sleep(20)
    os.system("killall -9 'Google Chrome'")