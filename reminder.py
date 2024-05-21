from tkinter import *
import time

#window size 
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 300

def create_window(parent=None):
    window = Toplevel(parent) if parent else Tk()
    window.title("Break Time")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width - WINDOW_WIDTH) // 2
    y_coordinate = (screen_height - WINDOW_HEIGHT) // 2
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_coordinate}+{y_coordinate}")
    return window

def create_label(parent, text):
    can_wiget = Canvas(parent)
    can_wiget = can_wiget.pack()
    label = Label(parent, text=text, font='verdana 25 bold', bd=6, fg='red').place(relx=0.5, rely=0.5, anchor=CENTER)
    return label

def close_window(window):
    window.destroy()
    return 0

def call_sbox(window):
    window.destroy()
    time.sleep(5)  # Pause for 5 seconds
    sbox = create_window()
    create_label(sbox, 'You need to take a break of 5 minutes!')
    button_ok = Button(sbox, text='O.K', command=lambda: close_window(sbox))
    button_ok.pack()

while True:
    mbox = create_window()
    create_label(mbox, 'You need to take a break of 5 minutes')
    button_mor5 = Button(mbox, text='more 5 minutes', command=lambda: call_sbox(mbox))
    button_mor5.pack(side=LEFT)
    button_ok = Button(mbox, text='O.K', command=lambda: close_window(mbox))
    button_ok.pack(side=RIGHT)
    mbox.mainloop()
