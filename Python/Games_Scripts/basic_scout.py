import time
import pyautogui

# Wait for the user to focus on the game window
input("Make sure the game window is active and press Enter to start...")

# Function to send army for scouting
def send_army_for_scouting():
    # Replace these coordinates with the specific location where you want to click
    scout_button_x, scout_button_y = 1168, 564
    
    # Move the mouse to the scout button and click
    pyautogui.moveTo(scout_button_x, scout_button_y, duration=0.5)
    pyautogui.click()
    pyautogui.click()
    
    #explore_x, explore_y = 1240,611
    pyautogui.moveTo(1240, 611, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(1368, 462, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(1145, 345, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(1145, 691, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(1410, 806, duration=0.5)
    pyautogui.click()
    
    time.sleep(2)
    
    pyautogui.press('esc')
    


while True:
    send_army_for_scouting()
    time.sleep(30)


