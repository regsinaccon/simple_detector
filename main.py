from pynput import keyboard
import time
import start
import controlkey
import speedtest
#import is_usb_in



operating_system=start.get_system()
#now_drives=start.find_drive(start.get_system())
if operating_system=="Windows":
    print("THIS TOOL MUST BE RUN AS ADMIN")
    print("START DETECTING")
else :
    print("IT MAY NOT RUN PROPERLY ON YOU PC ")


if operating_system=="Windows":
    while True:
        if speedtest.typing_speed():
            controlkey.disable_keyboard()
            print("The keyboard was diabled for 10 second")
            print("check if there is malicious device on your pc")
            for i in range(11):
                print(f'keyboard back in {10-i} sec')
                time.sleep(1.0)
            print("The keyboard is back")
            controlkey.enable_keyboard()
            break
controlkey.enable_keyboard()

            

        

