from tkinter import *
import customtkinter
from PIL import Image, ImageTk

from Controller.invoice_dbms import fetch_payment_details
from Model.payment import Payment


class InvoiceFrame:
    def __init__(self, window, invoice_no = 0):
        self.window = window
        self.font = "Century Gothic"
        self.invoice_no = invoice_no

    def show_invoice_window(self):
        self.invoice_frame = Toplevel(self.window, width=550, height=500, bg="white")
        self.invoice_frame.resizable(0,0)
        self.invoice_frame.title("Invoice")

        # Create a menu bar
        menubar = Menu(self.invoice_frame)
        self.invoice_frame.config(menu=menubar)

        # Create a "File" menu
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        # Add a "Print" option to the "File" menu
        file_menu.add_command(label="Print")

        self.main_frame = Frame(self.invoice_frame, width=550, height=500, bg="white")
        self.main_frame.place(x=0, y=0)

        self.taxi_logo = Image.open("Images/taxi.png").resize((43,43), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(self.taxi_logo)

        self.taxi_logo_label = Label(self.main_frame, image=photo, bg='white')
        self.taxi_logo_label.image = photo
        self.taxi_logo_label.place(x=20, y=10)


        self.heading_label = Label(self.main_frame, text="Taxi Booking System", fg="black", bg="white", font=(self.font, 20, 'bold'))
        self.heading_label.place(relx=0.5, rely=0.05, anchor = "center")

        self.slogan_label = Label(self.main_frame, text="Your Journey, Your Way.", fg="black", bg="white",
                                   font=(self.font, 10))
        self.slogan_label.place(relx=0.5, rely=0.105, anchor="center")

        self.invoice_label = Label(self.main_frame, text="Invoice No.",fg="black", bg="white",font=(self.font, 12, 'bold') )
        self.invoice_label.place(x=350, y=83)

        self.invoice_No = Label(self.main_frame, text="", fg="black", bg="white", font=(self.font, 12, 'bold'))
        self.invoice_No.place(x=450, y=83)

        self.invoice_line = Canvas(self.main_frame, width=250, height=2.0, bg='#4c4c4c', highlightthickness=0)
        self.invoice_line.place(x=450, y=108, width=45)

        self.bid = Label(self.main_frame,text="ID:", fg="black", bg="white", font=(self.font, 12, 'bold'))
        self.bid.place(x=20, y=125)

        self.booking_id = Label(self.main_frame, text="", fg="black", bg="white", font=(self.font, 12, 'bold'))
        self.booking_id.place(x=45, y=125)

        self.name = Label(self.main_frame, text="Name:", fg="black", bg="white", font=(self.font, 12))
        self.name.place(x=20, y=165)

        self.customer_name = Label(self.main_frame, text="", fg="black", bg="white", font=(self.font, 12))
        self.customer_name.place(x=80, y=165)

        self.seperate_line1 = Canvas(self.main_frame, width=250, height=2.0, bg='#4c4c4c', highlightthickness=0)
        self.seperate_line1.place(x=0, y=215, width=550)

        # Creating table-like structure
        self.sn_label = Label(self.main_frame, text="S.N", fg="red", bg="white", font=(self.font, 12, 'bold'))
        self.sn_label.place(x=20, y=230)

        self.pickup_label = Label(self.main_frame, text="Pickup", fg="red", bg="white", font=(self.font, 12, 'bold'))
        self.pickup_label.place(x=80, y=230)

        self.dropoff_label = Label(self.main_frame, text="Dropoff", fg="red", bg="white",
                                   font=(self.font, 12, 'bold'))
        self.dropoff_label.place(x=240, y=230)

        self.km_label = Label(self.main_frame, text="KM", fg="red", bg="white", font=(self.font, 12, 'bold'))
        self.km_label.place(x=410, y=230)

        self.unit_label = Label(self.main_frame, text="Unit", fg="red", bg="white", font=(self.font, 12, 'bold'))
        self.unit_label.place(x=480, y=230)

        self.sn = Label(self.main_frame, text="", fg="black", bg="white", font=(self.font, 12, ''))
        self.sn.place(x=20, y=276)

        self.pickup = Label(self.main_frame, text="", fg="black", bg="white", font=(self.font, 12, ''))
        self.pickup.place(x=80, y=276)

        self.dropoff = Label(self.main_frame, text="", fg="black", bg="white",
                                   font=(self.font, 12, ''))
        self.dropoff.place(x=240, y=276)

        self.km = Label(self.main_frame, text="", fg="black", bg="white", font=(self.font, 12, ''))
        self.km.place(x=410, y=276)

        self.unit = Label(self.main_frame, text="", fg="black", bg="white", font=(self.font, 12, ''))
        self.unit.place(x=480, y=276)


        self.seperate_line2 = Canvas(self.main_frame, width=250, height=2.0, bg='#4c4c4c', highlightthickness=0)
        self.seperate_line2.place(x=0, y=350, width=550)

        self.total_amount_lbl = Label(self.main_frame, text="Total Amount:", fg="black", bg="white", font=(self.font, 12, 'bold'))
        self.total_amount_lbl.place(x=350, y=375)

        self.total_amount_label = Label(self.main_frame, text="", fg="black", bg="white",
                                      font=(self.font, 12, 'bold'))
        self.total_amount_label.place(x=470, y=375)


        self.footer_lbl1 = Label(self.main_frame, text="taxi.booking@info.gmail.com",fg="black", bg="white", font=(self.font, 11))
        self.footer_lbl1.place(relx=0.5, rely=0.9, anchor = "center")

        self.footer_lbl2 = Label(self.main_frame, text="011-6969696", fg="black", bg="white",
                                 font=(self.font, 11))
        self.footer_lbl2.place(relx=0.5, rely=0.96, anchor="center")

        self.display_invoice_details()


    def display_invoice_details(self):
        payment = Payment(payment_id=self.invoice_no)
        result = fetch_payment_details(payment)
        if result is not None:
            self.invoice_No.configure(text=result[0])
            self.booking_id.configure(text=result[1])
            self.customer_name.configure(text=result[2])
            self.total_amount_label.configure(text=result[7])

            self.sn.configure(text="1")
            self.pickup.configure(text=result[3])
            self.dropoff.configure(text=result[4])
            self.km.configure(text=result[6])
            self.unit.configure(text="100")

if __name__ == '__main__':
    window = Tk()
    invoiceFrame = InvoiceFrame(window)
    invoiceFrame.show_invoice_window()
    window.mainloop()