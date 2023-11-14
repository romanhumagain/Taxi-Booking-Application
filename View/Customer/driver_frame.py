from tkinter import *
class DriverFrame(Frame):
    def __init__(self, window=None):
        super().__init__(window)

        self.config(bg="white", width=850, height=600)

        label = Label(self, text="Driver Frame ", font=("Arial", 40))
        label.place(relx=0.5, rely=0.5, anchor="center")