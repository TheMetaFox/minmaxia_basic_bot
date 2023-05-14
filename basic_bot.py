import pyautogui
import keyboard


def print_pixel_information():
    pyautogui.displayMousePosition()

def click(location):
    x, y = location[0], location[1]
    pyautogui.moveTo(x, y)  # move mouse to XY coordinates over num_second seconds
    pyautogui.click()
    pyautogui.moveTo(200,500)

upgrade_rgb = (85,119,255)
prestige_rgb = (221,68,0)
location_dict = {"Location 1":(390,200),
                "Location 2":(390,270),
                "Location 3":(390,340),
                "Location 4":(390,410),
                "Location 5":(390,480),
                "Location 6":(390,550),
                "Location 7":(390,620),
                "Location 8":(390,690),
                "Location 9":(390,760),
                "Location 10":(390,830),
                "Location 11":(390,900)}

print("To start program, press [s].")
keyboard.wait('s')
print("Starting program...")
while True:
    #pyautogui.click()

    # Upgrade Buildings    
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

    if (keyboard.is_pressed('d')):
        print_pixel_information()

    if (keyboard.is_pressed('q')):
        print("Quiting program...")
        break
    
