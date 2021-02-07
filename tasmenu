
import os
import sys
import tkinter
from tkinter import *


def start_recording():
    os.system('python fullInputRecorder2.py')


def start_replay():
    os.system('python fullInputReplay2.py')
    print('started replaying')


def name_file():
    label1.configure(text="Saved recording filename will be: "+session_file_name.get())
    global _name_of_file
    _name_of_file = session_file_name.get()
    print(_name_of_file)


_name_of_file = 'session1'

if __name__ == '__main__':
    panel = tkinter.Tk()
    panel.title('GeneralTAS')
    panel.geometry('400x200')

    _name_of_file = 'session1'

    session_file_name = Entry(panel, width=20)
    session_file_name.grid(column=0, row=0)

    label1 = Label(panel, text="Saved recording filename will be: session1")
    label1.grid(column=2, row=0)

    label2 = Label(panel, text="Press [esc] to finish and save recording")
    label2.grid(column=1, row=1)

    label3 = Label(panel, text="Replay recorded segments")
    label3.grid(column=1, row=2)

    button1 = Button(panel, text="Save name", command=name_file)
    button1.grid(column=1, row=0)

    button2 = Button(panel, text="Start Recording", command=start_recording)
    button2.grid(column=0, row=1)

    button3 = Button(panel, text="Start Replay", command=start_replay)
    button3.grid(column=0, row=2)

    check1 = Checkbutton(panel, text="test1", )
    check1.grid(column=0, row=3)

    panel.mainloop()
