import time
import cv2
import numpy as np
import pyautogui
from PIL import Image

# Load the target image (image of the button you want to click)
target_image = cv2.imread('target.png')

# Function to send army for scouting using image detection
def send_army_for_scouting():
    # Take a screenshot of the game window
    screenshot = pyautogui.screenshot()
    #screenshot.save("captured.png")
    # Convert the screenshot to a NumPy array
    screenshot_np = np.array(screenshot)

    # Convert BGR image to RGB
    screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

    # Match the target image using template matching
    result = cv2.matchTemplate(screenshot_rgb, target_image, cv2.TM_CCOEFF_NORMED)
    cv2.imshow('Result',result)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)



    # Get the coordinates of the best match
    print(max_loc, max_val)
    target_x, target_y = max_loc

    # Click on the best match
    pyautogui.click(1163,571)
    pyautogui.click(target_x, target_y, duration=0.5)

    # Wait for the scouting action to complete (adjust the duration based on the game's response time)
    time.sleep(2)

    # Example: Press 'Esc' key to exit scouting mode (adjust key as per your game's controls)
    pyautogui.press('esc')
    # You might need to add additional actions here to handle the scouting process based on your game's mechanics

# Infinite loop to automate scouting using image detection every 30 seconds
#while True:
send_army_for_scouting()
    #time.sleep(30)  # Wait for 30 seconds before the next scouting mission
