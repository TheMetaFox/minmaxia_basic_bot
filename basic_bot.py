import time
import pyautogui
import keyboard


def print_pixel_information():
    pyautogui.displayMousePosition()

def click(location):
    x, y = location[0], location[1]
    pyautogui.moveTo(x, y)  # move mouse to XY coordinates over num_second seconds
    pyautogui.click(clicks=1)
    pyautogui.moveTo(200,500)

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
                "Location 12":(440,915)}

'''location_dict = {"Location 1":(440,200),
                "Location 2":(440,270),
                "Location 3":(440,340),
                "Location 4":(440,410),
                "Location 5":(440,480),
                "Location 6":(440,550),
                "Location 7":(440,620),
                "Location 8":(440,690),
                "Location 9":(440,760),
                "Location 10":(440,830),
                "Location 11":(440,900)}'''


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

    if keyboard.is_pressed('p'):
        paused = paused == False
        time.sleep(1)

    if keyboard.is_pressed('d'):
        print_pixel_information()

    if keyboard.is_pressed('q'):
        print("Quiting program...")
        break