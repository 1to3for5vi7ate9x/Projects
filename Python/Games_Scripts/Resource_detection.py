import cv2 
import numpy as np
import pyautogui
import time
import random

def ss():
    time.sleep(1)
    screenshot = pyautogui.screenshot()
    screenshot.save('changed_city.png')
    
#def mousedrag():
        #original_position = pyautogui.position()    
        #pyautogui.moveTo(original_position[0] - 162, original_position[1]-400, duration =0.5)
        #pyautogui.dragTo(original_position[0]+30 , original_position[1]+30, duration=0.5, button = 'left') 
        #time.sleep(1)

def mousedrag():
    original_position = pyautogui.position()

    # Randomize movement direction and distance
    move_x = random.randint(-200, 200)  # Random movement in X direction
    move_y = random.randint(-200, 200)  # Random movement in Y direction

    # Move to the start position for dragging
    pyautogui.moveTo(original_position[0] + move_x, original_position[1] + move_y, duration=0.5)

    # Randomize end position for dragging
    end_x = random.randint(-200, 200)  # Random end position in X direction
    end_y = random.randint(-200, 200)  # Random end position in Y direction

    # Perform the drag to a new random location
    pyautogui.dragTo(original_position[0] + end_x, original_position[1] + end_y, duration=0.5, button='left')

    time.sleep(1)

