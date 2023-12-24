import tkinter.ttk
from datetime import datetime
from tkinter import *
import customtkinter
from tkinter import messagebox

from Controller.account_activity_dbms import insert_account_activity_details
from Controller.driver_dbms import register_driver, search_driver, get_all_driver, get_available_driver, \
    update_driver_details, delete_driver, fetch_reserved_driver
from Controller.customer_registration_dbms import register_user
from Model import Global
from Model.account_activity import AccountActivity
from Model.user import User
from Model.driver import Driver
from PIL import Image, ImageTk

class DriverWindow:
    def __init__(self, window, top_level_list = [], count_driver= None):
        self.window = window
        self.font = "Century Gothic"
        self.top_level_list = top_level_list
        self.count_driver = count_driver

        self.view_booking_label = None

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

    def show_driver_window(self):
        self.driver_window = Toplevel(self.window, bg="#3c3c3c")
        self.driver_window.title("Driver Management System")
        self.driver_window.resizable(0, 0)

        # to add toplevel window to the list in the AdminDashboard Class
        self.top_level_list.append(self.driver_window)

        width = 1000
        height = 600

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_position = (screen_width - width) // 2 + 140
        y_position = (screen_height - height) // 2

        self.driver_window.geometry(f"{width}x{height}+{x_position}+{y_position}")

        self.top_frame = customtkinter.CTkFrame(self.driver_window, width=980, height=70, corner_radius=20)
        self.top_frame.place(x=10, y=20)

        self.heading_label = customtkinter.CTkLabel(self.top_frame, text="Driver Management Panel", font=(self.font, 30))
        self.heading_label.place(relx=0.5, rely=0.5, anchor="center")

        self.driver_frame = customtkinter.CTkFrame(self.driver_window, width=780, height=490, corner_radius=20)
        self.driver_frame.place(x=10, y=100)

        # for search entry
        self.search_entry = customtkinter.CTkEntry(master=self.driver_frame, width=100, height=36, font=(self.font, 15),
                                              placeholder_text="Driver ID")
        self.search_entry.place(x=30, y=30)

        search_btn_image = ImageTk.PhotoImage(Image.open("Images/search.png").resize((25,25), Image.ANTIALIAS))


        self.search_button = customtkinter.CTkButton(master=self.driver_frame, width=60, height=35, text="search",image=search_btn_image,
                                                font=(self.font, 16),
                                                corner_radius=15, command=self.search_driver)
        self.search_button.place(x=140, y=32)


        # ============== for the driver details forms ==========
        self.name_lbl = customtkinter.CTkLabel(self.driver_frame, text="Name", font=(self.font, 13))
        self.name_lbl.place(x=30, y=90)

        self.name_entry = customtkinter.CTkEntry(self.driver_frame, font=(self.font, 13), width=100, height=35)
        self.name_entry.place(x=30, y=120)

        self.phone_lbl = customtkinter.CTkLabel(self.driver_frame, text="Phone", font=(self.font, 13))
        self.phone_lbl.place(x=160, y=90)

        self.phone_entry = customtkinter.CTkEntry(self.driver_frame, font=(self.font, 13), width=100, height=35)
        self.phone_entry.place(x=160, y=120)

        self.address_lbl = customtkinter.CTkLabel(self.driver_frame, text="Address", font=(self.font, 13))
        self.address_lbl.place(x=290, y=90)

        self.address_entry = customtkinter.CTkEntry(self.driver_frame, font=(self.font, 13), width=100, height=35)
        self.address_entry.place(x=290, y=120)

        self.license_lbl = customtkinter.CTkLabel(self.driver_frame, text="License No.", font=(self.font, 13))
        self.license_lbl.place(x=420, y=90)

        self.license_entry = customtkinter.CTkEntry(self.driver_frame, font=(self.font, 13), width=100, height=35)
        self.license_entry.place(x=420, y=120)

        self.gender_value = customtkinter.StringVar(value="Gender")
        self.gender_option = ['Male', 'Female']

        self.gender_lbl = customtkinter.CTkLabel(self.driver_frame, text="Gender", font=(self.font, 13))
        self.gender_lbl.place(x=550, y= 90)

        self.gender_combobox = customtkinter.CTkComboBox(self.driver_frame, values=self.gender_option, variable=self.gender_value, width=90, height=35)
        self.gender_combobox.place(x=550, y= 120)

        self.password_lbl = customtkinter.CTkLabel(self.driver_frame, text="Password", font=(self.font, 13))
        self.password_lbl.place(x=660, y=90)

        self.password_entry = customtkinter.CTkEntry(self.driver_frame, font=(self.font, 13), width=100, height=35)
        self.password_entry.place(x=660, y=120)

        self.button_frame = customtkinter.CTkFrame(self.driver_window, width=190, height=440, corner_radius=20)
        self.button_frame.place(x=800, y=120)

        #======================= CREATING A BUTTON FOR MORE FUNCTIONALITY ===================

        save_btn_image = ImageTk.PhotoImage(Image.open("Images/password.png").resize((30,30), Image.ANTIALIAS))


        self.save_button = customtkinter.CTkButton(self.button_frame,image=save_btn_image, text="Register", width=150,
                                                     font=(self.font, 15,'bold'), height=35, corner_radius=10,command=self.register_driver)
        self.save_button.place(relx=0.5, rely=0.1, anchor = "center")

        update_btn_image = ImageTk.PhotoImage(Image.open("Images/update.png").resize((30,30), Image.ANTIALIAS))


        self.update_button = customtkinter.CTkButton(self.button_frame, text="Update", width=150, height=35,image=update_btn_image,
                                                       font=(self.font, 15,'bold'), corner_radius=10, command=self.update_driver)
        self.update_button.place(relx=0.5, rely=0.24, anchor = "center")


        delete_button_image = ImageTk.PhotoImage(Image.open("Images/delete.png").resize((30,30), Image.ANTIALIAS))

        self.delete_button = customtkinter.CTkButton(self.button_frame, text="Delete", width=150, height=35,image=delete_button_image,
                                                       font=(self.font, 15,'bold'), corner_radius=10, command=self.delete_driver)
        self.delete_button.place(relx=0.5, rely=0.38, anchor = "center")

        self.line = Canvas(self.button_frame, bg="white", highlightthickness=0, height=3, width=200)
        self.line.place(x=0, y= 200)

        self.all_driver_button = customtkinter.CTkButton(self.button_frame, text="Driver Details", width=150,
                                                         height=35,
                                                         font=(self.font, 15,'bold'), corner_radius=10, command=self.driver_details_table)
        self.all_driver_button.place(relx=0.5, rely=0.55, anchor="center")


        self.available_button = customtkinter.CTkButton(self.button_frame, text="Available Driver", width=150, height=35,
                                                     font=(self.font, 15,'bold'), corner_radius=10, command=self.available_driver_details_table)
        self.available_button.place(relx=0.5, rely=0.69, anchor="center")

        self.reserved_button = customtkinter.CTkButton(self.button_frame, text="Reserved Driver", width=150,
                                                        height=35,
                                                        font=(self.font, 15,'bold'), corner_radius=10, command=self.reserved_driver_details_table)
        self.reserved_button.place(relx=0.5, rely=0.84, anchor="center")

        self.table_heading =customtkinter.CTkLabel(self.driver_frame, text="", font=(self.font, 23))
        self.table_heading.place(relx=0.5, rely= 0.42, anchor = "center")

        self.driver_table_frame = Frame(self.driver_frame, bg="red", width=760, height=240)
        self.driver_table_frame.place(x=10, y=240)

        self.driver_details_table()

    # ======== TO SEARCH THE DRIVER USING CUSTOMER ID ===========
    def search_driver(self):
        driver_id = self.search_entry.get()
        if driver_id != "":
            self.table_heading.configure(text="Driver Details")
            driver = Driver(driver_id=driver_id)
            searched_result, table_result = search_driver(driver)
            if not searched_result is None:
                # self.clear_driver_table_frame()
                self.driver_details_table()
                for item in self.driver_detail_table.get_children():
                    self.driver_detail_table.delete(item)

                for row in table_result:
                    self.driver_detail_table.insert('', END, values=row)

                self.clear_fields()
                self.name_entry.insert(0, searched_result[1])
                self.phone_entry.insert(0, searched_result[2])
                self.address_entry.insert(0, searched_result[3])
                self.license_entry.insert(0, searched_result[4])
                self.gender_value.set(searched_result[5])
                self.password_entry.insert(0, "password")
                self.password_entry.configure(show="*")


            else:
                messagebox.showerror("INVALID ENTRY", f"Driver with driver ID {driver_id} doesn't exists!", parent=self.driver_window)
                self.clear_fields()
        else:
            messagebox.showerror("ERROR", "please provide driver ID to get driver details", parent=self.driver_window)


    # ========= TO REGISTER THE DRIVER DETAILS =========
    def register_driver(self):

        if not (self.name_entry.get()=="" or self.address_entry.get()=="" or self.phone_entry.get() == "" or self.license_entry.get()=="" or self.gender_value.get() == "Gender" or self.password_entry.get()==""):
            name = self.name_entry.get()
            email = name.lower().strip() + "@gmail.com"
            password = self.password_entry.get()
            user_type = "driver"

            # Creating a instance of the User Model
            user = User(email=email, password=password, user_type= user_type)
            user_registered = register_user(user)
            if user_registered:
                driver = Driver(name=self.name_entry.get(), address=self.address_entry.get(), phone_no=self.phone_entry.get(), license=self.license_entry.get(), gender=self.gender_value.get(), driver_status="available")
                driver_registered = register_driver(driver, user)
                if driver_registered:
                    # TO INSERT RECORDS TO THE ACCOUNT ACTIVITY TABLE
                    current_date_time = datetime.now()
                    current_date = current_date_time.date()
                    current_time = current_date_time.time()

                    activity_related = "Driver Registered"
                    description = f"{self.name_entry.get()} was successfully registered as a driver"

                    accountActivity = AccountActivity(activity_related=activity_related, description=description,
                                                      date=current_date, time=current_time,
                                                      user_id=Global.current_user[0])
                    account_activity_stored = insert_account_activity_details(accountActivity)

                    if account_activity_stored:
                        messagebox.showinfo("Registration Success !", "Successfully Registered Driver", parent=self.driver_window)
                        self.set_all_driver_details()
                        self.clear_fields()
                        self.count_driver()
                    else:
                        messagebox.showerror("Activity Details Failed", "Activity Details Failed to Store.", parent= self.driver_window)
                else:
                    messagebox.showerror("Registration Failed", "Sorry Could't Register Driver!", parent=self.driver_window)
            else:
                messagebox.showerror("Registration Failed", "Sorry Could't Register User!", parent=self.driver_window)

        else:
            messagebox.showerror("Registration Failed", "Please Fill All The Details!", parent=self.driver_window)


    # =========== TO UPDATE THE DRIVER =================
    def update_driver(self):
        driver_id = self.search_entry.get()
        if not ( driver_id== "" or self.name_entry.get() == "" or self.address_entry.get() == "" or self.phone_entry.get() == "" or self.license_entry.get() == "" or self.gender_value.get() == "Gender" ):

            driver = Driver(driver_id=driver_id)
            found_driver, _ = search_driver(driver)

            if found_driver:
                driver = Driver(name=self.name_entry.get(), address=self.address_entry.get(),
                                    phone_no=self.phone_entry.get(), license=self.license_entry.get(),
                                    gender=self.gender_value.get(), driver_id=self.search_entry.get())

                driver_isupdated = update_driver_details(driver)

                if driver_isupdated:
                    # TO INSERT RECORDS TO THE ACCOUNT ACTIVITY TABLE
                    current_date_time = datetime.now()
                    current_date = current_date_time.date()
                    current_time = current_date_time.time()

                    activity_related = "Driver Updated"
                    description = f"Driver with driver ID {driver_id} was successfully updated."

                    accountActivity = AccountActivity(activity_related=activity_related, description=description,
                                                      date=current_date, time=current_time,
                                                      user_id=Global.current_user[0])
                    account_activity_stored = insert_account_activity_details(accountActivity)

                    if account_activity_stored:

                        messagebox.showinfo("Update Success !", "Successfully Updated Driver Details",
                                                parent=self.driver_window)
                        self.search_driver()
                    else:
                        messagebox.showerror("Activity Details Failed", "Activity Details Failed to Store.",
                                             parent=self.driver_window)

                else:
                    messagebox.showerror("Update Failed", "Sorry Could't Update Driver!", parent=self.driver_window)
            else:
                messagebox.showerror("Invalid ID", f"Driver With Driver ID {driver_id} Does't Exists", parent=self.driver_window)

        else:
            messagebox.showerror("Update Failed", "Please Fill All The Details!", parent=self.driver_window)

    # ======== TO DELETE THE DRIVER===========
    def delete_driver(self):
        driver_id = self.search_entry.get()
        if driver_id != "":
            confirmed = messagebox.askyesno("Confirm Delete", f"Do You Want To Delete The Driver With Driver ID {driver_id}?", parent=self.driver_window)
            if confirmed:
                driver = Driver(driver_id=driver_id)
                found_driver, _ = search_driver(driver)
                if found_driver:
                    if found_driver[5] == "available":
                        driver = Driver(driver_id=driver_id, user_id=found_driver[7])
                        driver_isdeleted = delete_driver(driver)
                        if driver_isdeleted:
                            # TO INSERT RECORDS TO THE ACCOUNT ACTIVITY TABLE
                            current_date_time = datetime.now()
                            current_date = current_date_time.date()
                            current_time = current_date_time.time()

                            activity_related = "Driver Deleted"
                            description = f"Driver with driver ID {driver_id} was successfully deleted."

                            accountActivity = AccountActivity(activity_related=activity_related, description=description,
                                                              date=current_date, time=current_time,
                                                              user_id=Global.current_user[0])
                            account_activity_stored = insert_account_activity_details(accountActivity)
                            if account_activity_stored:
                                messagebox.showinfo("Deletion Success", f"Successfully deleted driver having driver ID {driver_id}", parent=self.driver_window)
                                self.set_all_driver_details()
                                self.clear_fields()
                                self.search_entry.delete(0, END)
                                self.count_driver()
                            else:
                                messagebox.showerror("Activity Details Failed", "Activity Details Failed to Store.",
                                                     parent=self.driver_window)
                        else:
                            messagebox.showerror("ERROR", "Sorry Could't Delete Driver From The System.", parent=self.driver_window)
                    else:
                        messagebox.showerror("ERROR", "Sorry, You Can't Delete The Assigned Driver.\n Please Check The Availability Of Driver.", parent=self.driver_window)
                else:
                    messagebox.showerror("Invalid ID", f"Driver With Driver ID {driver_id} Does't Exists", parent=self.driver_window)
        else:
            messagebox.showerror("ERROR", "please provide driver ID to delete Driver", parent=self.driver_window)

    # ======== TO GET THE ALL DRIVER DETAILS ===========
    def driver_details_table(self):
        self.clear_driver_table_frame()
        self.clear_fields()
        self.search_entry.delete(0, END)

        if self.view_booking_label is not None:
            self.view_booking_label.destroy()
            self.view_booking_label = None

        self.table_heading.configure(text="Driver Details")

        self.driver_detail_table = tkinter.ttk.Treeview(self.driver_table_frame, columns=(
            "driver_id", "name", "phone_no", "address", "license_no", "gender", "driver_status"), height=9,
                                                         show="headings")

        self.driver_detail_table.heading("driver_id", text="D-ID", anchor=CENTER)
        self.driver_detail_table.heading("name", text="Name", anchor=CENTER)
        self.driver_detail_table.heading("phone_no", text="Phone", anchor=CENTER)
        self.driver_detail_table.heading("address", text="Address", anchor=CENTER)
        self.driver_detail_table.heading("license_no", text="license No", anchor=CENTER)
        self.driver_detail_table.heading("gender", text="Gender", anchor=CENTER)
        self.driver_detail_table.heading("driver_status", text="Status", anchor=CENTER)

        self.driver_detail_table.column("driver_id", width=60, anchor=CENTER)
        self.driver_detail_table.column("name", width=100, anchor=CENTER)
        self.driver_detail_table.column("phone_no", width=100, anchor=CENTER)
        self.driver_detail_table.column("address", width=100, anchor=CENTER)
        self.driver_detail_table.column("license_no", width=200, anchor=CENTER)
        self.driver_detail_table.column("gender", width=100, anchor=CENTER)
        self.driver_detail_table.column("driver_status", width=100, anchor=CENTER)

        self.driver_detail_table.place(x=0, y=0)
        self.driver_detail_table.bind("<ButtonRelease-1>", lambda event: self.fill_all_driver_details(event,self.driver_detail_table))

        self.set_all_driver_details()

    def set_all_driver_details(self):
        result = get_all_driver()
        for item in self.driver_detail_table.get_children():
            self.driver_detail_table.delete(item)

        for row in result:
            self.driver_detail_table.insert('', END, values=row)

    def available_driver_details_table(self):
        self.clear_driver_table_frame()
        self.clear_fields()
        self.search_entry.delete(0, END)

        if self.view_booking_label is not None:
            self.view_booking_label.destroy()
            self.view_booking_label = None

        self.table_heading.configure(text="Available Driver Details")

        self.available_driver_table = tkinter.ttk.Treeview(self.driver_table_frame, columns=(
            "driver_id", "name", "phone_no", "address", "license_no", "gender", "driver_status"), height=9,
                                                         show="headings")

        self.available_driver_table.heading("driver_id", text="D-ID", anchor=CENTER)
        self.available_driver_table.heading("name", text="Name", anchor=CENTER)
        self.available_driver_table.heading("phone_no", text="Phone", anchor=CENTER)
        self.available_driver_table.heading("address", text="Address", anchor=CENTER)
        self.available_driver_table.heading("license_no", text="license No", anchor=CENTER)
        self.available_driver_table.heading("gender", text="Gender", anchor=CENTER)
        self.available_driver_table.heading("driver_status", text="Status", anchor=CENTER)

        self.available_driver_table.column("driver_id", width=60, anchor=CENTER)
        self.available_driver_table.column("name", width=100, anchor=CENTER)
        self.available_driver_table.column("phone_no", width=100, anchor=CENTER)
        self.available_driver_table.column("address", width=100, anchor=CENTER)
        self.available_driver_table.column("license_no", width=200, anchor=CENTER)
        self.available_driver_table.column("gender", width=100, anchor=CENTER)
        self.available_driver_table.column("driver_status", width=100, anchor=CENTER)

        self.available_driver_table.place(x=0, y=0)
        self.available_driver_table.bind("<ButtonRelease-1>",lambda event: self.fill_all_driver_details(event,self.available_driver_table))

        self.set_available_driver_details()
    def set_available_driver_details(self):
        self.table_heading.configure(text="Available Driver Details")

        result = get_available_driver()

        for item in self.available_driver_table.get_children():
            self.available_driver_table.delete(item)

        for row in result:
            self.available_driver_table.insert('', END, values=row)

    def fill_all_driver_details(self, event, table):
        view_info = table.focus()
        driver_info = table.item(view_info)

        row = driver_info.get('values')
        self.clear_fields()
        self.search_entry.delete(0, END)
        self.search_entry.insert(0, row[0])
        self.name_entry.insert(0, row[1])
        self.phone_entry.insert(0, row[2])
        self.address_entry.insert(0, row[3])
        self.license_entry.insert(0, row[4])
        self.gender_value.set(row[5])

        self.password_entry.configure(show="*")
        self.password_entry.insert(0, "password")

    def reserved_driver_details_table(self):
        self.clear_driver_table_frame()
        self.clear_fields()
        self.search_entry.delete(0, END)
        self.table_heading.configure(text="Reserved Driver Details")

        self.reserved_driver_table = tkinter.ttk.Treeview(self.driver_table_frame, columns=(
            "driver_id","booking_id", "name", "phone_no", "address", "license_no", "gender"), height=9,
                                                         show="headings")

        self.reserved_driver_table.heading("driver_id", text="D-ID", anchor=CENTER)
        self.reserved_driver_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.reserved_driver_table.heading("name", text="Name", anchor=CENTER)
        self.reserved_driver_table.heading("phone_no", text="Phone", anchor=CENTER)
        self.reserved_driver_table.heading("address", text="Address", anchor=CENTER)
        self.reserved_driver_table.heading("license_no", text="license No", anchor=CENTER)
        self.reserved_driver_table.heading("gender", text="Gender", anchor=CENTER)

        self.reserved_driver_table.column("driver_id", width=60, anchor=CENTER)
        self.reserved_driver_table.column("booking_id", width=100, anchor=CENTER)
        self.reserved_driver_table.column("name", width=100, anchor=CENTER)
        self.reserved_driver_table.column("phone_no", width=100, anchor=CENTER)
        self.reserved_driver_table.column("address", width=100, anchor=CENTER)
        self.reserved_driver_table.column("license_no", width=200, anchor=CENTER)
        self.reserved_driver_table.column("gender", width=100, anchor=CENTER)

        self.reserved_driver_table.place(x=0, y=0)
        self.reserved_driver_table.bind("<ButtonRelease-1>",lambda event: self.fill_all_reserved_driver_details(event,self.reserved_driver_table))


        self.set_reserved_driver_details()

    def fill_all_reserved_driver_details(self, event, table):
        view_info = table.focus()
        driver_info = table.item(view_info)

        row = driver_info.get('values')
        self.clear_fields()
        self.search_entry.delete(0, END)
        self.search_entry.insert(0, row[0])
        self.name_entry.insert(0, row[2])
        self.phone_entry.insert(0, row[3])
        self.address_entry.insert(0, row[4])
        self.license_entry.insert(0, row[5])
        self.gender_value.set(row[6])

        self.password_entry.configure(show="*")
        self.password_entry.insert(0, "password")

        self.view_booking_label = Label(self.button_frame, text="View Booking", font = (self.font, 11, 'underline'), cursor="hand2", bg="#2c2c2c", fg="white")
        self.view_booking_label.place(relx= 0.5, rely= 0.94, anchor = "center")
        self.view_booking_label.bind("<Button-1>", lambda event: self.view_booking(event, row[1]))

    def set_reserved_driver_details(self):

        result = fetch_reserved_driver()

        for item in self.reserved_driver_table.get_children():
            self.reserved_driver_table.delete(item)

        for row in result:
            self.reserved_driver_table.insert('', END, values=row)

    def view_booking(self, event, booking_id):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_position = (screen_width - 820) // 2 + 180
        y_position = (screen_height - 420) // 2


        from booking_details_admin import BookingDetails
        bookingDetails = BookingDetails(self.driver_window)
        bookingDetails.show_booking_details_window()
        bookingDetails.booking_details_window.geometry(f"820x420+{x_position}+{y_position}")
        bookingDetails.top_frame.configure(width=800, height=100)

        bookingDetails.table_frame.configure(height=230)
        bookingDetails.booking_table_frame.configure(height=200)

        bookingDetails.search_entry.insert(0, booking_id)
        bookingDetails.search()

        bookingDetails.heading_label.configure(text=f"Showing Booking Details Of Booking ID {booking_id}", font=(self.font, 21))
        bookingDetails.button_frame.destroy()


    def clear_fields(self):
        # self.search_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.gender_value.set("Gender")
        self.license_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def clear_driver_table_frame(self):
        for widget in self.driver_table_frame.winfo_children():
            widget.destroy()


if __name__ == '__main__':
    window = Tk()
    driverWindow = DriverWindow(window)
    driverWindow.show_driver_window()
    window.mainloop()

