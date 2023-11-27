import tkinter.ttk
from tkinter import *
import customtkinter
from PIL import Image as PILImage, ImageTk
from datetime import datetime
from customer_details_admin import CustomerDetails
from booking_details_admin import BookingDetails
from View.login_activity import LoginActivity
from driver_frame_admin import DriverWindow
from tkinter import messagebox

from Controller.customer_dbms import fetch_all_customer

class AdminDashboard:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.title("Customer Dashboard")
        self.window.state("zoomed")
        self.window.resizable(0, 0)

        self.font = "Century Gothic"

        customtkinter.set_default_color_theme("green")


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
        # self.myprofile_label.bind('<Button-1>', lambda event:self.indicator(self.profile_indicator_lbl, self.my_profile_frame))

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
        # self.payment_label.bind("<Button-1>", lambda event:self.indicator(self.payment_indicator_lbl, self.payment_frame))

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
        self.inner_top_frame.place(x=30, y=20)

        # simple card like structure to show the total customer, booking and the total driver
        self.total_customer_frame = customtkinter.CTkFrame(master=self.inner_top_frame, corner_radius=30, height=150,
                                                          width=190)
        self.total_customer_frame.place(x=100, y=25)

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
                                           bg="#2c2c2c", fg="white")
        self.booking_number_label.place(relx=0.5, rely=0.25, anchor="center")

        self.total_booking_count_label = Label(self.total_booking_frame, font=(self.font, 28), text="10", bg="#2c2c2c",
                                                fg="#90EE90")
        self.total_booking_count_label.place(relx=0.5, rely=0.6, anchor="center")

        # ============= FOR TOTAL PENDING BOOKING FRAME ==========================
        self.total_pending_booking_frame = customtkinter.CTkFrame(master=self.inner_top_frame, corner_radius=30, height=150,
                                                          width=190)
        self.total_pending_booking_frame.place(x=605, y=25)

        self.pb_line = Canvas(self.inner_top_frame, bg="white", highlightthickness=0, height=3, width=60)
        self.pb_line.place(x=545, y=100)

        self.pending_booking_number_label = Label(self.total_pending_booking_frame, font=(self.font, 16), text="Pending Booking",
                                          bg="#2c2c2c", fg="white")
        self.pending_booking_number_label.place(relx=0.5, rely=0.25, anchor="center")

        self.total_pending_booking_count_label = Label(self.total_pending_booking_frame, font=(self.font, 28), text="10", bg="#2c2c2c",
                                               fg="#90EE90")
        self.total_pending_booking_count_label.place(relx=0.5, rely=0.6, anchor="center")

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


    # ================ FOR THE PENDING BOOKING DETAILS =========================
        pending_label = Label(self.innner_main_frame, text="Pending Booking Details",font=(self.font, 20), fg="white",bg="#2c2c2c")
        pending_label.place(x=440, y=240)

    #  for search entry
        search_entry = customtkinter.CTkEntry(master=self.innner_main_frame, width=150, height=36, placeholder_text="Booking ID")
        search_entry.place(x=30, y=270)

        search_btn_image = ImageTk.PhotoImage(PILImage.open("Images/search.png").resize((25,25), PILImage.ANTIALIAS))


        search_button = customtkinter.CTkButton(master=self.innner_main_frame, width=80, height=35, text="search", corner_radius=15,font=(self.font, 16), image=search_btn_image)
        search_button.place(x=190, y=272)


        # CREATING A FRAME TO SHOW THE TABLE
        self.table_frame = Frame(self.innner_main_frame, bg="white", width=1140, height=300)
        self.table_frame.place(x=30, y= 330)

        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)

        self.pending_booking_table = tkinter.ttk.Treeview(
            self.table_frame,
            columns=("booking_id", "customer_id", "customer_name", "pickup_address", "date", "time", "dropoff_address",
                     "status"),
            show="headings",
            height=14,
            yscrollcommand=self.scroll_y.set
        )

        self.scroll_y.place(x=1120, y=0, height=300)
        self.pending_booking_table.place(x=0, y=0)

        self.pending_booking_table.heading("booking_id", text="Booking ID", anchor=CENTER)
        self.pending_booking_table.heading("customer_id", text="Customer ID", anchor=CENTER)
        self.pending_booking_table.heading("customer_name", text="Name ID", anchor=CENTER)
        self.pending_booking_table.heading("pickup_address", text="Pickup Address", anchor=CENTER)
        self.pending_booking_table.heading("date", text="Date", anchor=CENTER)
        self.pending_booking_table.heading("time", text="Time", anchor=CENTER)
        self.pending_booking_table.heading("dropoff_address", text="Dropoff Address", anchor=CENTER)
        self.pending_booking_table.heading("status", text="Status", anchor=CENTER)


        self.pending_booking_table.column("booking_id",width=100, anchor=CENTER)
        self.pending_booking_table.column("customer_id",width=100, anchor=CENTER)
        self.pending_booking_table.column("customer_name", width=150, anchor=CENTER)
        self.pending_booking_table.column("pickup_address",width=250, anchor=CENTER)
        self.pending_booking_table.column("date",width=100, anchor=CENTER)
        self.pending_booking_table.column("time",width=100, anchor=CENTER)
        self.pending_booking_table.column("dropoff_address",width=205, anchor=CENTER)
        self.pending_booking_table.column("status",width=115, anchor=CENTER)

        # ======= SETTING BUTTONS FOR MORE FUNCTIONALITY ============
        assign_btn_image = ImageTk.PhotoImage(PILImage.open("Images/assign_driver.png").resize((30,30), PILImage.ANTIALIAS))


        self.assign_driver_button = customtkinter.CTkButton(master = self.innner_main_frame, width=160,font=(self.font, 18,'bold'),text="Assign Driver", height=36, corner_radius=20, image=assign_btn_image)
        self.assign_driver_button.place(x=400 , y=655 )


        cancel_btn_image = ImageTk.PhotoImage(PILImage.open("Images/cancel.png").resize((30,30), PILImage.ANTIALIAS))


        self.cancel_booking_button = customtkinter.CTkButton(master=self.innner_main_frame, width=160,
                                                            font=(self.font, 18, 'bold'), text="Cancel Booking", height=36,
                                                            corner_radius=20, image=cancel_btn_image)
        self.cancel_booking_button.place(x=600, y=655)

    # ========= SHOWING THE COUNT DETAILS IN THE ADMIN DASHBOARD =============
    def count_customer(self):
        count = 0
        result = fetch_all_customer()
        for data in result:
            count += 1
        self.total_customer_count_label.config(text=count)

    def count_total_booking(self):
        pass

    def count_pending_booking(self):
        pass

    def count_driver(self):
        pass

    # =========== TO SHOW THE CUSTOMER DETAILS WINDOW ================
    def customer_details_window(self):
        customerDetails = CustomerDetails(self.main_frame)
        customerDetails.show_customer_details_window()

    def driver_details_window(self):
        driverWindow = DriverWindow(self.main_frame)
        driverWindow.show_driver_window()

    def booking_details_window(self):
        bookingDetails = BookingDetails(self.main_frame)
        bookingDetails.show_booking_details_window()

    def activity_log_window(self):
        accountActivity = LoginActivity(self.main_frame)
        accountActivity.show_login_activity_window()

    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        self.time_label.config(text=current_time)
        self.window.after(1000, self.update_time)

    def hide_indicator(self):
        self.dashboard_indicator_lbl.config(bg="#3c3c3c")
        self.booking_indicator_lbl.config(bg="#3c3c3c")
        self.payment_indicator_lbl.config(bg="#3c3c3c")
        self.driver_indicator_lbl.config(bg="#3c3c3c")
        self.account_indicator_lbl.config(bg="#3c3c3c")
        self.logout_indicator_lbl.config(bg="#3c3c3c")

    def indicator(self, label, frame):
        self.hide_indicator()
        label.config(bg="white")
        self.clear_frame()
        frame()

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

def main_window():
    window = Tk()
    AdminDashboard(window)
    window.mainloop()

if __name__ == '__main__':
    main_window()