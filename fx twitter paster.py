from tkinter import *

import tkinter as tk
import pyperclip
import os

# main #

# Replace x.com with fxtwitter.com (twitter)
def replace_twitter_link(text):
    if "x.com" in text:
      return text.replace("x.com", "fxtwitter.com")
    else:
      return text

# Check clipboard

def monitor_clipboard():
    clipboarded_content = pyperclip.paste()

    # Only modify if the toggle is turned on

    if turnOn:
        modified_content = replace_twitter_link(clipboarded_content)

        if modified_content != clipboarded_content:
            pyperclip.copy(modified_content)
    root.after(500, monitor_clipboard)

# GUI #

root = tk.Tk()
root.title("Fx Twitter Paster")
root.geometry("500x300")

global turnOn
turnOn = False

# Create label
my_label = Label(root, text="Paster Disabled", fg="Gray", font=("Helvetica", 32))
my_label.pack(pady=20)

# Define images with path
path = os.getcwd()

on_image = PhotoImage(file=os.path.join(path + "/images/on.png"))
off_image = PhotoImage(file=os.path.join(path + "/images/off.png"))

## Switch ## 

def switch():
    global turnOn
    # Toggle the boolean state
    if turnOn:
        on_button.config(image=off_image)
        my_label.config(text="Paster Disabled", fg="Gray")
        turnOn = False
    else:
        on_button.config(image=on_image)
        my_label.config(text="Paster Enabled", fg="Black")
        turnOn = True

# Button 
on_button = Button(root, image=off_image, bd=0, command=switch)
on_button.pack(pady=50)

# Start clipboard monitoring in the Tkinter event loop
monitor_clipboard()

# Start the Tkinter main loop
root.mainloop()
