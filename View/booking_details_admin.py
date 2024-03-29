import tkinter.ttk
from tkinter import *
from tkinter import messagebox

import customtkinter
from PIL import ImageTk, Image as PILImage

from Controller.admin_dashboard_dbms import fetch_pending_booking_details, fetch_active_booking, fetch_booking_history, \
    search_booking_history, fetch_completed_booking
from Controller.booking_dbms import cancel_booking
from Model.booking import Booking

class BookingDetails:
    def __init__(self, window, cancel_booking_callback = None, count_booking_callback= None, top_level_list=None, count_total_booking= None):
        if top_level_list is None:
            top_level_list = []
        self.window = window
        self.cancel_booking_callback = cancel_booking_callback
        self.count_booking_callback = count_booking_callback
        self.count_total_booking = count_total_booking

        self.top_level_list = top_level_list

        self.font = "Century Gothic"
        self.booking_id = 0

    def show_booking_details_window(self):
        self.booking_details_window = Toplevel(self.window, bg="#3c3c3c")
        self.booking_details_window.title("Customer Booking Details")
        self.booking_details_window.resizable(0, 0)

        # to add the toplevel window to the list in the AdminDashboard
        self.top_level_list.append(self.booking_details_window)

        width = 1000
        height = 550

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_position = (screen_width - width) // 2 + 140
        y_position = (screen_height - height) // 2

        self.booking_details_window.geometry(f"{width}x{height}+{x_position}+{y_position}")

        self.cancel_booking = None

        self.top_frame = customtkinter.CTkFrame(self.booking_details_window, width=980, height=100, corner_radius=20)
        self.top_frame.place(x=10, y=20)

        self.heading_label = customtkinter.CTkLabel(self.top_frame, text="", font=(self.font, 30))
        self.heading_label.place(relx=0.5, rely=0.5, anchor = "center")

        self.table_frame = customtkinter.CTkFrame(self.booking_details_window, width=800, height=350, corner_radius=20)
        self.table_frame.place(x= 10, y= 180)

        #  for search entry
        self.search_entry = customtkinter.CTkEntry(master=self.booking_details_window, width=100, height=36,
                                                   placeholder_text="Booking ID")
        self.search_entry.place(x=30, y=130)

        search_btn_image = ImageTk.PhotoImage(PILImage.open("Images/search.png").resize((20, 20), PILImage.ANTIALIAS))

        self.search_button = customtkinter.CTkButton(master=self.booking_details_window, width=60, height=35, text="search",
                                                     corner_radius=15, font=(self.font, 15), image=search_btn_image,command=self.search)
        self.search_button.place(x=140, y=132)

        self.button_frame = customtkinter.CTkFrame(self.booking_details_window, width=170, height=400, corner_radius=20)
        self.button_frame.place(x=820, y= 130)

        active_btn_image = ImageTk.PhotoImage(PILImage.open("Images/active.png").resize((30,30), PILImage.ANTIALIAS))

        self.active_button = customtkinter.CTkButton(self.button_frame,text="Active ", width=150, font=(self.font, 16, 'bold'), height=35,corner_radius=10,image=active_btn_image, command=self.create_active_booking_table)
        self.active_button.place(x=10, y= 70)

        pending_btn_image = ImageTk.PhotoImage(PILImage.open("Images/pending.png").resize((30,30), PILImage.ANTIALIAS))


        self.pending_booking = customtkinter.CTkButton(self.button_frame, text="Pending", width=150, height=35,
                                                     font=(self.font, 16, 'bold'), corner_radius=10, image=pending_btn_image,command=self.create_pending_table)
        self.pending_booking.place(x=10, y=145)

        history_btn_image = ImageTk.PhotoImage(PILImage.open("Images/history.png").resize((30,30), PILImage.ANTIALIAS))


        self.booking_history = customtkinter.CTkButton(self.button_frame, text="History", width=150,height=35,image=history_btn_image,
                                                       font=(self.font, 16, 'bold'), corner_radius=10, command=self.create_booking_history_table)
        self.booking_history.place(x=10, y=220)

        complete_btn_image = ImageTk.PhotoImage(PILImage.open("Images/approved.png").resize((25, 25), PILImage.ANTIALIAS))

        self.complete_booking = customtkinter.CTkButton(self.button_frame, text="Completed", width=150, height=35,
                                                      font=(self.font, 16, 'bold'), corner_radius=10,
                                                      image=complete_btn_image, command=self.create_completed_booking_table)
        self.complete_booking.place(x=10, y=295)


        # creating a table in the table_frame to show the booking details

        self.booking_table_frame = Frame(self.table_frame, bg="white", width=780, height=320)
        self.booking_table_frame.place(x=10, y=15)

        booking_details_table = tkinter.ttk.Treeview(self.table_frame, height=12, columns=("booking_id", "customer_id", "pickup", "date", "time", "dropoff", "driver_name"))

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

        self.create_active_booking_table()

    def clear_booking_table_frame(self):
        for widget in self.booking_table_frame.winfo_children():
            widget.destroy()
    def create_active_booking_table(self):
        self.heading_label.configure(text="Customer Active Booking Details")
        self.clear_booking_table_frame()

        self.scroll_y = Scrollbar(self.booking_table_frame, orient=VERTICAL)
        self.active_booking_table = tkinter.ttk.Treeview(self.booking_table_frame, height=12, columns=("booking_id", "customer_id", "pickup", "date", "time", "dropoff", "driver_id","driver_name"),show="headings", yscrollcommand=self.scroll_y)
        self.active_booking_table.place(x=0, y=0)

        self.active_booking_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.active_booking_table.heading("customer_id", text="C-ID", anchor=CENTER)
        self.active_booking_table.heading("pickup", text="Pickup Address", anchor=CENTER)
        self.active_booking_table.heading("date", text="Date", anchor=CENTER)
        self.active_booking_table.heading("time", text="Time", anchor=CENTER)
        self.active_booking_table.heading("dropoff", text="Dropoff Address", anchor=CENTER)
        self.active_booking_table.heading("driver_id", text="D-ID", anchor=CENTER)
        self.active_booking_table.heading("driver_name", text="D-Name", anchor=CENTER)


        self.active_booking_table.column("booking_id", width=50, anchor=CENTER)
        self.active_booking_table.column("customer_id", width=50, anchor=CENTER)
        self.active_booking_table.column("pickup", width=170, anchor=CENTER)
        self.active_booking_table.column("date", width=60, anchor=CENTER)
        self.active_booking_table.column("time", width=50, anchor=CENTER)
        self.active_booking_table.column("dropoff", width=170, anchor=CENTER)
        self.active_booking_table.column("driver_id", width=50, anchor=CENTER)
        self.active_booking_table.column("driver_name", width=180, anchor=CENTER)

        self.display_active_booking()

    def create_pending_table(self):
        self.heading_label.configure(text="Customer Pending Booking Details")

        self.clear_booking_table_frame()

        self.scroll_y = Scrollbar(self.booking_table_frame, orient=VERTICAL)
        self.pending_booking_table = tkinter.ttk.Treeview(
            self.booking_table_frame,
            columns=("booking_id", "customer_id", "customer_name", "pickup_address", "date", "time", "dropoff_address",
                     "status"),
            show="headings",
            height=12,
            yscrollcommand=self.scroll_y.set
        )

        # self.scroll_y.place(x=1120, y=0, height=300)
        self.pending_booking_table.place(x=0, y=0)
        self.pending_booking_table.bind("<ButtonRelease-1>", self.select_booking)

        self.pending_booking_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.pending_booking_table.heading("customer_id", text="C-ID", anchor=CENTER)
        self.pending_booking_table.heading("customer_name", text="Name", anchor=CENTER)
        self.pending_booking_table.heading("pickup_address", text="Pickup Address", anchor=CENTER)
        self.pending_booking_table.heading("date", text="Date", anchor=CENTER)
        self.pending_booking_table.heading("time", text="Time", anchor=CENTER)
        self.pending_booking_table.heading("dropoff_address", text="Dropoff Address", anchor=CENTER)
        self.pending_booking_table.heading("status", text="Status", anchor=CENTER)

        self.pending_booking_table.column("booking_id", width=50, anchor=CENTER)
        self.pending_booking_table.column("customer_id", width=50, anchor=CENTER)
        self.pending_booking_table.column("customer_name", width=100, anchor=CENTER)
        self.pending_booking_table.column("pickup_address", width=200, anchor=CENTER)
        self.pending_booking_table.column("date", width=60, anchor=CENTER)
        self.pending_booking_table.column("time", width=60, anchor=CENTER)
        self.pending_booking_table.column("dropoff_address", width=180, anchor=CENTER)
        self.pending_booking_table.column("status", width=80, anchor=CENTER)


        self.display_pending_booking()


    def create_booking_history_table(self):
        self.clear_booking_table_frame()

        self.heading_label.configure(text="Customer Booking History")

        self.scroll_y = Scrollbar(self.booking_table_frame, orient=VERTICAL)
        self.booking_history_table = tkinter.ttk.Treeview(self.booking_table_frame, height=12, columns=(
        "booking_id", "customer_id", "pickup", "date", "time", "dropoff", "driver_id", "driver_name", "status"), show="headings",
                                                         yscrollcommand=self.scroll_y)
        self.booking_history_table.place(x=0, y=0)

        self.booking_history_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.booking_history_table.heading("customer_id", text="C-ID", anchor=CENTER)
        self.booking_history_table.heading("pickup", text="Pickup Address", anchor=CENTER)
        self.booking_history_table.heading("date", text="Date", anchor=CENTER)
        self.booking_history_table.heading("time", text="Time", anchor=CENTER)
        self.booking_history_table.heading("dropoff", text="Dropoff Address", anchor=CENTER)
        self.booking_history_table.heading("driver_id", text="D-ID", anchor=CENTER)
        self.booking_history_table.heading("driver_name", text="D-Name", anchor=CENTER)
        self.booking_history_table.heading("status", text="Status", anchor=CENTER)


        self.booking_history_table.column("booking_id", width=40, anchor=CENTER)
        self.booking_history_table.column("customer_id", width=40, anchor=CENTER)
        self.booking_history_table.column("pickup", width=150, anchor=CENTER)
        self.booking_history_table.column("date", width=60, anchor=CENTER)
        self.booking_history_table.column("time", width=50, anchor=CENTER)
        self.booking_history_table.column("dropoff", width=150, anchor=CENTER)
        self.booking_history_table.column("driver_id", width=40, anchor=CENTER)
        self.booking_history_table.column("driver_name", width=150, anchor=CENTER)
        self.booking_history_table.column("status", width=100, anchor=CENTER)


        self.display_booking_history()

    def create_completed_booking_table(self):
        self.heading_label.configure(text="Customer Completed Booking Details")
        self.clear_booking_table_frame()

        self.scroll_y = Scrollbar(self.booking_table_frame, orient=VERTICAL)
        self.completed_booking_table = tkinter.ttk.Treeview(self.booking_table_frame, height=12, columns=("booking_id", "customer_id", "pickup", "date", "time", "dropoff", "driver_id","driver_name", "status"),show="headings", yscrollcommand=self.scroll_y)
        self.completed_booking_table.place(x=0, y=0)

        self.completed_booking_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.completed_booking_table.heading("customer_id", text="C-ID", anchor=CENTER)
        self.completed_booking_table.heading("pickup", text="Pickup Address", anchor=CENTER)
        self.completed_booking_table.heading("date", text="Date", anchor=CENTER)
        self.completed_booking_table.heading("time", text="Time", anchor=CENTER)
        self.completed_booking_table.heading("dropoff", text="Dropoff Address", anchor=CENTER)
        self.completed_booking_table.heading("driver_id", text="D-ID", anchor=CENTER)
        self.completed_booking_table.heading("driver_name", text="D-Name", anchor=CENTER)
        self.completed_booking_table.heading("status", text="Status", anchor=CENTER)



        self.completed_booking_table.column("booking_id", width=40, anchor=CENTER)
        self.completed_booking_table.column("customer_id", width=40, anchor=CENTER)
        self.completed_booking_table.column("pickup", width=150, anchor=CENTER)
        self.completed_booking_table.column("date", width=50, anchor=CENTER)
        self.completed_booking_table.column("time", width=50, anchor=CENTER)
        self.completed_booking_table.column("dropoff", width=150, anchor=CENTER)
        self.completed_booking_table.column("driver_id", width=40, anchor=CENTER)
        self.completed_booking_table.column("driver_name", width=140, anchor=CENTER)
        self.completed_booking_table.column("status", width=140, anchor=CENTER)

        self.display_completed_booking()

    def display_pending_booking(self):
        result = fetch_pending_booking_details()
        if result is not None:
            for item in self.pending_booking_table.get_children():
                self.pending_booking_table.delete(item)

            for row in result:
                self.pending_booking_table.insert('', END, values=row)

    def display_active_booking(self):
        result = fetch_active_booking()
        if result is not None:
            for item in self.active_booking_table.get_children():
                self.active_booking_table.delete(item)

            for row in result:
                self.active_booking_table.insert('', END, values=row)

    def display_booking_history(self):
        result = fetch_booking_history()
        if result is not None:
            for item in self.booking_history_table.get_children():
                self.booking_history_table.delete(item)

            for row in result:
                self.booking_history_table.insert('', END, values=row)

    def display_completed_booking(self):
        result = fetch_completed_booking()
        if result is not None:
            for item in self.completed_booking_table.get_children():
                self.completed_booking_table.delete(item)

            for row in result:
                self.completed_booking_table.insert('', END, values=row)

    def select_booking(self, event):
        view_info = self.pending_booking_table.focus()
        booking_details = self.pending_booking_table.item(view_info)

        row = booking_details.get("values")
        self.booking_id = row[0]

    def search(self):
        booking_id = self.search_entry.get()
        if booking_id != "":
            booking = Booking(booking_id= booking_id)
            fetched_booking = search_booking_history(booking)
            if len(fetched_booking) != 0:
                self.create_booking_history_table()
                for item in self.booking_history_table.get_children():
                    self.booking_history_table.delete(item)
                for row in fetched_booking:
                    self.booking_history_table.insert('', END, values=row)
            else:
                messagebox.showerror("Not Found", f"Invalid Booking ID", parent = self.booking_details_window)

        else:
            messagebox.showerror("", "Please Provide Booking ID TO Search Booking", parent = self.booking_details_window)


if __name__ == '__main__':
    window = Tk()
    bookingDetails = BookingDetails(window)
    bookingDetails.show_booking_details_window()
    window.mainloop()