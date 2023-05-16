import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Test Driver (TV)")
root.config(bd=15)
text = tk.Text(root, width=40, height=10)
text.pack()

# create class
class TV:
    # make the test driver (TestTV)
    def __init__(self, name = "Default TV", channel = 98, volume = 4):
        self.name = name
        self.channel = channel
        self.volume = volume
        self.is_on = False

    def show(self):
        text.insert(tk.END, f"{self.name} - channel:{self.channel} | volume:{self.volume}\n")

    # method for status
    def status(self):
        status = f"{self.name} Status: ON" if self.is_on else f"{self.name} Status: OFF"
        messagebox.showinfo("Status", status)

    # turn on
    def turn_on(self):
        self.is_on = True
        messagebox.showinfo("Turn On", f"{self.name} is turned ON.")
    # turn off
    def turn_off(self):
        self.is_on = False
        messagebox.showinfo("Turn Off", f"{self.name} is turned OFF.")    
    # returns channel
    def get_channel(self):
        messagebox.showinfo("Channel", f"{self.name}'s channel is {self.channel}")
    # set a new channel    
    def set_channel(self,  new_channel):
        self.channel = new_channel
        messagebox.showinfo("Set Channel", f"New channel has been set: {new_channel}")
    # get volume level
    def get_volume(self):
        messagebox.showinfo("Volume", f"{self.name}'s volume level is {self.volume}")
    # set a new volume level
    def set_volume(self,  new_volume):
        self.volume = new_volume
        messagebox.showinfo("Set Volume", f"New volume level has been set: {new_volume}")
    # increase channel  
    def channel_up(self):
        self.channel += 1
    # decrease channel
    def channel_down(self):
        self.channel -= 1
    # increase volume
    def volume_up(self):
        self.volume += 1
    # decrease volume  
    def volume_down(self):
        self.volume -= 1
# create object of a class
default_tv = TV()
tv1 = TV("tv1", 30, 3)
tv2 = TV("tv2", 3, 2)
# call the method
tv1.show()  
tv2.show()
default_tv.show()
default_tv.turn_off()
default_tv.status()
default_tv.get_channel()
default_tv.set_channel(122)
default_tv.show()
tv2.channel_up()
tv2.show()
tv1.volume_down()
tv1.show()

root.mainloop()