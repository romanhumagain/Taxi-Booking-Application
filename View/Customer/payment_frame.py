from tkinter import  *
class PaymentFrame(Frame):
    def __init__(self, window=None):
        super().__init__(window)

        self.config(bg="white", width=850, height=600)

        label = Label(self, text="Payment Frame ", font=("Arial", 40))
        label.place(relx=0.5, rely=0.5, anchor="center")