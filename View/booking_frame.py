import re
from tkinter import *
from tkinter import Frame, Label

import customtkinter
import customtkinter as ctk
import tkintermapview
from tkcalendar import  DateEntry

from tkinter import messagebox

from Controller.payment_dbms import create_payment_table
from Model.booking import Booking
from Model.account_activity import AccountActivity
from Controller.booking_dbms import booking_taxi
from Controller.account_activity_dbms import insert_account_activity_details
from PIL import Image, ImageTk
from datetime import datetime


from Model import Global
from Model.payment import Payment
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

        today = datetime.today().date()
        self.pickup_date_entry = DateEntry(self, font=(font, 15), width=14, height=38, textvariable=self.pickUpDate,
                                           mindate=today)
        self.pickup_date_entry.place(x=195, y=230)

        self.pickup_time_label = Label(self, text="Pick Up Time", font=(font, 14), bg="#0E0E0E", fg="white")
        self.pickup_time_label.place(x=30, y=310)

        self.pickup_time_entry = ctk.CTkEntry(self, font=(font, 15), width=180, height=38, placeholder_text="0:00 AM/PM")
        self.pickup_time_entry.place(x=195, y=310)

        self.dropoff_address_label = Label(self, text="Drop Off Address", font=(font, 14), bg="#0E0E0E", fg="white")
        self.dropoff_address_label.place(x=30, y=390)

        self.dropff_address_entry = ctk.CTkEntry(self, font=(font, 15), width=180, height=38,textvariable=self.dropOffAddress)
        self.dropff_address_entry.place(x=195, y=390)

        full_screen_image = ImageTk.PhotoImage(Image.open("Images/full_screen.png").resize((40,40), Image.ANTIALIAS))
        full_screen_label = Label(self, image=full_screen_image, bg="#0E0E0E", cursor='hand2')
        full_screen_label.image = full_screen_image
        full_screen_label.place(x=850, y= 280)
        full_screen_label.bind("<Button-1>", self.view_full_screen_map)


        save_btn_image = ImageTk.PhotoImage(Image.open("Images/save.png").resize((20,20), Image.ANTIALIAS))


        self.request_booking_button = ctk.CTkButton(master=self, image=save_btn_image, text="Request Booking",font=(font, 16, 'bold'), corner_radius=8, height=35, width=120, command=self.booking_taxi)
        self.request_booking_button.place(x=120, y=460)

        self.clear_button = ctk.CTkButton(master=self, text="Clear", font=(font, 16),
                                                    corner_radius=8, height=35, width=120, command=self.booking_taxi)
        # self.clear_button.place(x=230, y=460)

        # for creating a frame to place a button
        self.button_frame = customtkinter.CTkFrame(master= self, width=870, height=70, corner_radius=20)
        self.button_frame.place(x=15, y=520)

        upodate_btn_image = ImageTk.PhotoImage(Image.open("Images/update.png").resize((20,20), Image.ANTIALIAS))

        self.update_booking_button = ctk.CTkButton(master=self.button_frame, text="Update Booking",image = upodate_btn_image, font=(font, 16, 'bold'),corner_radius=8, height=35, width=150, command=self.update_booking)
        self.update_booking_button.place(x=50, y=17)

        cancel_btn_image = ImageTk.PhotoImage(Image.open("Images/cancel.png").resize((20,20), Image.ANTIALIAS))

        self.cancel_booking_button = ctk.CTkButton(master=self.button_frame, text="Cancel Booking",image=cancel_btn_image, font=(font, 16, 'bold'),
                                                   corner_radius=8, height=35, width=150, command=self.cancel_booking)
        self.cancel_booking_button.place(x=250, y=17)

        approved_btn_image = ImageTk.PhotoImage(Image.open("Images/approved.png").resize((20,20), Image.ANTIALIAS))


        self.approved_booking_button = ctk.CTkButton(master=self.button_frame, text="Approved Booking",image=approved_btn_image, font=(font, 16, 'bold'),
                                               corner_radius=8, height=35, width=150, command=self.approved_booking)
        self.approved_booking_button.place(x=450, y=17)

        history_btn_image = ImageTk.PhotoImage(Image.open("Images/history.png").resize((20,20), Image.ANTIALIAS))

        self.booking_history_button = ctk.CTkButton(master=self.button_frame, text="Booking History",image=history_btn_image, font=(font, 16, 'bold'),corner_radius=8, height=35, width=150, command=self.booking_history)
        self.booking_history_button.place(x=670, y=17)

        self.map_frame = Frame(self, bg="red", width=480, height=400)
        self.map_frame.place(x=400, y=100)

        self.display_map()

    def display_map(self):
        try:
            latitude = 27.7172
            longitude = 85.3240

            # The line below initializes the map_view attribute
            self.map_view = tkintermapview.TkinterMapView(self.map_frame, width=450, height=400)
            self.map_view.pack(expand=True)

            # Set the position and zoom level
            self.map_view.set_position(latitude, longitude)
            self.map_view.zoom(8)

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

    def is_valid_pickup_date(self, pickup_date):
        try:
            pickup_date_object = datetime.strptime(pickup_date, "%m/%d/%y").date()
            current_date = datetime.today().date()
            return pickup_date_object >= current_date
        except ValueError:
            return False

    def booking_taxi(self):
        print(self.pickUpDate.get())
        if Global.logged_in_customer is not None:  # Check if logged_in_customer is not None
            if not (self.pickUpAddress.get() == "" or self.pickUpDate.get() == "" or self.pickup_time_entry.get() == "" or self.dropOffAddress.get() == ""):
                valid_time = self.validate_time_format(self.pickup_time_entry.get())
                if valid_time:
                    if self.is_valid_pickup_date(self.pickUpDate.get()):
                        booking = Booking(
                            pickup_address=self.pickUpAddress.get(),
                            pickup_date=self.pickUpDate.get(),
                            pickup_time=self.pickup_time_entry.get(),
                            dropoff_address=self.dropOffAddress.get(),
                            booking_status="Pending",
                            customer_id=Global.logged_in_customer[0],
                            trip_status=""
                        )
                        is_booked = booking_taxi(booking)
                        if is_booked:
                            payment = Payment(booking_id=booking.get_booking_id())
                            payment_table_created = create_payment_table(payment)

                            if payment_table_created:
                                # TO INSERT RECORDS TO THE ACCOUNT ACTIVITY TABLE
                                current_date_time = datetime.now()
                                current_date = current_date_time.date()
                                current_time = current_date_time.time()

                                activity_related = "Booking Requested"
                                description = f"Your Booking was requested for the trip of {self.pickUpAddress.get()} to {self.dropOffAddress.get()}"

                                accountActivity = AccountActivity(activity_related=activity_related,
                                                                  description=description,
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
                                messagebox.showerror("Booking Failed!", "Sorry, Couldn't Create Payment Table !")
                        else:
                            messagebox.showerror("Booking Failed!", "Sorry, Couldn't Book Your Request!")
                    else:
                        messagebox.showerror("Invalid Pickup Date", "Please provide a pickup date on or after today.")
                else:
                    messagebox.showerror("Invalid Time Format", "Please Provide Time in 0:00 AM/PM Format.")
            else:
                messagebox.showerror("Booking Failed!", "Please Provide All The Required Details !")
        else:
            messagebox.showerror("Booking Failed!", "User not logged in!")


    def clear_field(self):
        self.pickup_address_entry.delete(0, END)
        self.pickup_date_entry.delete(0, END)
        self.pickup_time_entry.delete(0, END)
        self.dropff_address_entry.delete(0, END)

    def view_full_screen_map(self, event):
        self.full_map_window = Toplevel(self, width=900, height=600, bg="#2c2c2c")
        self.full_map_window.title("Full Map")
        self.full_map_window.resizable(0,0)

        screen_width = self.full_map_window.winfo_screenwidth()
        screen_height = self.full_map_window.winfo_screenheight()

        window_width = 900
        window_height = 600

        x_position = (screen_width - window_width) // 2 + 142
        y_position = (screen_height - window_height) // 2 + 55

        self.full_map_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        try:
            latitude = 27.7172
            longitude = 85.3240

            # The line below initializes the map_view attribute
            self.map_view = tkintermapview.TkinterMapView(self.full_map_window, width=900, height=600)
            self.map_view.pack(expand=True)

            # Set the position and zoom level
            self.map_view.set_position(latitude, longitude)
            self.map_view.zoom(8)

        except Exception as e:
            print(f"Error displaying map: {e}")

    def validate_time_format(self,time_str):
        # Regular expression for matching time in the format of "4:00 AM"
        time_pattern = re.compile(r'^([1-9]|1[0-2]):[0-5][0-9] (AM|PM)$', re.IGNORECASE)

        return bool(re.match(time_pattern, time_str))








