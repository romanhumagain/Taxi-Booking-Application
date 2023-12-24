import tkinter
from tkinter import *
import customtkinter
from tkinter.ttk import Treeview

from PIL import ImageTk, Image

from Controller.driver_dashboard_dbms import fetch_complete_trip_history, fetch_incomplete_booking, \
    fetch_customer_details
from Model import Global
from Model.customer import Customer
from Model.driver import Driver
from tkinter import messagebox


class DriverTrip:
    def __init__(self, window, top_level_list = None, dashboard_indicator=None):
        self.window = window
        self.font = "Century Gothic"
        self.customer_id = 0
        if top_level_list is None:
            self.top_level_list = []
        self.top_level_list = top_level_list
        self.dashboard_indicator = dashboard_indicator

        style1 = tkinter.ttk.Style()
        style1.theme_use("default")
        style1.configure("Treeview",
                         background="#F4F4F4",
                         foreground="black",
                         rowheight=25,
                         fieldbackground="#F5F5F5",
                         bordercolor="black",
                         borderwidth=0,
                         font=(self.font, 12))
        style1.map('Treeview', background=[('selected', '#7EC8E3')],
                   foreground=[('active', 'black')])

        #
        style1.configure("Treeview.Heading",
                         background="#4c4c4c",
                         foreground="white",
                         relief="flat",
                         font=('Century Gothic', 12),
                         padding=(0, 6)
                         )

        style1.map("Treeview.Heading",
                   background=[('active', '#3c3c3c')],
                   foreground=[('active', 'white')])


    def show_driver_trip_window(self):
        self.driver_trip_window = Toplevel(self.window, bg="#3c3c3c")
        self.driver_trip_window.title("Driver Trip Details")
        self.driver_trip_window.resizable(0, 0)

        # Configure the window close event to call the on_closing function
        self.driver_trip_window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.top_level_list.append(self.driver_trip_window)


        width = 910
        height = 500

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_position = (screen_width - width) // 2 + 140
        y_position = (screen_height - height) // 2

        self.driver_trip_window.geometry(f"{width}x{height}+{x_position}+{y_position}")

        self.top_frame = customtkinter.CTkFrame(self.driver_trip_window, width= 870, height=100, corner_radius=25)
        self.top_frame.place(x=20, y=10)

        self.heading_label = customtkinter.CTkLabel(self.top_frame, text="", font=(self.font, 30))
        self.heading_label.place(relx= 0.5, rely=0.5, anchor = "center")


        self.button_frame = customtkinter.CTkFrame(self.driver_trip_window, width= 160, height=350, corner_radius=25)
        self.button_frame.place(x= 730, y=120)

        history_btn_image = ImageTk.PhotoImage(Image.open("Images/history.png").resize((20, 20), Image.ANTIALIAS))

        self.history_button = customtkinter.CTkButton(self.button_frame, text="Trip History", width=150, height=35,font=(self.font, 18), corner_radius=15,image=history_btn_image, command=self.show_trip_history)
        self.history_button.place(relx=0.5, rely = 0.28, anchor = "center")

        incomplete_btn_image = ImageTk.PhotoImage(Image.open("Images/pending.png").resize((20, 20), Image.ANTIALIAS))

        self.incomplete_button = customtkinter.CTkButton(self.button_frame, text="Incomplete Trip", width=150, height=35,image=incomplete_btn_image,
                                                      font=(self.font, 14), corner_radius=15, command=self.show_incomplete_trip)
        self.incomplete_button.place(relx=0.5, rely=0.48, anchor="center")

        customer_btn_image = ImageTk.PhotoImage(Image.open("Images/profile1.png").resize((20, 20), Image.ANTIALIAS))

        self.customer_button = customtkinter.CTkButton(self.button_frame, text="Customer Info", width=150,
                                                         height=35,
                                                         font=(self.font, 15), corner_radius=15, command=self.view_customer_info, image=customer_btn_image)
        self.customer_button.place(relx=0.5, rely=0.68, anchor="center")

        self.table_frame = customtkinter.CTkFrame(self.driver_trip_window, width=700, height=350, corner_radius=25)
        self.table_frame.place(x=20, y=120)

        self.show_trip_history()

        # self.show_customer_info()

    def create_table(self):
        self.trip_table = Treeview(
            self.table_frame,
            columns=("booking_id", "customer_id", "pickup_address", "date", "time", "dropoff_address"),
            show="headings",
            height=14,
        )

        self.trip_table.place(x=0, y=0)
        # self.assigned_booking_table.bind("<ButtonRelease-1>", self.select_booking)

        self.trip_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.trip_table.heading("customer_id", text="C-ID", anchor=CENTER)
        self.trip_table.heading("pickup_address", text="Pickup", anchor=CENTER)
        self.trip_table.heading("date", text="Date", anchor=CENTER)
        self.trip_table.heading("time", text="Time", anchor=CENTER)
        self.trip_table.heading("dropoff_address", text="Dropoff", anchor=CENTER)

        self.trip_table.column("booking_id", width=70, anchor=CENTER)
        self.trip_table.column("customer_id", width=70, anchor=CENTER)
        self.trip_table.column("pickup_address", width=200, anchor=CENTER)
        self.trip_table.column("date", width=80, anchor=CENTER)
        self.trip_table.column("time", width=80, anchor=CENTER)
        self.trip_table.column("dropoff_address", width=200, anchor=CENTER)

        self.trip_table.bind("<ButtonRelease-1>", self.select_customer)
    def show_trip_history(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        self.create_table()
        self.get_trip_history()
        self.customer_id = 0
        self.heading_label.configure(text="Your Trip History")

    def show_customer_info(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        self.heading_label.configure(text="Customer Info")

        self.customer_details_table = Treeview(
            self.table_frame,
            columns=("customer_id", "customer_name", "phone","address","gender", "date_of_birth"),
            show="headings",
            height=14,
        )

        self.customer_details_table.place(x=0, y=0)

        self.customer_details_table.heading("customer_id", text="C-ID", anchor=CENTER)
        self.customer_details_table.heading("customer_name", text="Name", anchor=CENTER)
        self.customer_details_table.heading("phone", text="Phone No.", anchor=CENTER)
        self.customer_details_table.heading("address", text="Address", anchor=CENTER)
        self.customer_details_table.heading("gender", text="Gender", anchor=CENTER)
        self.customer_details_table.heading("date_of_birth", text="D.O.B", anchor=CENTER)

        self.customer_details_table.column("customer_id", width=50, anchor=CENTER)
        self.customer_details_table.column("customer_name", width=190, anchor=CENTER)
        self.customer_details_table.column("phone", width=120, anchor=CENTER)
        self.customer_details_table.column("address", width=140, anchor=CENTER)
        self.customer_details_table.column("gender", width=100, anchor=CENTER)
        self.customer_details_table.column("date_of_birth", width=100, anchor=CENTER)


    def show_incomplete_trip(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        self.create_table()
        self.get_incomplete_trip()
        self.customer_id = 0
        self.heading_label.configure(text="Incomplete Trip Details")



    # =============== FUNCTION TO FETCH THE DATA FROM THE BACKED ==================

    def get_trip_history(self):
        driver = Driver(driver_id=Global.logged_in_driver[0])
        result = fetch_complete_trip_history(driver)

        if len(result) != 0:
            for item in self.trip_table.get_children():
                self.trip_table.delete(item)

            for row in result:
                self.trip_table.insert('', END, values=row)

    def get_incomplete_trip(self):
        driver = Driver(driver_id=Global.logged_in_driver[0])
        result = fetch_incomplete_booking(driver)

        if result is not None:
            for item in self.trip_table.get_children():
                self.trip_table.delete(item)

            for row in result:
                self.trip_table.insert('', END, values=row)

    def select_customer(self, event):
        value_info = self.trip_table.focus()
        customer_info = self.trip_table.item(value_info)

        row = customer_info.get('values')
        self.customer_id = row[1]

    def view_customer_info(self):
        if self.customer_id != 0:
            self.show_customer_info()
            customer = Customer(customer_id = self.customer_id)
            result = fetch_customer_details(customer)
            if result is not None:
                for item in self.customer_details_table.get_children():
                    self.customer_details_table.delete(item)

                for row in result:
                    self.customer_details_table.insert('', END, values=row)

        else:
            messagebox.showerror("ERROR!", "Please Select Customer's Booking To View The Customer Info!", parent=self.driver_trip_window)

    def on_closing(self):
        self.driver_trip_window.destroy()
        self.dashboard_indicator()

if __name__ == '__main__':
    window = Tk()
    driverTrip = DriverTrip(window)
    driverTrip.show_driver_trip_window()
    window.mainloop()




