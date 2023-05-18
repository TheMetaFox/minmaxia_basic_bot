import time
import pyautogui
import keyboard
import win32api, win32con


def print_pixel_information():
    pyautogui.displayMousePosition()

def click(location):
    win32api.SetCursorPos(location)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.01)

upgrade_rgb = (85,119,255)
prestige_rgb = (221,68,0)
location_dict = {"Location 1":(440,200),
                "Location 2":(440,265),
                "Location 3":(440,330),
                "Location 4":(440,395),
                "Location 5":(440,460),
                "Location 6":(440,525),
                "Location 7":(440,590),
                "Location 8":(440,655),
                "Location 9":(440,720),
                "Location 10":(440,785),
                "Location 11":(440,850),
                "Location 12":(440,915),
                "Location 13":(440,980),
                "Location 14":(440,1045),
                "Location 15":(440,1110)}

paused = True

print("To start program, press [s].")
keyboard.wait('s')
print("Starting program...")
while True:
    #pyautogui.click()

    # Upgrade Buildings   
     
    if paused == False:
        for location in location_dict:
            #print(f"Checking location {location}...")
            pixel_r = pyautogui.pixel(location_dict[location][0],location_dict[location][1])[0]
            if (pixel_r == upgrade_rgb[0]):
                #print(f"Upgrading location {location}...")
                click(location_dict[location])
                continue
            #print(f"The pixel red value {pixel_r} does not match {upgrade_rgb[0]}")
            if (pixel_r == prestige_rgb[0]):
                click(location_dict[location])
                continue
        win32api.SetCursorPos((200,500))


    if keyboard.is_pressed('p'):
        paused = paused == False
        time.sleep(1)

    if keyboard.is_pressed('d'):
        print_pixel_information()

    if keyboard.is_pressed('q'):
        print("Quiting program...")
        break