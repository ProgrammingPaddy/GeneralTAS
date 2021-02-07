
import time
import os
import sys
from functools import partial
import pyWinhook
import pythoncom


def left_down(event, file_path):
    x, y = event.Position
    print(','.join(['left_down', str(x), str(y)]))
    with open(file_path, 'a') as f:
        f.write(','.join(['left_down', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


def left_up(event, file_path):
    x, y = event.Position
    print(",".join(['left_up', str(x), str(y)]))
    with open(file_path, 'a') as f:
        f.write(",".join(['left_up', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


def right_down(event, file_path):
    x, y = event.Position
    print(','.join(['right_down', str(x), str(y)]))
    with open(file_path, 'a') as f:
        f.write(",".join(['right_down', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


def right_up(event, file_path):
    x, y = event.Position
    print(','.join(['right_up', str(x), str(y)]))
    with open(file_path, 'a') as f:
        f.write(",".join(['right_up', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


def moved(event, file_path):
    x, y = event.Position
    print(','.join(['moved', str(x), str(y)]))
    with open(file_path, 'a') as f:
        f.write(",".join(['moved', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


def key_down(event, file_path, dir_path):
    global saved_recording
    if event.Ascii == 27:  # Ascii('ESC')=27
        print('End of recording')
        with open(file_path, 'w') as f:
            f.writelines(saved_recording)
            f.write('done')
        sys.exit()
    elif event.Ascii == 97:
        print('re-recording segment')
        with open(file_path, 'w') as f:
            f.write(",".join(['newSegment', str(time.time())]))
            f.write('\n')
    elif event.Ascii == 98:
        print('segment saved')
        with open(file_path, 'a') as f:
            f.write(",".join(['segment_end', str(time.time())]))
            f.write('\n')
        with open(file_path, 'r') as f:
            saved_recording = (saved_recording + (f.readlines()))
        with open(file_path, 'w') as f:
            f.write('')
    else:
        keyPressed = event.Ascii
        print(','.join(['kbPressed', chr(keyPressed)]))
        with open(file_path, 'a') as f:
            f.write(",".join(['kbPressed', chr(keyPressed), str(time.time())]))
            f.write('\n')
    return True


def key_up(event, file_path, dir_path):
    keyReleased = event.Ascii
    print(','.join(['kbReleased', chr(keyReleased)]))
    with open(file_path, 'a') as f:
        f.write(",".join(['kbReleased', chr(keyReleased), str(time.time())]))
        f.write('\n')
    return True


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    directory = 'mouse_recorder'
    try:
        session_name = 'newkeyboardreplaytest3'
    except:
        print('you must enter a name for the session\nfor example: python record.py session_name')
        sys.exit()
    dir_path = os.path.join(os.getcwd(), directory, session_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    saved_recording = []
    file_name = 'history.txt'
    file_path = os.path.join(dir_path, file_name)
    print(dir_path)

    ld = partial(left_down, file_path=file_path)
    lu = partial(left_up, file_path=file_path)
    rd = partial(right_down, file_path=file_path)
    ru = partial(right_up, file_path=file_path)
    mv = partial(moved, file_path=file_path)

    hm = pyWinhook.HookManager()
    hm.SubscribeMouseLeftDown(ld)
    hm.SubscribeMouseLeftUp(lu)
    hm.SubscribeMouseRightDown(rd)
    hm.SubscribeMouseRightUp(ru)
    hm.SubscribeMouseMove(mv)
    hm.HookMouse()

    pressedKey = partial(key_down, file_path=file_path, dir_path=dir_path)
    releasedKey = partial(key_up, file_path=file_path, dir_path=dir_path)

    hm.KeyDown = pressedKey
    hm.KeyUp = releasedKey
    hm.HookKeyboard()

    pythoncom.PumpMessages()

    hm.UnhookMouse()
    hm.UnHookKeyboard()
