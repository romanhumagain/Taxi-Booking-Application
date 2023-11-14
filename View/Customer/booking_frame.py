from tkinter import Frame, Label

class BookingFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.config(bg="white", width=850, height=600)

        label = Label(self, text="Booking Frame ", font=("Arial", 40))
        label.place(relx=0.5, rely=0.5, anchor="center")
