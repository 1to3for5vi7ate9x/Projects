import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import time
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)  # A short delay to simulate a real click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def mouse_drag(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.dragTo(x,y)

def activate_window(title):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        vm_window = windows[0]
        vm_window.activate()
        return vm_window
    else:
        print("VM window not found.")
        return None

def capture_screenshot(vm_window):
    if vm_window is not None:
        vm_screenshot = pyautogui.screenshot(region=(vm_window.left, vm_window.top, vm_window.width, vm_window.height))
        vm_screenshot.save('vm_screenshot.png')
        return vm_screenshot
    else:
        return None


def find_and_click_template(screenshot, template_image, vm_window, threshold=0.6):
    template_gray = cv2.cvtColor(template_image, cv2.COLOR_BGR2GRAY)
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(max_val)

    if max_val >= threshold:
        # Calculate the center of the matched region
        center_x = max_loc[0] + int(template_image.shape[1]/2)
        center_y = max_loc[1] + int(template_image.shape[0]/2)
        # Adjust for the VM window's position on the screen
        global_x = vm_window.left + center_x
        global_y = vm_window.top + center_y
        click(global_x, global_y)
        print(f"Clicked at ({global_x}, {global_y}) on the screen")
    else:
        print("Template not found.")

def find_and_click_origems(screenshot, origem_image, vm_window, threshold=0.6):
    origem_gray = cv2.cvtColor(origem_image, cv2.COLOR_BGR2GRAY)
    screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, origem_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(max_val)

    if max_val >= threshold:
        # Calculate the center of the matched region
        center_x = max_loc[0] + int(origem_image.shape[1]/2)
        center_y = max_loc[1] + int(origem_image.shape[0]/2)
        # Adjust for the VM window's position on the screen
        global_x = vm_window.left + center_x
        global_y = vm_window.top + center_y
        click(global_x, global_y)
        print(f"Clicked at ({global_x}, {global_y}) on the screen")
    else:
        print("Origem not found.")

def process_vm_window(vm_window_title, template_image, origem_image):
    vm_window = activate_window(vm_window_title)
    if vm_window is None:
        print(f"VM window with title '{vm_window_title}' not found.")
        return

    screenshot = capture_screenshot(vm_window)
    if screenshot is not None:
        find_and_click_template(screenshot, template_image, vm_window)
        find_and_click_origems(screenshot, origem_image, vm_window)
        
        
def main():
    vm_window_titles = ["Wolf Ghost"] 
    #vm_window_titles = ["1","2","3","4","5","6","7","8","9"] # Replace with your actual VM window titles
    world_image = cv2.imread('world.png')  # Ensure this file exists in your script's directory
    origem_image = cv2.imread('origem.png')

    for vm_window_title in vm_window_titles:
        process_vm_window(vm_window_title, world_image,origem_image)

if __name__ == "__main__":
    main()
