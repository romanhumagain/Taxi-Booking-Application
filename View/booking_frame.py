from tkinter import *
from tkinter import Frame, Label
import customtkinter as ctk
import tkintermapview
from tkcalendar import  DateEntry

from tkinter import messagebox
from Model.booking import Booking
from Model.account_activity import AccountActivity
from Controller.booking_dbms import booking_taxi
from Controller.account_activity_dbms import insert_account_activity_details
from PIL import Image, ImageTk
from datetime import datetime


from Model import Global
from View.approved_booking import ApprovedBooking
from View.booking_history import BookingHistory
from View.cancel_booking import CancelBooking
from View.update_booking import UpdateBooking


class BookingFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.config(bg="#0E0E0E", width=900, height=600)
        font = "Century Gothic"

        # Creating a textvariable for the entry box
        self.pickUpAddress = StringVar()
        self.pickUpDate = StringVar()
        self.pickUpTime = StringVar()
        self.dropOffAddress = StringVar()

        heading_icon = ImageTk.PhotoImage(Image.open("Images/details.png"))
        self.heading_icon_label = Label(self, image=heading_icon, bg='#0E0E0E')
        self.heading_icon_label.image = heading_icon
        self.heading_icon_label.place(x=240, y=15)

        self.heading_label = Label(self, text="Book Your Rides !", font=(font, 26), bg="#0E0E0E", fg="white")
        self.heading_label.place(relx=0.53, rely=0.08, anchor="center")

        self.pickup_address_label = Label(self, text="Pick Up Address", font=(font,14), bg="#0E0E0E", fg="white")
        self.pickup_address_label.place(x=30, y=150)

        self.pickup_address_entry = ctk.CTkEntry(self,font=(font, 15),width=180, height=38,textvariable=self.pickUpAddress)
        self.pickup_address_entry.place(x=195,y= 145)

        self.pickup_date_label = Label(self, text="Pick Up Date", font=(font, 14), bg="#0E0E0E", fg="white")
        self.pickup_date_label.place(x=30, y=230)

        self.pickup_date_entry = DateEntry(self, font=(font, 15), width=14, height=38,textvariable=self.pickUpDate)
        self.pickup_date_entry.place(x=195, y=230)

        self.pickup_time_label = Label(self, text="Pick Up Time", font=(font, 14), bg="#0E0E0E", fg="white")
        self.pickup_time_label.place(x=30, y=310)

        self.pickup_time_entry = ctk.CTkEntry(self, font=(font, 15), width=180, height=38,textvariable=self.pickUpTime)
        self.pickup_time_entry.place(x=195, y=310)

        self.dropoff_address_label = Label(self, text="Drop Off Address", font=(font, 14), bg="#0E0E0E", fg="white")
        self.dropoff_address_label.place(x=30, y=390)

        self.dropff_address_entry = ctk.CTkEntry(self, font=(font, 15), width=180, height=38,textvariable=self.dropOffAddress)
        self.dropff_address_entry.place(x=195, y=390)

        self.request_booking_button = ctk.CTkButton(master=self, text="Request Booking",font=(font, 16), corner_radius=8, height=35, width=120, command=self.booking_taxi)
        self.request_booking_button.place(x=30, y=530)

        self.update_booking_button = ctk.CTkButton(master=self, text="Update Booking", font=(font, 16),corner_radius=8, height=35, width=150, command=self.update_booking)
        self.update_booking_button.place(x=200, y=530)

        self.cancel_booking_button = ctk.CTkButton(master=self, text="Cancel Booking", font=(font, 16),
                                                   corner_radius=8, height=35, width=150, command=self.cancel_booking)
        self.cancel_booking_button.place(x=380, y=530)

        self.approved_booking_button = ctk.CTkButton(master=self, text="Approved Booking", font=(font, 16),
                                               corner_radius=8, height=35, width=150, command=self.approved_booking)
        self.approved_booking_button.place(x=555, y=530)

        self.booking_history_button = ctk.CTkButton(master=self, text="Booking History", font=(font, 16),corner_radius=8, height=35, width=150, command=self.booking_history)
        self.booking_history_button.place(x=735, y=530)

        self.map_frame = Frame(self, bg="red", width=480, height=400)
        self.map_frame.place(x=400, y=100)

        self.display_map()

    def display_map(self):
        try:
            latitude = 27.7172
            longitude = 85.3240

            # The line below initializes the map_view attribute
            self.map_view = tkintermapview.TkinterMapView(self.map_frame, width=480, height=400)
            self.map_view.pack(expand=True)

            # Set the position and zoom level
            self.map_view.set_position(latitude, longitude)
            self.map_view.zoom(8)

        except Exception as e:
            print(f"Error displaying map: {e}")


        except Exception as e:
            print(f"Error displaying map: {e}")

    def update_booking(self):
            updateBooking = UpdateBooking(self)
            updateBooking.show_update_booking_window()
    def cancel_booking(self):
        cancelBooking = CancelBooking(self)
        cancelBooking.show_cancel_booking_window()

    def approved_booking(self):
        approvedBooking = ApprovedBooking(self)
        approvedBooking.show_approved_booking_window()

    def booking_history(self):
        bookingHistory = BookingHistory(self)
        bookingHistory.show_booking_history_window()

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
                    # TO INSERT RECORDS TO THE ACCOUNT ACTIVITY TABLE
                    current_date_time = datetime.now()
                    current_date = current_date_time.date()
                    current_time = current_date_time.time()

                    activity_related = "Booking Requested"
                    description = f"Your Booking was requested for the trip of {self.pickUpAddress.get()} to {self.dropOffAddress.get()}"

                    accountActivity = AccountActivity(activity_related=activity_related, description=description,
                                                      date=current_date, time=current_time,
                                                      user_id=Global.current_user[0])
                    account_activity_stored = insert_account_activity_details(accountActivity)
                    if account_activity_stored:
                        message_content = (
                            "Your booking request was successful!\n\n"
                            "Thank you for choosing our service. Your booking is now pending approval. "
                            "Our team will review your request, and you can expect a confirmation within 24 hours.\n\n"
                        )
                        messagebox.showinfo("Booking Success", message_content)
                        self.clear_field()
                    else:
                        messagebox.showerror("ERROR!", "Account Activity Couldn't Store.")
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






