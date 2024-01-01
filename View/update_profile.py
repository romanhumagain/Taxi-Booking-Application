import re
from tkinter import *
from tkcalendar import calendar_, DateEntry
import  customtkinter
from PIL import  Image, ImageTk
from Model import Global
from Model.customer import Customer
from Model.user import User
from Model.account_activity import AccountActivity
from Controller.profile_dbms import profile_details, update_customer_profile
from Controller.account_activity_dbms import insert_account_activity_details
from tkinter import messagebox
from datetime import datetime

# from customer_dashboard

class UpdateProfile:
    def __init__(self, frame, profile_update_callback):
        self.frame = frame
        self.profile_update_callback = profile_update_callback

        self.font = "Century Gothic"
        # customtkinter.set_default_color_theme("green")

    def show_update_profile_window(self):
        self.update_profile_window = Toplevel(self.frame)
        self.update_profile_window.title("Update Profile")
        self.update_profile_window.config(bg="#2c2c2c")
        self.update_profile_window.resizable(0, 0)

        screen_width = self.update_profile_window.winfo_screenwidth()
        screen_height = self.update_profile_window.winfo_screenheight()

        window_width = 450
        window_height = 450

        x_position = (screen_width - window_width) // 2 + 140
        y_position = (screen_height - window_height) // 2

        self.update_profile_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        heading_icon = ImageTk.PhotoImage(Image.open("Images/update1.png"))
        self.heading_icon_label = Label(self.update_profile_window, image=heading_icon, bg='#2c2c2c')
        self.heading_icon_label.image = heading_icon
        # self.heading_icon_label.place(x=67, y=3)

        self.heading_label = Label(self.update_profile_window, text="Update Your Profile", font=(self.font, 17), bg="#2c2c2c", fg="white")
        self.heading_label.place(relx=0.5, rely=0.06, anchor="center")

        self.name_entry = customtkinter.CTkEntry(master=self.update_profile_window, font=(self.font, 15), width=170,placeholder_text="Full Name", height=38)
        self.name_entry.place(x=35, y=90)

        self.name_label= Label(master=self.update_profile_window,text="Name", font=(self.font, 9),bg="#2c2c2c", fg="white")
        self.name_label.place(x=35, y=65)

        self.mobile_entry = customtkinter.CTkEntry(master=self.update_profile_window, font=(self.font, 15),width=170, placeholder_text="Phone No", height=38)
        self.mobile_entry.place(x=250, y=90)

        self.mobile_label = Label(master=self.update_profile_window, text="Phone No", font=(self.font, 8), bg="#2c2c2c",fg="white")
        self.mobile_label.place(x=250, y=65)

        self.email_entry = customtkinter.CTkEntry(master=self.update_profile_window, font=(self.font, 13), width=170,placeholder_text="example@gmail.com", height=38)
        self.email_entry.place(x=35, y=170)

        self.email_label = Label(master=self.update_profile_window, text="Email", font=(self.font, 9), bg="#2c2c2c",
                                  fg="white")
        self.email_label.place(x=35, y=145)


        self.address_entry = customtkinter.CTkEntry(self.update_profile_window, font=(self.font, 15),width=170, placeholder_text="Current Address", height=38)
        self.address_entry.place(x=250, y=170)

        self.address_label = Label(master=self.update_profile_window, text="Address", font=(self.font, 9), bg="#2c2c2c",
                                 fg="white")
        self.address_label.place(x=250, y=145)

        self.payment_method = customtkinter.StringVar(value="Payment Method")

        self.payment_entry = customtkinter.CTkComboBox(master=self.update_profile_window, values=['Online', 'Cash'],variable=self.payment_method, width=170, height=40)
        self.payment_entry.place(x=35, y=255)

        self.payment_label = Label(master=self.update_profile_window, text="Payment", font=(self.font, 9), bg="#2c2c2c",
                                   fg="white")
        self.payment_label.place(x=35, y=230)


        self.gender_var = customtkinter.StringVar(value="Gender")

        self.gender_entry = customtkinter.CTkComboBox(master=self.update_profile_window,values=["Male", "Female", "Others"], variable=self.gender_var,width=170, height=40)
        self.gender_entry.place(x=250, y=255)

        self.gender_label = Label(master=self.update_profile_window, text="Gender", font=(self.font, 9), bg="#2c2c2c",
                                   fg="white")
        self.gender_label.place(x=250, y=230)

        self.dob_label = Label(self.update_profile_window, text="DOB", fg="white", bg="#2c2c2c",font=(self.font, 12))
        self.dob_label.place(x=26, y=325)

        self.dob_entry = DateEntry(self.update_profile_window, font=('yu gothic ui', 12), selectmode='day',
                                   style='my.DateEntry', background="black",
                                   bordercolor="white",
                                   selectbackground="red", width=12, date_pattern='yyyy-mm-dd')

        self.dob_entry.place(x=70, y=325)

        self.update_button = customtkinter.CTkButton(master = self.update_profile_window, text="Update Profile", font=(self.font, 15), corner_radius=10,height=35, command=self.update_profile)
        self.update_button.place(x=70, y=390)

        self.exit_button = customtkinter.CTkButton(master=self.update_profile_window, text="Exit", font=(self.font, 16),height=35,corner_radius=10, command=self.cancel_window)
        self.exit_button.place(x=260, y=390)

        self.set_profile_details()

    def set_profile_details(self):
        customer = Customer(customer_id=Global.logged_in_customer[0])
        customer_profile_info, user = profile_details(customer)
        if customer_profile_info is not None:
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, customer_profile_info[1])

            self.mobile_entry.delete(0, END)
            self.mobile_entry.insert(0, customer_profile_info[2])

            self.email_entry.delete(0, END)
            self.email_entry.insert(0, user[1])

            self.address_entry.delete(0, END)
            self.address_entry.insert(0, customer_profile_info[4])

            self.dob_entry.delete(0, END)
            self.dob_entry.insert(0, customer_profile_info[5])

            self.payment_method.set(customer_profile_info[3])
            self.gender_var.set(customer_profile_info[6])

    def cancel_window(self):
        self.update_profile_window.destroy()

    def update_profile(self):
        name = self.name_entry.get()
        phone_no = self.mobile_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        payment_method = self.payment_method.get()
        gender = self.gender_var.get()
        date_of_birth = self.dob_entry.get()

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.",
                                 parent=self.update_profile_window)
            return

        # Validate phone number format
        if not re.match(r"^\d{10}$", phone_no):
            messagebox.showerror("Invalid Phone Number", "Please enter a valid 10-digit phone number.",
                                 parent=self.update_profile_window)
            return

        # Check other non-empty fields
        if not (name == "" or phone_no == "" or email == "" or address == "" or payment_method == "" or gender == ""):
            customer = Customer(customer_id=Global.logged_in_customer[0], name=name, phone_no=phone_no, address=address,
                                date_of_birth=date_of_birth, payment=payment_method, gender=gender)
            user = User(user_id=Global.current_user[0], email=email)

            profile_is_updated = update_customer_profile(customer, user)

            if profile_is_updated:
                # TO INSERT RECORDS TO THE ACCOUNT ACTIVITY TABLE
                current_date_time = datetime.now()
                current_date = current_date_time.date()
                current_time = current_date_time.time()

                activity_related = "Profile Updated"
                description = "Your Profile was updated."

                accountActivity = AccountActivity(activity_related=activity_related, description=description,
                                                  date=current_date, time=current_time, user_id=Global.current_user[0])
                account_activity_stored = insert_account_activity_details(accountActivity)

                if account_activity_stored:
                    messagebox.showinfo("Profile Update Success", "Your Profile Has Been Successfully Updated.",
                                        parent=self.update_profile_window)
                    self.set_profile_details()

                    self.update_profile_window.destroy()
                    if self.profile_update_callback:
                        self.profile_update_callback()
                else:
                    messagebox.showerror("ERROR!", "Account Activity Couldn't Store.",
                                         parent=self.update_profile_window)
            else:
                messagebox.showerror("Update Failed", "Sorry, Your Profile Couldn't Update!",
                                     parent=self.update_profile_window)
        else:
            messagebox.showerror("Update Failed", "Please Fill All The Details", parent=self.update_profile_window)


if __name__ == '__main__':
    window = Tk()
    update_profile = UpdateProfile(window)
    update_profile.show_update_profile_window()
    window.mainloop()
