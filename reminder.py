"""***####by defolt whiuot user was tuch, up withe th os
******###after a 2 break of 5m you can take a 15 m break
****** def install
####back to work*****"""
#!/usr/bin/python3
import os
if os.name == 'nt':
    os.system('cls')
#    src = 'reminder.exe'
#    dest = 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/reminder.exe'
    os.rename('reminder.exe', 'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/reminder.exe')
else:
    loction = os.getcwd()
    os.system('clear')
    os.system(f"sed  -i '1i {loction}/reminder.py &'  ~/.bashrc")
#    os.system(f"sed -i '19,20d' {loction}/reminder.py")
    try:
        import tkinter
    except ImportError as e:
        print('We install a library so the script can run easily ....\nWe need from you to input your password that we can install the missing without problem')
        def install_function():
            os.system("sudo bash -c 'sudo apt-get update && sudo apt install python3-tk -y >/dev/null 2>&1 & disown'")
        install_function()
from tkinter import *
import time
while True:
    local_time = 3
    local_time = local_time
    time.sleep(local_time)
    while True:
        mbox = Tk()
        mbox.title("Break Time")
        width_win = 800
        hidth_win = 300
        screen_wi = mbox.winfo_screenwidth()
        screen_hi = mbox.winfo_screenheight()
        x_cordinet = (screen_wi/2) - (width_win/2)
        y_cordinet = (screen_hi/2) - (hidth_win/2)
        mbox.geometry("%dx%d+%d+%d" % (width_win, hidth_win, x_cordinet, y_cordinet))
        def close_mbox_re():
            mbox.destroy()
            time.sleep(2)
            def close_smbox():
                smbox.destroy()
            smbox = Tk()
            smbox.title("Break Time")
            width_win = 800
            hidth_win = 300
            screen_wi = smbox.winfo_screenwidth()
            screen_hi = smbox.winfo_screenheight()
            x_cordinet = (screen_wi/2) - (width_win/2)
            y_cordinet = (screen_hi/2) - (hidth_win/2)
            smbox.geometry("%dx%d+%d+%d" % (width_win, hidth_win, x_cordinet, y_cordinet))
            canwiget = Canvas(smbox)
            canwiget.pack()
            thelabel = Label(smbox , text = 'You need to take a break of 5 minutes!' , font = 'verdana 25 bold', bd = 6, fg = 'red')
            canwiget.create_window(200, 100, window=thelabel)
        def close_mbox():
            mbox.destroy()
        canwiget = Canvas(mbox)
        canwiget.pack()
        thelabel = Label(mbox , text = 'You need to take a break of 5 minutes' , font = 'verdana 25 bold', bd = 6, fg = 'red')
        canwiget.create_window(200, 100, window=thelabel)
        btoon_mor5 = Button(mbox, text = ' more 5 minutes', command = close_mbox_re)
        btoon_ok = Button(mbox, text = 'O.K', command = close_mbox)
        canwiget.create_window(350, 250, window=btoon_mor5)
        canwiget.create_window(0, 250, window=btoon_ok)
        mbox.mainloop()
        break
