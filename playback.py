
import time
import os
import sys
import pyautogui
import ctypes


os.chdir(os.path.dirname(os.path.realpath(__file__)))
directory = 'mouse_recorder'
try:
    session_name = 'newkeyboardreplaytest7'
except:
    print('you must enter a name for the session\nfor example: python replay.py session_name')
    sys.exit()
dir_path = os.path.join(os.getcwd(), directory, session_name)

file_name = 'history.txt'
file_path = os.path.join(dir_path, file_name)
#print dir_path

# open the recording file
with open(file_path, 'r') as f:
    steps = f.readlines()

# clean steps
new_steps = []
for step in steps:
    new_step = []
    for i in step.split(','):
        new_step.append(i.strip('\n'))
    new_steps.append(new_step)


# start moving mouse cursor
t_last = float(new_steps[0][-1])

pyautogui.PAUSE = 0

for step in new_steps:

    if step[0] == 'moved':
        t_two = time.time()
        t_one = t_two
        delay = (float(step[-1]) - t_last)
        if delay > 1:
            delay = 0
        while t_two < (t_one + delay):
            t_two = time.time()
        else:
            print('moved')
            #pos_x = (65536 * int(step[1]) / ctypes.windll.user32.GetSystemMetrics(0) + 1)
            #pos_y = (65536 * int(step[2]) / ctypes.windll.user32.GetSystemMetrics(1) + 1)
            #ctypes.windll.user32.mouse_event((0x0001 + 0x8000), int(pos_x), int(pos_y), 0, 0)
            ctypes.windll.user32.SetCursorPos(int(step[1]), int(step[2]))
            #pyautogui.moveTo(int(step[1]), int(step[2]))
            t_last = float(step[-1])

    if step[0] == 'kbPressed':
        t_two = time.time()
        t_one = t_two
        delay = (float(step[-1]) - t_last)
        if delay > 1:
            delay = 0
        while t_two < (t_one + delay):
            t_two = time.time()
        else:
            holder = ctypes.windll.User32.VkKeyScanW(ord(step[1]))
            used_code = int(hex(holder), 16)
            scan_code = ctypes.windll.User32.MapVirtualKeyW(used_code, 0)
            ctypes.windll.user32.keybd_event(used_code, scan_code, 0, 0)
            #pyautogui.keyDown(step[1])
            t_last = float(step[-1])

    if step[0] == 'kbReleased':
        t_two = time.time()
        t_one = t_two
        delay = (float(step[-1]) - t_last)
        if delay > 1:
            delay = 0
        while t_two < (t_one + delay):
            t_two = time.time()
        else:
            holder = ctypes.windll.User32.VkKeyScanW(ord(step[1]))
            used_code = int(hex(holder), 16)
            scan_code = ctypes.windll.User32.MapVirtualKeyW(used_code, 0)
            ctypes.windll.user32.keybd_event(used_code, scan_code, 0x0002, 0)
            #pyautogui.keyUp(step[1])
            t_last = float(step[-1])

    if step[0] == 'left_down':
        t_two = time.time()
        t_one = t_two
        delay = (float(step[-1]) - t_last)
        if delay > 1:
            delay = 0
        while t_two < (t_one + delay):
            t_two = time.time()
        else:
            pyautogui.moveTo(int(step[1]), int(step[2]))
            pyautogui.mouseDown(button='left')
            t_last = float(step[-1])

    if step[0] == 'left_up':
        t_two = time.time()
        t_one = t_two
        delay = (float(step[-1]) - t_last)
        if delay > 1:
            delay = 0
        while t_two < (t_one + delay):
            t_two = time.time()
        else:
            pyautogui.moveTo(int(step[1]), int(step[2]))
            pyautogui.mouseUp(button='left')
            t_last = float(step[-1])

    if step[0] == 'right_down':
        t_two = time.time()
        t_one = t_two
        delay = (float(step[-1]) - t_last)
        if delay > 1:
            delay = 0
        while t_two < (t_one + delay):
            t_two = time.time()
        else:
            pyautogui.moveTo(int(step[1]), int(step[2]))
            pyautogui.mouseDown(button='right')
            t_last = float(step[-1])

    if step[0] == 'right_up':
        t_two = time.time()
        t_one = t_two
        delay = (float(step[-1]) - t_last)
        if delay > 1:
            delay = 0
        while t_two < (t_one + delay):
            t_two = time.time()
        else:
            pyautogui.moveTo(int(step[1]), int(step[2]))
            pyautogui.mouseUp(button='right')
            t_last = float(step[-1])

    if step[0] == 'done':
        print('End autorun')
        sys.exit()
