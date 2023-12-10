import tkinter.ttk
from tkinter import *
from tkinter import messagebox

import customtkinter
from PIL import Image as PILImage, ImageTk
from datetime import datetime

from Controller.driver_dashboard_dbms import fetch_assigned_booking
from Model import Global
from Model.driver import Driver
from View.login_activity import LoginActivity


class DriverDashboard:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.title("Driver Dashboard")
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

        self.navbar = Frame(self.window, bg="#2c2c2c", pady=25)
        self.navbar.pack(side="top", fill="x")

        self.taxi_logo = PILImage.open("Images/taxi.png")
        photo = ImageTk.PhotoImage(self.taxi_logo)

        self.taxi_logo_label = Label(self.navbar, image=photo, bg='#2c2c2c')
        self.taxi_logo_label.image = photo
        self.taxi_logo_label.place(x=20, y=0)

        self.slogan_label = Label(self.navbar, text="Taxi Booking System",
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
        self.dashboard_label.place(x=130, y=225)
        self.dashboard_label.bind('<Button-1>', lambda event:self.dashboard_indicator(self.dashboard_indicator_lbl))

        self.dashboard_indicator_lbl = Label(self.side_bar_frame, bg="white", width=0, height=2)
        self.dashboard_indicator_lbl.place(x=80, y=225)

        # to show the icon image
        dashboard_icon = ImageTk.PhotoImage(PILImage.open("Images/booking1.png"))
        self.dashboard_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=dashboard_icon)
        self.dashboard_icon_label.image = dashboard_icon
        self.dashboard_icon_label.place(x=90, y=225)

        # for booking option
        self.profile_label = Label(self.side_bar_frame, text="Profile", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.profile_label.place(x=130, y=305)
        self.profile_label.bind("<Button-1>",self.show_driver_profile)

        self.profile_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.profile_indicator_lbl.place(x=80, y=305)

        profile_icon = ImageTk.PhotoImage(PILImage.open("Images/profile1.png").resize((28, 28), PILImage.ANTIALIAS))
        self.profile_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=profile_icon)
        self.profile_icon_label.image = profile_icon
        self.profile_icon_label.place(x=90, y=305)

        self.heading_profile_label = Label(self.navbar, bg='#2c2c2c', image=profile_icon)
        self.heading_profile_label.image = profile_icon
        self.heading_profile_label.place(x=1280, y=8)

        self.profle_name = Label(self.navbar, bg='#2c2c2c', text="", font=(self.font, 13), fg="white")
        self.profle_name.place(x=1320, y=10)
        self.profle_name.configure(text=Global.logged_in_driver[1])

        # for booking option
        self.trip_label = Label(self.side_bar_frame, text="Trip", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.trip_label.place(x=130, y=385)
        self.trip_label.bind("<Button-1>", lambda event:self.window_indicator(self.booking_indicator_lbl, self.booking_details_window))

        self.trip_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.trip_indicator_lbl.place(x=80, y=385)

        trip_icon = ImageTk.PhotoImage(PILImage.open("Images/booking1.png"))
        self.trip_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=trip_icon)
        self.trip_icon_label.image = trip_icon
        self.trip_icon_label.place(x=90, y=385)

        # for account Activity
        self.account_activity_label = Label(self.side_bar_frame, text="Activity", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.account_activity_label.place(x=130, y=465)
        self.account_activity_label.bind("<Button-1>", self.show_activity_window)

        self.account_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.account_indicator_lbl.place(x=80, y=465)

        account_icon = ImageTk.PhotoImage(PILImage.open("Images/login_activity1.png"))
        self.account_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=account_icon)
        self.account_icon_label.image = account_icon
        self.account_icon_label.place(x=90, y=465)

        # for logout option
        self.logout_label = Label(self.side_bar_frame, text="Log Out", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.logout_label.place(x=130, y=545)
        self.logout_label.bind("<Button-1>", self.logout)


        self.logout_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.logout_indicator_lbl.place(x=80, y=545)

        logout_icon = ImageTk.PhotoImage(PILImage.open("Images/logout1.png"))
        self.logout_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=logout_icon)
        self.logout_icon_label.image = logout_icon
        self.logout_icon_label.place(x=90, y=545)

        # creating a main frame in right side
        self.main_frame = Frame(self.window, bg="#1c1c1c", width=1240)
        self.main_frame.pack(side='right',fill = 'y')

    #     creating a inner main frame above the main panel
        self.innner_main_frame = customtkinter.CTkFrame(master=self.main_frame, width=1190, height=710, corner_radius=40)
        self.innner_main_frame.place(x=25, y=20)

        self.inner_top_frame = customtkinter.CTkFrame(master=self.innner_main_frame, width=1135, height=200, corner_radius=40)
        self.inner_top_frame.place(x=30, y=10)

        self.status_icon = customtkinter.CTkImage(light_image= PILImage.open("Images/booked_s.png"), dark_image=PILImage.open("Images/booked_s.png"),)

        self.status_icon_label = customtkinter.CTkLabel(self.innner_main_frame, text = "", image=self.status_icon)
        self.status_icon_label.image = self.status_icon
        self.status_icon_label.place(x=950, y=225)

        self.status_label = customtkinter.CTkLabel(self.innner_main_frame, text = "You're Now Booked! ", font=(self.font, 16))
        self.status_label.place(x=980, y=225)


        # simple card like structure to show the total customer, booking and the total driver
        self.total_riding_frame = customtkinter.CTkFrame(master=self.inner_top_frame, corner_radius=30, height=150,
                                                          width=190,cursor="hand2")
        self.total_riding_frame.place(x=200, y=25)
        # self.total_customer_frame.bind("<Button-1>", self.customer_records)



        self.riding_number_label = Label(self.total_riding_frame, font=(self.font, 16), text="Total Riding",
                                          bg="#2c2c2c", fg="white")
        self.riding_number_label.place(relx=0.5, rely=0.25, anchor="center")

        self.total_riding_count_label = Label(self.total_riding_frame, font=(self.font, 28), text="", bg="#2c2c2c",
                                               fg="#90EE90")
        self.total_riding_count_label.place(relx=0.5, rely=0.6, anchor="center")


        # ============= FOR TOTAL BOOKING FRAME ==========================
        self.total_assigned_frame = customtkinter.CTkFrame(master=self.inner_top_frame, corner_radius=30, height=150,
                                                           width=190)
        self.total_assigned_frame.place(x=455, y=25)

        self.bc_line = Canvas(self.inner_top_frame, bg="white", highlightthickness=0, height=3, width=65)
        self.bc_line.place(x= 390, y= 100)

        self.assigned_number_label = Label(self.total_assigned_frame, font=(self.font, 16), text="Assigned Riding",
                                           bg="#2c2c2c", fg="white", cursor="hand2")
        self.assigned_number_label.place(relx=0.5, rely=0.25, anchor="center")

        self.total_assigned_count_label = Label(self.total_assigned_frame, font=(self.font, 28), text="10", bg="#2c2c2c",
                                                fg="#90EE90")
        self.total_assigned_count_label.place(relx=0.5, rely=0.6, anchor="center")

        # ============= FOR TOTAL PENDING BOOKING FRAME ==========================
        self.total_completed_booking_frame = customtkinter.CTkFrame(master=self.inner_top_frame, corner_radius=30, height=150,
                                                          width=190, cursor="hand2")
        self.total_completed_booking_frame.place(x=705, y=25)
        # self.total_pending_booking_frame.bind("<Button-1>", self.display_pending_booking_records)


        self.pb_line = Canvas(self.inner_top_frame, bg="white", highlightthickness=0, height=3, width=60)
        self.pb_line.place(x=645, y=100)

        self.completed_booking_number_label = Label(self.total_completed_booking_frame, font=(self.font, 16), text="Completed Trip",
                                          bg="#2c2c2c", fg="white",cursor="hand2")
        self.completed_booking_number_label.place(relx=0.5, rely=0.25, anchor="center")


        self.total_completed_booking_count_label = Label(self.total_completed_booking_frame, font=(self.font, 28), text="", bg="#2c2c2c",
                                               fg="#90EE90")
        self.total_completed_booking_count_label.place(relx=0.5, rely=0.6, anchor="center")

        self.tab_view = customtkinter.CTkTabview(self.innner_main_frame, width=1140, height=430, corner_radius=15)
        self.tab_view.place(x=30, y=260)

        self.assigned_tab = self.tab_view.add("Assigned")
        self.complete_tab = self.tab_view.add("Complete Trip")

        # to set the currently visible tab
        self.tab_view.set("Assigned")

        # ======================== SHOWING THE CONTENT IN THE TABLE TAB VIEW================================

        self.assigned_tab_frame = customtkinter.CTkFrame(self.assigned_tab, width=1160, height=460)
        self.assigned_tab_frame.place(x=0, y=5)

        assigned_label = customtkinter.CTkLabel(self.assigned_tab_frame, text="Your Assigned Booking Details",
                                               font=(self.font, 26))
        assigned_label.place(relx=0.5, rely=0.069, anchor="center")

        self.scroll_y = Scrollbar(self.assigned_tab_frame, orient=VERTICAL)

        self.assigned_booking_table = tkinter.ttk.Treeview(
            self.assigned_tab_frame,
            columns=("booking_id", "customer_id", "customer_name", "pickup_address", "date", "time", "dropoff_address",
                     "status"),
            show="headings",
            height=10,
            yscrollcommand=self.scroll_y.set
        )

        self.scroll_y.place(x=1120, y=80, height=285)
        self.assigned_booking_table.place(x=0, y=80)
        # self.assigned_booking_table.bind("<ButtonRelease-1>", self.select_booking)

        self.assigned_booking_table.heading("booking_id", text="Booking ID", anchor=CENTER)
        self.assigned_booking_table.heading("customer_id", text="Customer ID", anchor=CENTER)
        self.assigned_booking_table.heading("customer_name", text="Name", anchor=CENTER)
        self.assigned_booking_table.heading("pickup_address", text="Pickup Address", anchor=CENTER)
        self.assigned_booking_table.heading("date", text="Date", anchor=CENTER)
        self.assigned_booking_table.heading("time", text="Time", anchor=CENTER)
        self.assigned_booking_table.heading("dropoff_address", text="Dropoff Address", anchor=CENTER)
        self.assigned_booking_table.heading("status", text="Status", anchor=CENTER)

        self.assigned_booking_table.column("booking_id", width=100, anchor=CENTER)
        self.assigned_booking_table.column("customer_id", width=100, anchor=CENTER)
        self.assigned_booking_table.column("customer_name", width=150, anchor=CENTER)
        self.assigned_booking_table.column("pickup_address", width=250, anchor=CENTER)
        self.assigned_booking_table.column("date", width=100, anchor=CENTER)
        self.assigned_booking_table.column("time", width=100, anchor=CENTER)
        self.assigned_booking_table.column("dropoff_address", width=205, anchor=CENTER)
        self.assigned_booking_table.column("status", width=115, anchor=CENTER)

        self.display_assigned_booking()


    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        self.time_label.config(text=current_time)
        self.window.after(1000, self.update_time)

    def show_driver_profile(self, event):
        from View.driver_profile import DriverProfile

        driverProfile = DriverProfile(self.window )
        driverProfile.show_driver_profile()

    def show_activity_window(self, event):
        activityWindow = LoginActivity(self.window)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        activityWindow.show_login_activity_window()

        # x_position = (screen_width - 900) // 2 + 142
        # y_position = (screen_height - 580) // 2 -20
        # activityWindow.login_activity_window.geometry(f"{900}x{580}+{x_position}+{y_position}")

    def logout(self, event):
        from main_page import MainPage

        confirmed = messagebox.askyesno("Logout", "Do You Want To Logout ?")
        if confirmed:
            self.window.destroy()
            main_dashboard_window = Tk()
            main_dashboard = MainPage(main_dashboard_window)
            main_dashboard_window.mainloop()

    def dashboard_indicator(self, dashboard_indicator_lbl):
        pass

    def window_indicator(self, customer_indicator_lbl, customer_details_window):
        pass

    def display_assigned_booking(self):
        if Global.logged_in_driver is not None:
            driver_id = Global.logged_in_driver[0]
            driver = Driver(driver_id = driver_id)

            result = fetch_assigned_booking(driver)
            if result is not None:

                for item in self.assigned_booking_table.get_children():
                    self.assigned_booking_table.delete(item)

                for row in result:
                    self.assigned_booking_table.insert('', END, values=row)






if __name__ == '__main__':
    window = Tk()
    driverDashboard = DriverDashboard(window)
    window.mainloop()