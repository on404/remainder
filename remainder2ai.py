#!/usr/bin/python3
import os
import platform
import time

def break_time_notification():
    """Display break time notification and wait for user interaction."""
    try:
        import tkinter
    except ImportError:
        print("Tkinter is not installed. Please install it manually to use this script.")
        return

    root = tkinter.Tk()
    root.title("Break Time")
    width = 800
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

    label = tkinter.Label(root, text='You need to take a 5-minute break!', font='verdana 25 bold', bd=6, fg='red')
    label.pack()

    def close_window():
        root.destroy()

    def extend_break():
        root.destroy()
        time.sleep(300)  # Extend break by 5 minutes

    button_more = tkinter.Button(root, text='More 5 minutes', command=extend_break)
    button_ok = tkinter.Button(root, text='OK', command=close_window)
    button_more.pack(side='left')
    button_ok.pack(side='right')

    root.mainloop()

def main():
    while True:
        # Break every 2 hours
        time.sleep(7200)
        break_time_notification()

        # Take a 15-minute break every 2 hours
        time.sleep(900)

if __name__ == "__main__":
    main()