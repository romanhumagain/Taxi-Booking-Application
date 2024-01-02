import re
from datetime import datetime
from tkinter import *
from tkinter import messagebox

import customtkinter
from PIL import Image, ImageTk
import tkinter.messagebox

from tkcalendar import DateEntry

from Controller.account_activity_dbms import insert_account_activity_details
from Controller.user_dbms import change_user_password
from Model import Global
from Model.account_activity import AccountActivity
from Model.user import User
from Model.driver import Driver
from View.main_page import MainPage
from Controller.driver_dashboard_dbms import update_driver_profile, get_profile_details


class DriverProfile:
    def __init__(self, window, profle_name, top_level_list=None, dashboard_indicator=None):
        self.window = window
        self.profle_name = profle_name
        self.font = "Century Gothic"
        if top_level_list is None:
            self.top_level_list = []
        self.top_level_list = top_level_list
        self.dashboard_indicator = dashboard_indicator

    def show_driver_profile(self):
        self.driver_profile_window = Toplevel(self.window, width=720, height=460, bg="#2c2c2c")
        self.driver_profile_window.title("Driver Profile")
        self.driver_profile_window.resizable(0, 0)

        self.top_level_list.append(self.driver_profile_window)
        # Configure the window close event to call the on_closing function
        self.driver_profile_window.protocol("WM_DELETE_WINDOW", self.on_closing)

        screen_width = self.driver_profile_window.winfo_screenwidth()
        screen_height = self.driver_profile_window.winfo_screenheight()

        window_width = 720
        window_height = 460

        x_position = (screen_width - window_width) // 2 + 100
        y_position = (screen_height - window_height) // 2 + 20

        self.driver_profile_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.profile_frame = Frame(self.driver_profile_window, bg="#222222", width=720, height=460)
        self.profile_frame.place(x=0, y=0)

        # to place the profile icon image
        photo = ImageTk.PhotoImage(Image.open("Images/driver_user.png").resize((75, 75), Image.ANTIALIAS))

        self.user_profile_image_label = Label(self.profile_frame, image=photo, bg='#222222')
        self.user_profile_image_label.image = photo
        self.user_profile_image_label.place(relx=0.5, rely=0.12, anchor='center')

        # to show the Customer Name
        self.user_name = Label(self.profile_frame, text="", font=(self.font, 22), fg='white', bg='#222222')
        self.user_name.place(relx=0.5, rely=0.26, anchor='center')

        #   to show the personal information

        self.details_frame = customtkinter.CTkFrame(self.profile_frame, width=680, height=200, corner_radius=20)
        self.details_frame.place(x=20, y=170)

        self.email_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Email")
        self.email_label.place(x=40, y=20)

        self.driver_email_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.driver_email_label.place(x=40, y=45)

        self.email_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.email_line.place(x=40, y=70, width=225)

        self.mobile_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Phone No")
        self.mobile_label.place(x=320, y=20)

        self.driver_mobile_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.driver_mobile_label.place(x=320, y=45)

        self.mobile_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.mobile_line.place(x=322, y=70, width=135)

        self.address_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Address")
        self.address_label.place(x=520, y=20)

        self.driver_address_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.driver_address_label.place(x=520, y=45)

        self.address_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.address_line.place(x=522, y=70, width=145)

        self.gender_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Gender")
        self.gender_label.place(x=40, y=100)

        self.driver_gender_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.driver_gender_label.place(x=40, y=125)

        self.gender_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.gender_line.place(x=40, y=155, width=90)

        self.license_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="License")
        self.license_label.place(x=320, y=100)

        self.driver_license_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.driver_license_label.place(x=320, y=125)

        self.license_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.license_line.place(x=322, y=155, width=135)

        self.status_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Status")
        self.status_label.place(x=520, y=100)

        self.driver_status_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.driver_status_label.place(x=520, y=125)

        self.status_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.status_line.place(x=520, y=155, width=145)

        #     to show the button for more functionality of the application
        update_btn_image = ImageTk.PhotoImage(Image.open("Images/update.png").resize((20, 20), Image.ANTIALIAS))

        self.update_button = customtkinter.CTkButton(master=self.profile_frame, image=update_btn_image,
                                                     text="Update Profile", font=(self.font, 16, 'bold'),
                                                     corner_radius=15, height=34, width=100,
                                                     command=self.show_update_profile_window)
        self.update_button.place(x=160, y=400)

        password_btn_image = ImageTk.PhotoImage(Image.open("Images/password1.png").resize((20, 20), Image.ANTIALIAS))

        self.change_password_button = customtkinter.CTkButton(master=self.profile_frame, image=password_btn_image,
                                                              text="Change Password", font=(self.font, 16, 'bold'),
                                                              corner_radius=15, height=34, width=100,
                                                              command=self.show_change_password_window)
        self.change_password_button.place(x=345, y=400)

        self.fill_driver_info()

    def show_change_password_window(self):
        self.change_password_window = Toplevel(self.driver_profile_window, bg="#2c2c2c")
        self.change_password_window.title("Change Password")
        self.change_password_window.resizable(0, 0)

        screen_width = self.change_password_window.winfo_screenwidth()
        screen_height = self.change_password_window.winfo_screenheight()

        window_width = 420
        window_height = 380

        x_position = (screen_width - window_width) // 2 + 100
        y_position = (screen_height - window_height) // 2 + 40

        self.change_password_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        heading_icon = ImageTk.PhotoImage(Image.open("Images/change_password.png").resize((35, 35), Image.ANTIALIAS))
        self.heading_icon_label = Label(self.change_password_window, image=heading_icon, bg='#2c2c2c')
        self.heading_icon_label.image = heading_icon
        self.heading_icon_label.place(x=70, y=10)

        self.heading_label = Label(self.change_password_window, text="Change Your Password", font=(self.font, 17),
                                   bg="#2c2c2c", fg="white")
        self.heading_label.place(relx=0.56, rely=0.08, anchor="center")

        self.password_label = Label(self.change_password_window, text="Password", fg="white", bg="#2c2c2c",
                                    font=(self.font, 10))
        self.password_label.place(x=90, y=78)

        self.password_entry = customtkinter.CTkEntry(master=self.change_password_window, font=(self.font, 15),
                                                     width=240, placeholder_text="Password", height=40)
        self.password_entry.place(relx=0.5, rely=0.33, anchor="center")

        self.co_password_label = Label(self.change_password_window, text="Confirm Password", fg="white", bg="#2c2c2c",
                                       font=(self.font, 10))
        self.co_password_label.place(x=90, y=180)

        self.co_password_entry = customtkinter.CTkEntry(master=self.change_password_window, font=(self.font, 15),
                                                        width=240, placeholder_text="Confirm Password", height=40)
        self.co_password_entry.place(relx=0.5, rely=0.59, anchor="center")

        self.change_button = customtkinter.CTkButton(master=self.change_password_window, text="Change Password",
                                                     font=(self.font, 15), corner_radius=8, height=35,
                                                     command=self.change_password)
        self.change_button.place(x=50, y=295)

        self.exit_button = customtkinter.CTkButton(master=self.change_password_window, text="Exit",
                                                   font=(self.font, 16),
                                                   corner_radius=8, height=35, command=self.cancel_window)
        self.exit_button.place(x=230, y=295)

    def cancel_window(self):
        self.change_password_window.destroy()

    def change_password(self):
        password = self.password_entry.get()
        confirm_password = self.co_password_entry.get()
        if len(password) >= 8:
            if password == confirm_password:
                user = User(user_id=Global.current_user[0], password=password)
                password_changed = change_user_password(user)
                if password_changed:
                    messagebox.showinfo("Password Changed Successfully",
                                        "Your password has been changed successfully.\n\n Please RE-LOGIN your account.",
                                        parent=self.change_password_window)
                    # TO INSERT RECORDS TO THE ACCOUNT ACTIVITY TABLE
                    current_date_time = datetime.now()
                    current_date = current_date_time.date()
                    current_time = current_date_time.time()

                    activity_related = "Password Changed"
                    description = "Your account password was successfully updated. If you did not initiate this change, please contact support immediately."

                    accountActivity = AccountActivity(activity_related=activity_related, description=description,
                                                      date=current_date, time=current_time,
                                                      user_id=Global.current_user[0])
                    account_activity_stored = insert_account_activity_details(accountActivity)

                    if account_activity_stored:
                        self.cancel_window()
                        self.driver_profile_window.destroy()
                        self.window.destroy()
                        login_page_window = Tk()
                        login_page = MainPage(login_page_window)
                        login_page_window.mainloop()
                    else:
                        messagebox.showerror("ERROR!", "Account Activity Couldn't Store.",
                                             parent=self.change_password_window)
                else:
                    messagebox.showerror("Password Changed Failed", "Sorry, could't change your password !",
                                         parent=self.change_password_window)
            else:
                messagebox.showerror("Invalid Entry", "Password Didn't Matched !", parent=self.change_password_window)
        else:
            messagebox.showerror("Invalid Entry", "Pssword should be atleast 8 character long.",
                                 parent=self.change_password_window)
    #     ================= WINDOW FOR UPDATING PROFILE ========================
    def show_update_profile_window(self):
        self.update_profile_window = Toplevel(self.driver_profile_window)
        self.update_profile_window.title("Update Profile")
        self.update_profile_window.config(bg="#2c2c2c")
        self.update_profile_window.resizable(0, 0)

        screen_width = self.update_profile_window.winfo_screenwidth()
        screen_height = self.update_profile_window.winfo_screenheight()

        window_width = 450
        window_height = 400

        x_position = (screen_width - window_width) // 2 + 110
        y_position = (screen_height - window_height) // 2 + 40

        self.update_profile_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        heading_icon = ImageTk.PhotoImage(Image.open("Images/update1.png"))
        self.heading_icon_label = Label(self.update_profile_window, image=heading_icon, bg='#2c2c2c')
        self.heading_icon_label.image = heading_icon
        # self.heading_icon_label.place(x=67, y=3)

        self.heading_label = Label(self.update_profile_window, text="Update Your Profile", font=(self.font, 17),
                                   bg="#2c2c2c", fg="white")
        self.heading_label.place(relx=0.5, rely=0.06, anchor="center")

        self.name_entry = customtkinter.CTkEntry(master=self.update_profile_window, font=(self.font, 15), width=170,
                                                 placeholder_text="Full Name", height=38)
        self.name_entry.place(x=35, y=90)

        self.name_label = Label(master=self.update_profile_window, text="Name", font=(self.font, 9), bg="#2c2c2c",
                                fg="white")
        self.name_label.place(x=35, y=65)

        self.mobile_entry = customtkinter.CTkEntry(master=self.update_profile_window, font=(self.font, 15), width=170,
                                                   placeholder_text="Phone No", height=38)
        self.mobile_entry.place(x=250, y=90)

        self.mobile_label = Label(master=self.update_profile_window, text="Phone No", font=(self.font, 8), bg="#2c2c2c",
                                  fg="white")
        self.mobile_label.place(x=250, y=65)

        self.email_entry = customtkinter.CTkEntry(master=self.update_profile_window, font=(self.font, 13), width=170,
                                                  placeholder_text="example@gmail.com", height=38)
        self.email_entry.place(x=35, y=170)

        self.email_label = Label(master=self.update_profile_window, text="Email", font=(self.font, 9), bg="#2c2c2c",
                                 fg="white")
        self.email_label.place(x=35, y=145)

        self.address_entry = customtkinter.CTkEntry(self.update_profile_window, font=(self.font, 15), width=170,
                                                    placeholder_text="Current Address", height=38)
        self.address_entry.place(x=250, y=170)

        self.address_label = Label(master=self.update_profile_window, text="Address", font=(self.font, 9), bg="#2c2c2c",
                                   fg="white")
        self.address_label.place(x=250, y=145)

        self.license_entry = customtkinter.CTkEntry(master=self.update_profile_window, width=170, height=38,
                                                    placeholder_text="License Number", font=(self.font, 15))
        self.license_entry.place(x=35, y=255)

        self.license_label = Label(master=self.update_profile_window, text="License", font=(self.font, 9), bg="#2c2c2c",
                                   fg="white")
        self.license_label.place(x=35, y=230)

        self.gender_var = customtkinter.StringVar(value="Gender")

        self.gender_entry = customtkinter.CTkComboBox(master=self.update_profile_window,
                                                      values=["Male", "Female", "Others"], variable=self.gender_var,
                                                      width=170, height=40)
        self.gender_entry.place(x=250, y=255)

        self.gender_label = Label(master=self.update_profile_window, text="Gender", font=(self.font, 9), bg="#2c2c2c",
                                  fg="white")
        self.gender_label.place(x=250, y=230)

        self.update_button = customtkinter.CTkButton(master=self.update_profile_window, text="Update Profile",
                                                     font=(self.font, 15), corner_radius=10, height=35,
                                                     command=self.update_profile)
        self.update_button.place(x=70, y=330)

        self.exit_button = customtkinter.CTkButton(master=self.update_profile_window, text="Exit", font=(self.font, 16),
                                                   height=35, corner_radius=10, command=self.cancel_update_window)
        self.exit_button.place(x=260, y=330)

        self.set_profile_details()

    def fill_driver_info(self):
        driver_instance = Driver(driver_id=Global.logged_in_driver[0])
        user_instance = User(user_id=Global.current_user[0])

        driver, user = get_profile_details(driver_instance, user_instance)

        self.user_name.configure(text=driver[1])
        self.driver_email_label.configure(text=user[1])
        self.driver_mobile_label.configure(text=driver[2])
        self.driver_address_label.configure(text=driver[3])
        self.driver_gender_label.configure(text=driver[4])
        self.driver_license_label.configure(text=driver[5])
        self.driver_status_label.configure(text=driver[6])

    def set_profile_details(self):
        driver_instance = Driver(driver_id=Global.logged_in_driver[0])
        user_instance = User(user_id=Global.current_user[0])

        driver, user = get_profile_details(driver_instance, user_instance)

        self.name_entry.delete(0, END)
        self.name_entry.insert(0, driver[1])

        self.mobile_entry.delete(0, END)
        self.mobile_entry.insert(0, driver[2])

        self.email_entry.delete(0, END)
        self.email_entry.insert(0, user[1])

        self.address_entry.delete(0, END)
        self.address_entry.insert(0, driver[3])

        self.license_entry.delete(0, END)
        self.license_entry.insert(0, driver[5])

        self.gender_var.set(driver[4])

    def cancel_update_window(self):
        self.update_profile_window.destroy()

    def update_profile(self):

        name = self.name_entry.get()
        phone_no = self.mobile_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        license = self.license_entry.get()
        gender = self.gender_var.get()

        if not (name == "" or phone_no == "" or email == "" or address == "" or license == "" or gender == ""):
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                messagebox.showerror("Invalid Email", "Please enter a valid email address.",
                                     parent=self.update_profile_window)
                return

            # Validate phone number format
            if not re.match(r"^\d{10}$", phone_no):
                messagebox.showerror("Invalid Phone Number", "Please enter a valid 10-digit phone number.",
                                     parent=self.update_profile_window)
                return

            driver = Driver(driver_id=Global.logged_in_driver[0], name=name, phone_no=phone_no, address=address,
                            license=license, gender=gender)

            user = User(user_id=Global.current_user[0], email=email)

            profile_isupdated = update_driver_profile(driver, user)

            if profile_isupdated:

                # TO INSERT RECORDS TO THE ACCOUNT ACTIVITY TABLE
                current_date_time = datetime.now()
                current_date = current_date_time.date()
                current_time = current_date_time.time()

                activity_related = "Profile Updated"
                description = f"Your Profile was updated."

                accountActivity = AccountActivity(activity_related=activity_related, description=description,
                                                  date=current_date, time=current_time, user_id=Global.current_user[0])
                account_activity_stored = insert_account_activity_details(accountActivity)

                if account_activity_stored:
                    messagebox.showinfo("Profile Update Success", "Your Profile Has Been Successfully Updated.",
                                        parent=self.update_profile_window)
                    self.profle_name.configure(text=name)
                    self.fill_driver_info()
                    self.update_profile_window.destroy()

                else:
                    messagebox.showerror("ERROR!", "Account Activity Couldn't Store.",
                                         parent=self.update_profile_window)
            else:
                messagebox.showerror("Update Failed", "Sorry, Your Profile Couldn't Update !",
                                     parent=self.update_profile_window)
        else:
            messagebox.showerror("Update Failed", "Please Fill All The Details", parent=self.update_profile_window)

    def on_closing(self):
        self.driver_profile_window.destroy()
        self.dashboard_indicator()

if __name__ == '__main__':
    window = Tk()
    driverProfile = DriverProfile(window)
    driverProfile.show_driver_profile()
    window.mainloop()
