from tkinter import *
#I use after func that calc the time in ms...
#on my system the app use around 90 mb
#I dont use the destroy func because it kill the app 
class BreakTimeApp:
    def __init__(self):
        # Create the main window and set it up
        self.root = self.create_window()
        self.create_root_window()
        # Create a secondary window for additional options
        self.sbox = self.create_window()
        # Hide the secondary window initially
        self.sbox.withdraw()
        # Schedule the 'run' method to be executed after 2 hour
        self.root.after(7_200_000, self.run) 

    def create_window(self):
        # Create a new window
        window = Tk()
        # Hide window borders and title bar
        window.overrideredirect(1)
        # Get screen dimensions
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        # Calculate coordinates to center the window
        x_coordinate = (screen_width - 800) // 2
        y_coordinate = (screen_height - 300) // 2
        # Set window size and position
        window.geometry(f"800x300+{x_coordinate}+{y_coordinate}")
        return window

    def create_root_window(self):
        # Create label widget with the message
        self.label = Label(self.root, text='You need to take a break of 5 minutes', font='verdana 25 bold', bd=6, fg='red')
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Create button widget to request additional 5 minutes
        self.button_mor5 = Button(self.root, text='more 5 minutes', command=self.call_sbox)
        self.button_mor5.place(relx=0.15, rely=0.8, anchor=S)

        # Create button widget to acknowledge break
        self.button_ok_root = Button(self.root, text='O.K', command=self.close_main_window)
        self.button_ok_root.place(relx=0.9, rely=0.8, anchor=S)

    def call_sbox(self):
        # Hide the main window
        self.root.withdraw()
        # Schedule the 'show_sbox' method to be executed after 5 minutes
        self.root.after(300_000, self.show_sbox)

    def show_sbox(self):
        # Create label widget with break message in the secondary window
        self.sbox_label = Label(self.sbox, text='You need to take a break of 5 minutes!', font='verdana 25 bold', bd=6, fg='red')
        self.sbox_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        # Create button widget to acknowledge break in the secondary window
        self.button_ok_sbox = Button(self.sbox, text='O.K', command=self.close_sbox)
        self.button_ok_sbox.place(relx=0.5, rely=0.8, anchor=CENTER)
        # Make the secondary window visible
        self.sbox.deiconify()

    def close_sbox(self):
        # Hide the secondary window
        self.sbox.withdraw()
        # Schedule the main window to be displayed after 5 minutes
        self.root.after(300_000, self.root.deiconify) 

    def close_main_window(self):
        # Hide the main window
        self.root.withdraw()
        # Schedule the main window to be displayed after 2 hour and 5 minutes
        self.root.after(7_500_000, self.root.deiconify)

    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()

if __name__ == "__main__":
    # Create an instance of the BreakTimeApp class
    app = BreakTimeApp()
    # Start the application
    app.run()
