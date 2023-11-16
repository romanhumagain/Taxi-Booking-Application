from tkinter import *
import customtkinter
from PIL import Image as PILImage, ImageTk
from datetime import datetime
from tkinter import simpledialog

from booking_frame import *
from driver_frame import *
from payment_frame import *
from login_activity_frame import *
from update_profile import *
from change_password import *

from tkinter import messagebox



class CustomerDashboard:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.title("Customer Dashboard")
        self.window.state("zoomed")
        self.window.resizable(0, 0)

        self.font = "Century Gothic"

        customtkinter.set_appearance_mode("System")
        # customtkinter.set_default_color_theme("green")

        self.navbar = Frame(self.window, bg="#2c2c2c", pady=25)
        self.navbar.pack(side="top", fill="x")

        self.taxi_logo = PILImage.open("Images/taxi.png")
        photo = ImageTk.PhotoImage(self.taxi_logo)

        self.taxi_logo_label = Label(self.navbar, image=photo, bg='#2c2c2c')
        self.taxi_logo_label.image = photo
        self.taxi_logo_label.place(x=20, y=0)

        self.slogan_label = Label(self.navbar, text="Taxi Booking System",
                                  fg='white', bg='#2c2c2c', font=(self.font, 30))
        self.slogan_label.pack()

        # ===== creating a side bar =====
        self.side_bar_frame = Frame(self.window, bg="#3c3c3c", width=300)
        self.side_bar_frame.pack(side='left',fill = 'y' )

        # for clock image
        clock_image = ImageTk.PhotoImage(PILImage.open("Images/clock.png"))
        self.clock_image_label = Label(self.side_bar_frame, image=clock_image, bg='#3c3c3c', justify=CENTER)
        self.clock_image_label.image = clock_image
        self.clock_image_label.place(x=90, y=20)

        # for the time label
        self.time_label = Label(self.side_bar_frame, font=(self.font, 15), bg='#3c3c3c', fg='white')
        self.time_label.place(x=40, y=130)

        self.update_time()

        # creating line
        self.line = Canvas(self.side_bar_frame, width=300, height=1)
        self.line.place(x=0, y=170)

        # for the option in the side_bar_frame

        # for profile option
        self.myprofile_label = Label(self.side_bar_frame, text = "Profile",font=(self.font, 17), fg='white', bg='#3c3c3c', cursor='hand2')
        self.myprofile_label.place(x=125, y=205)
        self.myprofile_label.bind('<Button-1>', lambda event:self.indicator(self.profile_indicator_lbl, self.my_profile_frame))

        self.profile_indicator_lbl = Label(self.side_bar_frame, bg="white", width=0, height=2)
        self.profile_indicator_lbl.place(x=80, y=205)

        # to show the icon image
        profile_icon = ImageTk.PhotoImage(PILImage.open("Images/profile.png"))
        self.profile_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=profile_icon)
        self.profile_icon_label.image = profile_icon
        self.profile_icon_label.place(x=90, y=205)



        # for booking option
        self.booking_label = Label(self.side_bar_frame, text="Booking", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.booking_label.place(x=125, y=285)
        self.booking_label.bind("<Button-1>", lambda event:self.indicator(self.booking_indicator_lbl, self.booking_frame))

        self.booking_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.booking_indicator_lbl.place(x=80, y=285)

        booking_icon = ImageTk.PhotoImage(PILImage.open("Images/booking.png"))
        self.booking_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=booking_icon)
        self.booking_icon_label.image = booking_icon
        self.booking_icon_label.place(x=90, y=285)

        # for driver option
        self.driver_label = Label(self.side_bar_frame, text="Driver", font=(self.font, 17), fg='white', bg='#3c3c3c', cursor='hand2')
        self.driver_label.place(x=125, y=365)
        self.driver_label.bind("<Button-1>", lambda event:self.indicator(self.driver_indicator_lbl, self.driver_frame))

        self.driver_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.driver_indicator_lbl.place(x=80, y=365)

        driver_icon = ImageTk.PhotoImage(PILImage.open("Images/driver.png"))
        self.driver_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=driver_icon)
        self.driver_icon_label.image = driver_icon
        self.driver_icon_label.place(x=90, y=365)

        # for payment option
        self.payment_label = Label(self.side_bar_frame, text="Payment", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.payment_label.place(x=125, y=445)
        self.payment_label.bind("<Button-1>", lambda event:self.indicator(self.payment_indicator_lbl, self.payment_frame))

        self.payment_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.payment_indicator_lbl.place(x=80, y=445)

        payment_icon = ImageTk.PhotoImage(PILImage.open("Images/payment.png"))
        self.payment_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=payment_icon)
        self.payment_icon_label.image = payment_icon
        self.payment_icon_label.place(x=90, y=445)

        # for account Activity
        self.account_activity_label = Label(self.side_bar_frame, text="Activity", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.account_activity_label.place(x=125, y=525)
        self.account_activity_label.bind("<Button-1>", lambda event:self.indicator(self.account_indicator_lbl, self.login_activity_frame))

        self.account_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.account_indicator_lbl.place(x=80, y=525)

        account_icon = ImageTk.PhotoImage(PILImage.open("Images/login_activity.png"))
        self.account_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=account_icon)
        self.account_icon_label.image = account_icon
        self.account_icon_label.place(x=90, y=525)

        # for logout option
        self.logout_label = Label(self.side_bar_frame, text="Log Out", font=(self.font, 17), fg='white',bg='#3c3c3c', cursor='hand2')
        self.logout_label.place(x=125, y=605)
        self.logout_label.bind("<Button-1>", self.logout)


        self.logout_indicator_lbl = Label(self.side_bar_frame, bg="#3c3c3c", width=0, height=2)
        self.logout_indicator_lbl.place(x=80, y=605)

        logout_icon = ImageTk.PhotoImage(PILImage.open("Images/logout.png"))
        self.logout_icon_label = Label(self.side_bar_frame, bg='#3c3c3c', image=logout_icon)
        self.logout_icon_label.image = logout_icon
        self.logout_icon_label.place(x=90, y=605)

        # creating a main frame in right side
        self.main_frame = Frame(self.window, bg="black", width=1240)
        self.main_frame.pack(side='right',fill = 'y')

        self.main_bg_frame = PILImage.open("Images/login_background.jpg")
        photo = ImageTk.PhotoImage(self.main_bg_frame)

        self.main_panel = Label(self.main_frame, image=photo)
        self.main_panel.image = photo
        self.main_panel.pack(fill="both", expand="yes")

    #     creating a inner main frame above the main panel
        self.innner_main_frame = Frame(self.main_panel, bg='black', width=850, height=600)
        self.innner_main_frame.place(x=190, y=50)

        self.my_profile_frame()

    def my_profile_frame(self):
        self.profile_frame = Frame(self.innner_main_frame, bg="black", width=850, height=600)
        self.profile_frame.place(x=0, y=0)

    # to place the profile icon image
        photo = ImageTk.PhotoImage(PILImage.open("Images/user_profile1.png"))

        self.user_profile_image_label = Label(self.profile_frame, image=photo, bg='black')
        self.user_profile_image_label.image = photo
        self.user_profile_image_label.place(relx=0.5, rely=0.14, anchor='center')

    # to show the Customer Name
        self.user_name = Label(self.profile_frame, text="Roman Humagain", font=(self.font, 22), fg='white', bg='black')
        self.user_name.place(relx=0.5, rely=0.26, anchor = 'center')

    #  simple card to show the total booking number
        self.total_booking_frame = customtkinter.CTkFrame(master = self.profile_frame,  corner_radius=30, height=90, width=190)
        self.total_booking_frame.place(x=230, y=200)

        self.booking_number_label = Label(self.total_booking_frame, font=(self.font, 14), text="Total Booking", bg="#2c2c2c", fg="white")
        self.booking_number_label.place(relx=0.5, rely=0.25, anchor = "center")

        self.booking_count_label = Label(self.total_booking_frame, font=(self.font, 20), text="0", bg="#2c2c2c", fg="#90EE90")
        self.booking_count_label.place(relx=0.5, rely=0.6, anchor = "center")


        #  simple card to show the total requested booking number
        self.booking_requested_frame = customtkinter.CTkFrame(master=self.profile_frame, corner_radius=30, height=90,
                                                          width=190)
        self.booking_requested_frame.place(x=450, y=200)

        self.booking_requested_label = Label(self.booking_requested_frame, font=(self.font, 14), text="Pending Booking",bg="#2c2c2c", fg="white")
        self.booking_requested_label.place(x=10, y=10)

        self.booking_count_label = Label(self.booking_requested_frame, font=(self.font, 20), text="0", bg="#2c2c2c",fg="#90EE90")
        self.booking_count_label.place(relx=0.5, rely=0.6, anchor="center")

    #     to show the personal information
        self.email_label = Label(self.profile_frame, font=(self.font, 9), text="Email", bg="black", fg="white")
        self.email_label.place(x=110, y=325)

        self.user_email_label = Label(self.profile_frame, text="romanhumagain@gmail.com", fg="white", bg="black", font=(self.font, 12))
        self.user_email_label.place(x=110, y=350)

        self.email_line = Canvas(self.profile_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.email_line.place(x=112, y=375, width=230)


        self.mobile_label = Label(self.profile_frame, font=(self.font, 9), text="Phone No", bg="black", fg="white")
        self.mobile_label.place(x=375, y=325)

        self.user_mobile_label = Label(self.profile_frame, text="+977 9840617106", fg="white", bg="black",font=(self.font, 12))
        self.user_mobile_label.place(x=375, y=350)

        self.mobile_line = Canvas(self.profile_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.mobile_line.place(x=377, y=375, width=135)

        self.address_label = Label(self.profile_frame, font=(self.font, 9), text="Address", bg="black", fg="white")
        self.address_label.place(x=565, y=325)

        self.user_address_label = Label(self.profile_frame, text="Panauti, Kavre", fg="white", bg="black",font=(self.font, 12))
        self.user_address_label.place(x=565, y=350)

        self.address_line = Canvas(self.profile_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.address_line.place(x=567, y=375, width=145)

        self.gender_label = Label(self.profile_frame, font=(self.font, 9), text="Gender", bg="black", fg="white")
        self.gender_label.place(x=110, y=420)

        self.user_gender_label = Label(self.profile_frame, text="Male", fg="white", bg="black", font=(self.font, 12))
        self.user_gender_label.place(x=110, y=445)

        self.gender_line = Canvas(self.profile_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.gender_line.place(x=112, y=475, width=90)

        self.dob_label = Label(self.profile_frame, font=(self.font, 9), text="D.O.B", bg="black", fg="white")
        self.dob_label.place(x=375, y=420)

        self.user_dob_label = Label(self.profile_frame, text="2003-03-29", fg="white", bg="black", font=(self.font, 12))
        self.user_dob_label.place(x=375, y=445)

        self.dob_line = Canvas(self.profile_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.dob_line.place(x=377, y=475, width=135)

        self.payment_label = Label(self.profile_frame, font=(self.font, 9), text="Payment Method", bg="black", fg="white")
        self.payment_label.place(x=565, y=420)

        self.user_payment_label = Label(self.profile_frame, text="Online", fg="white", bg="black", font=(self.font, 12))
        self.user_payment_label.place(x=565, y=445)

        self.payment_line = Canvas(self.profile_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.payment_line.place(x=567, y=475, width=145)

    #     to show the button for more functionality of the application
        self.update_button = customtkinter.CTkButton(master = self.profile_frame, text="Update Profile", font=(self.font, 15), corner_radius=8,height=30, command=self.update_profile)
        self.update_button.place(x=90, y=550)

        self.delete_button = customtkinter.CTkButton(master=self.profile_frame, text="Delete Profile",font=(self.font, 15), corner_radius=8,  height=30, command=self.delete_account)
        self.delete_button.place(x=260, y=550)

        self.change_password_button = customtkinter.CTkButton(master=self.profile_frame, text="Change Password",font=(self.font, 15), corner_radius=8,height=30, command=self.change_password)
        self.change_password_button.place(x=430, y=550)

        self.login_info_button = customtkinter.CTkButton(master=self.profile_frame, text="Login Info", font=(self.font, 15), corner_radius=8,height=30)
        self.login_info_button.place(x=610, y=550)

    def update_profile(self):
        updateProfile = UpdateProfile(self.profile_frame)
        updateProfile.show_update_profile_window()

    def change_password(self):
        changePasword = ChangePassword(self.profile_frame)
        changePasword.show_change_password_window()

    def delete_account(self):
        user_input = simpledialog.askstring("Confirm Deletion",
                                            "Are you sure you want to delete your account?\n\nType 'CONFIRMDELETE' and press OK to confirm.")

        if user_input == 'CONFIRMDELETE':
            print("Account deletion confirmed.")
        else:
            print("Account deletion canceled or confirmation failed.")
    def booking_frame(self):
        # to show the booking frame inside inner_main_frame
        booking_frame = BookingFrame(self.innner_main_frame)
        booking_frame.place(x=0, y=0)

    def driver_frame(self):
        driver_frame = DriverFrame(self.innner_main_frame)
        driver_frame.place(x=0, y=0)

    def payment_frame(self):
        payment_frame = PaymentFrame(self.innner_main_frame)
        payment_frame.place(x=0, y=0)

    def login_activity_frame(self):
        login_activity_frame = LoginActivityFrame(self.innner_main_frame)
        login_activity_frame.place(x=0, y=0)

    def update_time(self):
        current_time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        self.time_label.config(text=current_time)
        self.window.after(1000, self.update_time)

    def hide_indicator(self):
        self.profile_indicator_lbl.config(bg="#3c3c3c")
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
    CustomerDashboard(window)
    window.mainloop()

if __name__ == '__main__':
    main_window()