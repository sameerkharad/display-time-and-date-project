#import tkinter by using pip
from tkinter import *
#by using tkinter import the label entry
from tkinter.tix import LabelEntry
from tkinter.ttk import *
#import strftime
from time import strftime


root = Tk()
root.title("clock")

def time():
    string = strftime("%m-%y\n%H:%M:%S %p")
    label.config(text=string)
    label.after(1000,time)

label = Label(root, font=("ds-digital, 80"),background = "white",foreground = "black")
label.pack(anchor='w')
time()
mainloop()