def move_worldmap():
    screenshot = pyautogui.screenshot()
    screenshot.save('city.png')   
    city_img = cv2.imread('city.png', cv2.IMREAD_UNCHANGED)
    target_img = cv2.imread('city_world.png', cv2.IMREAD_UNCHANGED)

    result = cv2.matchTemplate(city_img, target_img, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    

    threshold = .55
    y_loc, x_loc = np.where(result >= threshold)
    
#--------------From Inside the city ----------------#

    if len(x_loc) == 0:
        target_img = cv2.imread('world.png', cv2.IMREAD_UNCHANGED)
        result = cv2.matchTemplate(city_img, target_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        threshold = .55
        y_loc, x_loc = np.where(result >= threshold)
        button_x = max_loc[0]//2 + 5
        button_y = max_loc[1]//2 + 5
        pyautogui.moveTo(button_x, button_y, duration=0.5)
        pyautogui.click()
        pyautogui.click()
move_worldmap() 
     
def megafruit():
    mousedrag()
    ss()
    changed_city = cv2.imread('changed_city.png', cv2.IMREAD_UNCHANGED)
    megafruit_img = cv2.imread('Megafruit.png', cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(changed_city, megafruit_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_loc, max_val)
    threshold = .60
    y_loc, x_loc = np.where(result >= threshold)
    if len(x_loc) == 0:
        return 0, None
    else:
        w, h = megafruit_img.shape[1], megafruit_img.shape[0]
        print(w,h)
        x,y=int(max_loc[0] + w // 2), int(max_loc[1] + h // 2) #Midpoints of the match
        print(x,y)
    
        return 1, (x,y)

def cohengen():
    mousedrag()
    ss()
    changed_city = cv2.imread('changed_city.png', cv2.IMREAD_UNCHANGED)
    cohengen_img = cv2.imread('Cohengen.png', cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(changed_city, cohengen_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_loc, max_val)
    threshold = .60
    y_loc, x_loc = np.where(result >= threshold)
    if len(x_loc) == 0:
        return 0, None
    else:
        w, h = cohengen_img.shape[1], cohengen_img.shape[0]
        print(w,h)
        x,y=int(max_loc[0] + w // 2), int(max_loc[1] + h // 2) # Midpoints of the match
        print(x,y)
        return 1, (x,y)

def pyrostone():
    mousedrag()
    ss()
    changed_city = cv2.imread('changed_city.png', cv2.IMREAD_UNCHANGED)
    pyrostone_img = cv2.imread('Pyrostone.png', cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(changed_city, pyrostone_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_loc, max_val)
    threshold = .60
    y_loc, x_loc = np.where(result >= threshold)
    if len(x_loc) == 0:
        return 0, None
    else:
        w, h = pyrostone_img.shape[1], pyrostone_img.shape[0]
        print(w,h)
        x,y=int(max_loc[0] + w // 2), int(max_loc[1] + h // 2) #Midpoints of the match
        print(x,y)
        return 1, (x,y)

def ather():
    mousedrag()
    ss()
    changed_city = cv2.imread('changed_city.png', cv2.IMREAD_UNCHANGED)
    ather_img = cv2.imread('Ather.png', cv2.IMREAD_UNCHANGED)
    result = cv2.matchTemplate(changed_city, ather_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_loc, max_val)
    threshold = .60
    y_loc, x_loc = np.where(result >= threshold)
    if len(x_loc) == 0:
        return 0, None
    else:
        w, h = ather_img.shape[1], ather_img.shape[0]
        print(w,h)
        x,y=int(max_loc[0] + w // 2), int(max_loc[1] + h // 2)
        print(x,y)
        return 1, (x,y)

def search_megafruit():
    scaling_factor = 2
    for i in range(4):
        match, midpoint = megafruit()
        if match == 0:
            print("No match")
        else:
            button_x = int(midpoint[0] / scaling_factor)
            button_y = int(midpoint[1] / scaling_factor)
            print(button_x, button_y)
            pyautogui.moveTo(button_x+12, button_y+18, duration=0.5)
            pyautogui.click()
            pyautogui.click()
            break

def search_cohengen():
    scaling_factor = 2
    for i in range(4):
        match, midpoint = cohengen()
        if match == 0:
            print("No match")
        else:
            button_x = int(midpoint[0] / scaling_factor)
            button_y = int(midpoint[1] / scaling_factor)
            print(button_x, button_y)
            pyautogui.moveTo(button_x+12, button_y+18, duration=0.5)
            pyautogui.click()
            pyautogui.click()
            break

def search_pyrostone():
    scaling_factor = 2
    for i in range(4):
        match, midpoint = pyrostone()
        if match == 0:
            print("No match")
        else:
            button_x = int(midpoint[0] / scaling_factor)
            button_y = int(midpoint[1] / scaling_factor)
            print(button_x, button_y)
            pyautogui.moveTo(button_x+12, button_y+18, duration=0.5)
            pyautogui.click()
            pyautogui.click()
            break

def search_ather():
    scaling_factor = 2
    for i in range(4):
        match, midpoint = ather()
        if match == 0:
            print("No match")
        else:
            button_x = int(midpoint[0] / scaling_factor)
            button_y = int(midpoint[1] / scaling_factor)
            print(button_x, button_y)
            pyautogui.moveTo(button_x+12, button_y+18, duration=0.5)
            pyautogui.click()
            pyautogui.click()
            break
#search_ather()

#search_megafruit()

search_cohengen()












#search_megafruit()

# def cohengen():
#     mousedrag()
#     ss()
#     changed_city = cv2.imread('changed_city.png', cv2.IMREAD_UNCHANGED)
#     cohen_img = cv2.imread('Cohengen.png', cv2.IMREAD_UNCHANGED)
#     result = cv2.matchTemplate(changed_city, cohen_img, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     print(max_loc,max_val)
#     threshold = .48
#     y_loc, x_loc = np.where(result >= threshold)
#     x1 = len(x_loc)
#     w = cohen_img.shape[1]
#     h = cohen_img.shape[0]
#     for(x,y) in zip(x_loc, y_loc):
#         cv2.rectangle(changed_city, (x,y),(x+w,y+h),(0,255,255),2)
#     return x1,max_loc
#     #cv2.imshow('City',changed_city)
#     #cv2.waitKey()
#     #cv2.destroyAllWindows()

# def search_cohengen():
#     for i in range(4):
#         match,location = cohengen()
#         if match == 0:
#             print("No match")
#         else:
#             button_x = location[0]//2 + 6
#             button_y = location[1]//2 + 10
#             print(button_x,button_y)
#             pyautogui.moveTo(button_x, button_y, duration=0.5)
#             pyautogui.click()
#             break



# def megafruit():
#     mousedrag()
#     ss()
#     changed_city = cv2.imread('changed_city.png', cv2.IMREAD_UNCHANGED)
#     megafruit_img = cv2.imread('Megafruit.png', cv2.IMREAD_UNCHANGED)
#     result = cv2.matchTemplate(changed_city, megafruit_img, cv2.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#     print(max_loc,max_val)
#     threshold = .60
#     y_loc, x_loc = np.where(result >= threshold)
#     x1 = len(x_loc)
#     w = megafruit_img.shape[1]
#     h = megafruit_img.shape[0]
#     for(x,y) in zip(x_loc, y_loc):
#         cv2.rectangle(changed_city, (x,y),(x+w,y+h),(0,255,255),2)
#     return x1,max_loc

# def search_megafruit():
#     for i in range(4):
#         match,location = megafruit()
#         if match == 0:
#             print("No match")
#         else:
#             button_x = location[0]//2 + 6
#             button_y = location[1]//2 + 10
#             print(button_x,button_y)
#             pyautogui.moveTo(button_x, button_y, duration=0.5)
#             pyautogui.click()
#             break

# search_megafruit()   
         
#for i in range(4):
#     mousedrag()
#     ss()
#     cohengen()

          
#Display the matched result
#cv2.imshow('City',city_img)
#cv2.waitKey()
#cv2.destroyAllWindows()
