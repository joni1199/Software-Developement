import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

class GUI:
    def __init__(self,):
        window = tk.Tk()
        window.title('Calculator')
    
    frame = tk.Frame(master=window, bg="lightgreen", padx=10)

    entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
    entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)
    

    



class calc:
    def __init__(self, ):