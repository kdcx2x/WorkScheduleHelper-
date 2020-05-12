from tkinter import *
from tkinter import ttk
import PyPDF2 
import glob
import os

def calculate(*args):
    try:
        filenumber = file_number.get()
        os.listdir("tesy")
        cur_path =os.getcwd()
        entries = os.listdir(cur_path)
        print(entries)
        text.set(filenumber)
    except ValueError:
        pass

root = Tk()
root.title("Timecard")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

file_number = StringVar()
text = StringVar()

fn_entry = ttk.Entry(mainframe, width=7, textvariable=file_number)
fn_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=text).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="file_number").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="text").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

fn_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()