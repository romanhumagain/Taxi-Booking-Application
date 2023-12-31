import tkinter.ttk
from tkinter import *
import customtkinter
from PIL import Image as PILImage, ImageTk
from datetime import datetime

from Controller.admin_dashboard_dbms import fetch_customer_booking, fetch_pending_booking_details, \
    search_booking_details, fetch_total_booking, fetch_total_driver
from Controller.booking_dbms import cancel_booking
from Model.booking import Booking
from View.assign_driver import AssignDriverPage
from View.payment_details_admin import PaymentDetails
from customer_details_admin import CustomerDetails
from View.login_activity import LoginActivity
from driver_frame_admin import DriverWindow
from booking_details_admin import BookingDetails
from chart import BookingLineChart
from tkinter import messagebox

from Controller.customer_dbms import fetch_all_customer

# for the chart
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas as pd

class AdminDashboard:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.title("Customer Dashboard")
        self.window.state("zoomed")
        self.window.resizable(0, 0)

        self.booking_details_id = 0
        self.font = "Century Gothic"

        self.table_frame = None
        self.chart_frame = None

        self.top_levels = []

        self.selected_pending_booking_list = None
        self.pending_bookings = None


        # customtkinter.set_default_color_theme("green")



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


        customtkinter.set_appearance_mode("System")
        # customtkinter.set_default_color_theme("green")

        self.navbar = Frame(self.window, bg="#2c2c2c", pady=25)
        self.navbar.pack(side="top", fill="x")

        self.taxi_logo = PILImage.open("Images/taxi.png")
        photo = ImageTk.PhotoImage(self.taxi_logo)

        self.taxi_logo_label = Label(self.navbar, image=photo, bg='#2c2c2c')
        self.taxi_logo_label.image = photo
        self.taxi_logo_label.place(x=20, y=0)

        self.slogan_label = Label(self.navbar, text="Taxi Booking System - Admin Dashboard",
                                  fg='white', bg='#2c2c2c', font=(self.font, 25))
        self.slogan_label.pack()

        # ===== creating a side bar =====
        self.side_bar_frame = Frame(self.window, bg="#3c3c3c", width=300)
        self.side_bar_frame.pack(side='left',fill = 'y' )

        # for clock image
        clock_image = ImageTk.PhotoImage(PILImage.open("Images/datetime.png"))
        self.clock_image_label = Label(self.side_bar_frame, image=clock_image, bg='#3c3c3c', justify=CENTER)
        self.clock_image_label.image = clock_image
        self.clock_image_label.place(x=110, y=20)

        # for the time label
        self.time_label = Label(self.side_bar_frame, font=(self.font, 15), bg='#3c3c3c', fg='white')
        self.time_label.place(x=40, y=130)

        self.update_time()

        # creating line
        self.line = Canvas(self.side_bar_frame, width=300, height=1)
        self.line.place(x=0, y=170)

        # for the option in the side_bar_frame

        # for profile option
        self.dashboard_label = Label(self.side_bar_frame, text = "Dashboard",font=(self.font, 17), fg='white', bg='#3c3c3c', cursor='hand2')
        self.dashboard_label.place(x=130, y=205)
        self.dashboard_label.bind('<Button-1>', lambda event:self.dashboard_indicator(self.dashboard_indicator_lbl))

        self.dashboard_indicator_lbl = Label(self.side_bar_frame, bg="white", width=0, height=2)
        self.dashboard_indicator_lbl.place(x=80, y=205)

        # to show the icon image
        dashboard_icon = ImageTk.PhotoImage(PILImage.open("Images/booking1.png"))
        self.dashboard_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=dashboard_icon)
        self.dashboard_icon_label.image = dashboard_icon
        self.dashboard_icon_label.place(x=90, y=205)

        # for booking option
        self.customer_label = Label(self.side_bar_frame, text="Customer", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.customer_label.place(x=130, y=275)
        self.customer_label.bind("<Button-1>", lambda event:self.window_indicator(self.customer_indicator_lbl, self.customer_details_window))

        self.customer_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.customer_indicator_lbl.place(x=80, y=275)

        customer_icon = ImageTk.PhotoImage(PILImage.open("Images/profile1.png"))
        self.customer_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=customer_icon)
        self.customer_icon_label.image = customer_icon
        self.customer_icon_label.place(x=90, y=275)


        # for booking option
        self.booking_label = Label(self.side_bar_frame, text="Booking", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.booking_label.place(x=130, y=345)
        self.booking_label.bind("<Button-1>", lambda event:self.window_indicator(self.booking_indicator_lbl, self.booking_details_window))

        self.booking_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.booking_indicator_lbl.place(x=80, y=345)

        booking_icon = ImageTk.PhotoImage(PILImage.open("Images/booking1.png"))
        self.booking_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=booking_icon)
        self.booking_icon_label.image = booking_icon
        self.booking_icon_label.place(x=90, y=345)

        # for driver option
        self.driver_label = Label(self.side_bar_frame, text="Driver", font=(self.font, 17), fg='white', bg='#3c3c3c', cursor='hand2')
        self.driver_label.place(x=130, y=415)
        self.driver_label.bind("<Button-1>", lambda event:self.window_indicator(self.driver_indicator_lbl, self.driver_details_window))

        self.driver_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.driver_indicator_lbl.place(x=80, y=415)

        driver_icon = ImageTk.PhotoImage(PILImage.open("Images/driver1.png"))
        self.driver_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=driver_icon)
        self.driver_icon_label.image = driver_icon
        self.driver_icon_label.place(x=90, y=415)

        # for payment option
        self.payment_label = Label(self.side_bar_frame, text="Payment", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.payment_label.place(x=130, y=485)
        self.payment_label.bind("<Button-1>", lambda event:self.window_indicator(self.payment_indicator_lbl, self.payment_details_window))

        self.payment_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.payment_indicator_lbl.place(x=80, y=485)

        payment_icon = ImageTk.PhotoImage(PILImage.open("Images/payment1.png"))
        self.payment_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=payment_icon)
        self.payment_icon_label.image = payment_icon
        self.payment_icon_label.place(x=90, y=485)

        # for account Activity
        self.account_activity_label = Label(self.side_bar_frame, text="Activity", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.account_activity_label.place(x=130, y=555)
        self.account_activity_label.bind("<Button-1>", lambda event:self.window_indicator(self.account_indicator_lbl, self.activity_log_window))

        self.account_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.account_indicator_lbl.place(x=80, y=555)

        account_icon = ImageTk.PhotoImage(PILImage.open("Images/login_activity1.png"))
        self.account_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=account_icon)
        self.account_icon_label.image = account_icon
        self.account_icon_label.place(x=90, y=555)

        # for logout option
        self.logout_label = Label(self.side_bar_frame, text="Log Out", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.logout_label.place(x=130, y=625)
        self.logout_label.bind("<Button-1>", self.logout)


        self.logout_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.logout_indicator_lbl.place(x=80, y=625)

        logout_icon = ImageTk.PhotoImage(PILImage.open("Images/logout1.png"))
        self.logout_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=logout_icon)
        self.logout_icon_label.image = logout_icon
        self.logout_icon_label.place(x=90, y=625)

        # creating a main frame in right side
        self.main_frame = Frame(self.window, bg="#1c1c1c", width=1240)
        self.main_frame.pack(side='right',fill = 'y')

    #     creating a inner main frame above the main panel
        self.innner_main_frame = customtkinter.CTkFrame(master=self.main_frame, width=1190, height=710, corner_radius=40)
        self.innner_main_frame.place(x=25, y=20)

        self.inner_top_frame = customtkinter.CTkFrame(master=self.innner_main_frame, width=1135, height=200, corner_radius=40)
        self.inner_top_frame.place(x=30, y=10)

        # simple card like structure to show the total customer, booking and the total driver
        self.total_customer_frame = customtkinter.CTkFrame(master=self.inner_top_frame, corner_radius=30, height=150,
                                                          width=190,cursor="hand2")
        self.total_customer_frame.place(x=100, y=25)
        self.total_customer_frame.bind("<Button-1>", self.customer_records)



        self.customer_number_label = Label(self.total_customer_frame, font=(self.font, 16), text="Total Customer",
                                          bg="#2c2c2c", fg="white")
        self.customer_number_label.place(relx=0.5, rely=0.25, anchor="center")

        self.total_customer_count_label = Label(self.total_customer_frame, font=(self.font, 28), text="", bg="#2c2c2c",
                                               fg="#90EE90")
        self.total_customer_count_label.place(relx=0.5, rely=0.6, anchor="center")

        self.count_customer()

        # ============= FOR TOTAL BOOKING FRAME ==========================
        self.total_booking_frame = customtkinter.CTkFrame(master=self.inner_top_frame, corner_radius=30, height=150,
                                                           width=190)
        self.total_booking_frame.place(x=355, y=25)

        self.bc_line = Canvas(self.inner_top_frame, bg="white", highlightthickness=0, height=3, width=65)
        self.bc_line.place(x= 290, y= 100)

        self.booking_number_label = Label(self.total_booking_frame, font=(self.font, 16), text="Total Booking",
                                           bg="#2c2c2c", fg="white", cursor="hand2")
        self.booking_number_label.place(relx=0.5, rely=0.25, anchor="center")

        self.total_booking_count_label = Label(self.total_booking_frame, font=(self.font, 28), text="10", bg="#2c2c2c",
                                                fg="#90EE90")
        self.total_booking_count_label.place(relx=0.5, rely=0.6, anchor="center")

        self.count_total_booking()

        # ============= FOR TOTAL PENDING BOOKING FRAME ==========================
        self.total_pending_booking_frame = customtkinter.CTkFrame(master=self.inner_top_frame, corner_radius=30, height=150,
                                                          width=190, cursor="hand2")
        self.total_pending_booking_frame.place(x=605, y=25)
        self.total_pending_booking_frame.bind("<Button-1>", self.display_pending_booking_records)


        self.pb_line = Canvas(self.inner_top_frame, bg="white", highlightthickness=0, height=3, width=60)
        self.pb_line.place(x=545, y=100)

        self.pending_booking_number_label = Label(self.total_pending_booking_frame, font=(self.font, 16), text="Pending Booking",
                                          bg="#2c2c2c", fg="white",cursor="hand2")
        self.pending_booking_number_label.place(relx=0.5, rely=0.25, anchor="center")


        self.total_pending_booking_count_label = Label(self.total_pending_booking_frame, font=(self.font, 28), text="", bg="#2c2c2c",
                                               fg="#90EE90")
        self.total_pending_booking_count_label.place(relx=0.5, rely=0.6, anchor="center")

        self.count_pending_booking()


        # ============= FOR TOTAL DRIVER FRAME ==========================
        self.total_driver_frame = customtkinter.CTkFrame(master=self.inner_top_frame, corner_radius=30, height=150,
                                                          width=190)
        self.total_driver_frame.place(x=860, y=25)

        self.dp_line = Canvas(self.inner_top_frame, bg="white", highlightthickness=0, height=3, width=65)
        self.dp_line.place(x=795, y=100)

        self.driver_number_label = Label(self.total_driver_frame, font=(self.font, 16), text="Total Driver",
                                          bg="#2c2c2c", fg="white")
        self.driver_number_label.place(relx=0.5, rely=0.25, anchor="center")

        self.total_driver_count_label = Label(self.total_driver_frame, font=(self.font, 28), text="5", bg="#2c2c2c",
                                               fg="#90EE90")
        self.total_driver_count_label.place(relx=0.5, rely=0.6, anchor="center")

        self.count_driver()

        self.tab_view = customtkinter.CTkTabview(self.innner_main_frame, width=1140, height=470, corner_radius=15, command=self.show_chart)
        self.tab_view.place(x=30, y=220)

        self.table_tab = self.tab_view.add("Bookings")
        self.graph_tab = self.tab_view.add("Graph")

        # to set the currently visible tab
        self.tab_view.set("Bookings")

        #======================== SHOWING THE CONTENT IN THE TABLE TAB VIEW================================

        self.table_tab_frame = customtkinter.CTkFrame(self.table_tab, width=1160, height=460)
        self.table_tab_frame.place(x=0, y=5)

        # ================ FOR THE PENDING BOOKING DETAILS =========================
        pending_label = customtkinter.CTkLabel(self.table_tab_frame, text="Pending Booking Details", font=(self.font, 26))
        pending_label.place(relx=0.5, rely=0.069, anchor="center")

        #  for search entry
        self.search_entry = customtkinter.CTkEntry(master=self.table_tab_frame, width=100, height=36,
                                              placeholder_text="Booking ID")
        self.search_entry.place(x=30, y=20)

        search_btn_image = ImageTk.PhotoImage(PILImage.open("Images/search.png").resize((20, 20), PILImage.ANTIALIAS))

        self.search_button = customtkinter.CTkButton(master=self.table_tab_frame, width=60, height=35, text="search",
                                                corner_radius=15, font=(self.font, 15), image=search_btn_image,
                                                command=self.search_booking)
        self.search_button.place(x=140, y=22)

        self.scroll_y = Scrollbar(self.table_tab_frame, orient=VERTICAL)

        self.pending_booking_table = tkinter.ttk.Treeview(
            self.table_tab_frame,
            columns=("booking_id", "customer_id", "customer_name", "pickup_address", "date", "time", "dropoff_address",
                     "status"),
            show="headings",
            height=9,
            yscrollcommand=self.scroll_y.set
        )

        self.scroll_y.place(x=1120, y=80, height=285)
        self.pending_booking_table.place(x=0, y=80)
        self.pending_booking_table.bind("<ButtonRelease-1>", self.select_booking)


        self.pending_booking_table.heading("booking_id", text="Booking ID", anchor=CENTER)
        self.pending_booking_table.heading("customer_id", text="Customer ID", anchor=CENTER)
        self.pending_booking_table.heading("customer_name", text="Name", anchor=CENTER)
        self.pending_booking_table.heading("pickup_address", text="Pickup Address", anchor=CENTER)
        self.pending_booking_table.heading("date", text="Date", anchor=CENTER)
        self.pending_booking_table.heading("time", text="Time", anchor=CENTER)
        self.pending_booking_table.heading("dropoff_address", text="Dropoff Address", anchor=CENTER)
        self.pending_booking_table.heading("status", text="Status", anchor=CENTER)

        self.pending_booking_table.column("booking_id", width=100, anchor=CENTER)
        self.pending_booking_table.column("customer_id", width=100, anchor=CENTER)
        self.pending_booking_table.column("customer_name", width=150, anchor=CENTER)
        self.pending_booking_table.column("pickup_address", width=250, anchor=CENTER)
        self.pending_booking_table.column("date", width=100, anchor=CENTER)
        self.pending_booking_table.column("time", width=100, anchor=CENTER)
        self.pending_booking_table.column("dropoff_address", width=205, anchor=CENTER)
        self.pending_booking_table.column("status", width=115, anchor=CENTER)

        # ======= CALLING FUNCTION TO SET THE DETAILS IN THE TABLE ==========
        self.display_pending_booking_details()

        # ======= SETTING BUTTONS FOR MORE FUNCTIONALITY ============
        assign_btn_image = ImageTk.PhotoImage(
            PILImage.open("Images/assign_driver.png").resize((30, 30), PILImage.ANTIALIAS))

        self.assign_driver_button = customtkinter.CTkButton(master=self.table_tab_frame, width=150,
                                                            font=(self.font, 18, 'bold'), text="Assign Driver",
                                                            height=35, corner_radius=20, image=assign_btn_image, command=self.assign_driver)
        self.assign_driver_button.place(x=370, y=354)

        cancel_btn_image = ImageTk.PhotoImage(PILImage.open("Images/cancel.png").resize((30, 30), PILImage.ANTIALIAS))

        self.cancel_booking_button = customtkinter.CTkButton(master=self.table_tab_frame, width=150,
                                                             font=(self.font, 18, 'bold'), text="Cancel Booking",
                                                             height=35,
                                                             corner_radius=20, image=cancel_btn_image, command=self.cancel_booking_details)
        self.cancel_booking_button.place(x=570, y=354)


    def show_chart(self):
        # ========================  SHOWING THE CONTENT IN THE GRAPH TAB VIEW  ================================

        self.chart_tab_frame = customtkinter.CTkFrame(self.graph_tab, width=1140, height=460)
        self.chart_tab_frame.place(x=0, y=5)

        # chart_label = customtkinter.CTkLabel(self.chart_tab_frame, text="Daily Booking Records Chart",
        #                                      font=(self.font, 25))
        # chart_label.place(relx=0.5, rely=0.056, anchor="center")

        result = fetch_customer_booking()

        result = [
    ('2023-12-10', 1),
    ('2023-12-18', 18),
    ('2023-12-21', 5),
    ('2023-12-22', 1),
    ('2023-12-29', 5),
    ('2023-12-30', 5),
    ('2024-01-15', 2)
]

        # preparing data for plotting
        dates = []
        bookings = []

        for row in result:
            dates.append(row[0])
            bookings.append(row[1])



        # creating a matplotlib figure
        figure, ax = plt.subplots(figsize=(11.8, 4))
        ax.set_facecolor('#f0f0f0')  # Set the background color of the chart

        # Plotting the line and getting the first element of the returned list
        line, = ax.plot_date(dates, bookings, '-')

        # to set the labels and the title for the chart
        ax.set_xlabel("Date", fontsize=10)
        ax.set_ylabel("Total Bookings", fontsize=12)
        ax.set_title("Daily Booking Records Chart", fontsize = 15)

        # Set font size for the line
        ax.tick_params(axis='both', which='major', labelsize=9)

        # Set the y-axis ticks with a step of 5
        plt.yticks(range(0, max(bookings) + 5, 5))

        # creating a canvas for the Matplotlib figure
        canvas = FigureCanvasTkAgg(figure, master=self.chart_tab_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.place(x=0, y=0)
        canvas.draw()

    # ========= SHOWING THE COUNT DETAILS IN THE ADMIN DASHBOARD =============
    def count_customer(self):
        count = 0
        result = fetch_all_customer()
        for data in result:
            count += 1
        self.total_customer_count_label.config(text=count)

    def count_total_booking(self):
        count = 0
        result = fetch_total_booking()
        for data in result:
            count += 1
        self.total_booking_count_label.config(text=count)

    def count_pending_booking(self):
        count = 0
        result = fetch_pending_booking_details()
        for data in result:
            count +=1
        self.total_pending_booking_count_label.config(text=count)

    def count_driver(self):
        count = 0
        result = fetch_total_driver()
        for data in result:
            count += 1
        self.total_driver_count_label.config(text=count)

    # =========== TO SHOW THE CUSTOMER DETAILS WINDOW ================
    def customer_details_window(self):
        self.destroy_toplevels()

        customerDetails = CustomerDetails(self.main_frame, self.count_customer, self.top_levels)
        customerDetails.show_customer_details_window()

    def driver_details_window(self):
        self.destroy_toplevels()

        driverWindow = DriverWindow(self.main_frame, self.top_levels, self.count_driver)
        driverWindow.show_driver_window()

    def payment_details_window(self):
        self.destroy_toplevels()
        payment_window = PaymentDetails(self.main_frame, self.top_levels)
        payment_window.show_payment_details_window()

    def booking_details_window(self ):
        self.destroy_toplevels()

        bookingDetails = BookingDetails(self.main_frame, self.display_pending_booking_details,self.count_pending_booking, self.top_levels, self.count_total_booking)
        bookingDetails.show_booking_details_window()

    def activity_log_window(self):
        self.destroy_toplevels()

        accountActivity = LoginActivity(self.main_frame, self.top_levels)
        accountActivity.show_login_activity_window()

    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        self.time_label.config(text=current_time)
        self.window.after(1000, self.update_time)

    def hide_indicator(self):
        self.dashboard_indicator_lbl.config(bg="#3c3c3c")
        self.customer_indicator_lbl.config(bg="#3c3c3c")
        self.booking_indicator_lbl.config(bg="#3c3c3c")
        self.payment_indicator_lbl.config(bg="#3c3c3c")
        self.driver_indicator_lbl.config(bg="#3c3c3c")
        self.account_indicator_lbl.config(bg="#3c3c3c")
        self.logout_indicator_lbl.config(bg="#3c3c3c")

    def dashboard_indicator(self, label):
        self.hide_indicator()
        label.config(bg="white")

        self.destroy_toplevels()


    def destroy_toplevels(self):
        for toplevel in self.top_levels:
            toplevel.destroy()


    def window_indicator(self, label, frame):
        self.hide_indicator()
        label.config(bg="white")
        frame()
        # self.customer_details_window()

    def clear_frame(self):
        for widget in self.innner_main_frame.winfo_children():
            widget.destroy()

    def logout(self, event):
        from main_page import MainPage

        confirmed = messagebox.askyesno("Logout", "Do You Want To Logout ?")
        if confirmed:
            self.window.destroy()
            main_dashboard_window = Tk()
            main_dashboard = MainPage(main_dashboard_window)
            main_dashboard_window.mainloop()
    def search_booking(self):
        booking_id = self.search_entry.get()
        if not booking_id == "":
            booking = Booking(booking_id=booking_id)
            result = search_booking_details(booking)

            if len(result) != 0:
                for item in self.pending_booking_table.get_children():
                    self.pending_booking_table.delete(item)

                for row in result:
                     self.pending_booking_table.insert('', END, values=row)
            else:
                messagebox.showerror("Records Not Found", f"Booking with Booking ID {booking_id} doesn't exists.")
        else:
            messagebox.showerror("ERROR", "Please provide Booking ID to search.")

    # ================ TO SET THE PENDING BOOKING DETAILS IN THE ADMIN DASHBOARD ====================
    def display_pending_booking_details(self):
        result = fetch_pending_booking_details()
        self.pending_bookings = result
        if result is not None:
            for item in self.pending_booking_table.get_children():
                self.pending_booking_table.delete(item)

            for row in result:
                self.pending_booking_table.insert('', END, values=row)

    def select_booking(self, event):
        view_info = self.pending_booking_table.focus()
        booking_details = self.pending_booking_table.item(view_info)

        row = booking_details.get("values")

        self.booking_details_id = row[0]
        self.selected_pending_booking_list = row

    def cancel_booking_details(self):

        if len(self.pending_bookings) != 0:
            if not self.booking_details_id == 0:
                confirmed = messagebox.askyesno("Confirm", f"Are you sure you want to cancel the booking of Booking ID {self.booking_details_id}?")
                if confirmed:
                    booking = Booking(booking_id = self.booking_details_id)
                    canceled = cancel_booking(booking)
                    if canceled:
                        messagebox.showinfo("SUCCESS", f"Successfully Canceled Booking of Booking ID {self.booking_details_id}")
                        self.display_pending_booking_details()
                        self.selected_pending_booking_list = None

                        self.booking_details_id = 0

                        self.count_pending_booking()
                        self.count_total_booking()
            else:
                messagebox.showerror("ERROR", "please select booking from the table.")
        else:
            messagebox.showerror("No Pending Bookings", "There is no any pending booking to cancel.")

    def display_pending_booking_records(self, event):
        self.display_pending_booking_details()

    def customer_records(self, event):
        self.customer_details_window()

    def assign_driver(self):
        if len(self.pending_bookings) != 0:
            if self.selected_pending_booking_list is not None:
                self.destroy_toplevels()

                assignDriverPage = AssignDriverPage(self.main_frame, self.selected_pending_booking_list,self.display_pending_booking_details, self.count_pending_booking )
                assignDriverPage.show_assign_driver_window()

            else:
                messagebox.showerror("Unknown Data", "Please select the booking for assigning the Driver!")
        else:
         messagebox.showerror("No Pending Bookings", "There is no any pending booking to assign driver.")


def main_window():
    window = Tk()
    AdminDashboard(window)
    window.mainloop()

if __name__ == '__main__':
    main_window()