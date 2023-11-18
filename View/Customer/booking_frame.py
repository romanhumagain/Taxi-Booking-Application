from tkinter import *
from tkinter import Frame, Label
import customtkinter as ctk
from tkcalendar import  DateEntry
from update_booking import *
from tkinter import messagebox
from Model.booking import Booking
from Controller.booking_dbms import booking_taxi
from PIL import Image, ImageTk

from Model import Global
class BookingFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.config(bg="black", width=850, height=600)
        font = "Century Gothic"

        # Creating a textvariable for the entry box
        self.pickUpAddress = StringVar()
        self.pickUpDate = StringVar()
        self.pickUpTime = StringVar()
        self.dropOffAddress = StringVar()

        heading_icon = ImageTk.PhotoImage(Image.open("Images/details.png"))
        self.heading_icon_label = Label(self, image=heading_icon, bg='black')
        self.heading_icon_label.image = heading_icon
        self.heading_icon_label.place(x=240, y=15)

        self.heading_label = Label(self, text="Book Your Rides !", font=(font, 26), bg="black", fg="white")
        self.heading_label.place(relx=0.53, rely=0.08, anchor="center")

        self.pickup_address_label = Label(self, text="Pick Up Address", font=(font,14), bg="black", fg="white")
        self.pickup_address_label.place(x=30, y=140)

        self.pickup_address_entry = ctk.CTkEntry(self,font=(font, 15),width=200, height=38,textvariable=self.pickUpAddress)
        self.pickup_address_entry.place(x=200,y= 135)

        self.pickup_date_label = Label(self, text="Pick Up Date", font=(font, 14), bg="black", fg="white")
        self.pickup_date_label.place(x=30, y=220)

        self.pickup_date_entry = DateEntry(self, font=(font, 15), width=16, height=38,textvariable=self.pickUpDate)
        self.pickup_date_entry.place(x=200, y=220)

        self.pickup_time_label = Label(self, text="Pick Up Time", font=(font, 14), bg="black", fg="white")
        self.pickup_time_label.place(x=30, y=300)

        self.pickup_time_entry = ctk.CTkEntry(self, font=(font, 15), width=200, height=38,textvariable=self.pickUpTime)
        self.pickup_time_entry.place(x=200, y=300)

        self.dropoff_address_label = Label(self, text="Drop Off Address", font=(font, 14), bg="black", fg="white")
        self.dropoff_address_label.place(x=30, y=380)

        self.dropff_address_entry = ctk.CTkEntry(self, font=(font, 15), width=200, height=38,textvariable=self.dropOffAddress)
        self.dropff_address_entry.place(x=200, y=380)

        self.request_booking_button = ctk.CTkButton(master=self, text="Request Booking",font=(font, 17,'bold'), corner_radius=8, height=35, width=200, command=self.booking_taxi)
        self.request_booking_button.place(x=30, y=480)

        self.clear_button = ctk.CTkButton(master=self, text="Clear", font=(font, 17, 'bold'),height=35,corner_radius=8, command=self.clear_field)
        self.clear_button.place(x=260, y=480)

        self.update_booking_button = ctk.CTkButton(master=self, text="Update Booking", font=(font, 17, 'bold'),corner_radius=8, height=35, width=170, command=self.update_booking)
        self.update_booking_button.place(x=600, y=210)

        self.approved_booking_button = ctk.CTkButton(master=self, text="Approved Booking", font=(font, 17, 'bold'),
                                               corner_radius=8, height=35, width=170)
        self.approved_booking_button.place(x=600, y=280)

        self.booking_history_button = ctk.CTkButton(master=self, text="Booking History", font=(font, 17, 'bold'),corner_radius=8, height=35, width=170)
        self.booking_history_button.place(x=600, y=350)

    def update_booking(self):
            updateBooking = UpdateBooking(self)
            updateBooking.show_update_booking_window()

    def booking_taxi(self):

        if Global.logged_in_customer is not None:  # Check if logged_in_customer is not None
            if not (
                    self.pickUpAddress.get() == "" or self.pickUpDate.get() == "" or self.pickUpTime.get() == "" or self.dropOffAddress.get() == ""):
                booking = Booking(
                    pickup_address=self.pickUpAddress.get(),
                    pickup_date=self.pickUpDate.get(),
                    pickup_time=self.pickUpTime.get(),
                    dropoff_address=self.dropOffAddress.get(),
                    booking_status="Pending",
                    customer_id=Global.logged_in_customer[0]
                )
                is_booked = booking_taxi(booking)
                if is_booked:
                    message_content = (
                        "Your booking request was successful!\n\n"
                        "Thank you for choosing our service. Your booking is now pending approval. "
                        "Our team will review your request, and you can expect a confirmation within 24 hours.\n\n"
                    )
                    messagebox.showinfo("Booking Success", message_content)
                    self.clear_field()
                else:
                    messagebox.showerror("Booking Failed!", "Sorry, Couldn't Book Your Request!")
            else:
                messagebox.showerror("Booking Failed!", "Please Provide All The Required Details !")
        else:
            messagebox.showerror("Booking Failed!", "User not logged in!")

    def clear_field(self):
        self.pickup_address_entry.delete(0, END)
        self.pickup_date_entry.delete(0, END)
        self.pickup_time_entry.delete(0, END)
        self.dropff_address_entry.delete(0, END)





