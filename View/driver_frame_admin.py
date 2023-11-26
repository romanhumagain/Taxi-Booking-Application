import tkinter.ttk
from tkinter import *
import customtkinter
from tkinter import messagebox
from Controller.driver_dbms import register_driver, search_driver, get_all_driver
from Controller.customer_registration_dbms import register_user
from Model.user import User
from Model.driver import Driver

class DriverWindow:
    def __init__(self, window):
        self.window = window
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

    def show_driver_window(self):
        self.driver_window = Toplevel(self.window, bg="#3c3c3c")
        self.driver_window.title("Driver Management System")
        self.driver_window.resizable(0, 0)

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

        self.search_button = customtkinter.CTkButton(master=self.driver_frame, width=60, height=35, text="search",
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
        self.save_button = customtkinter.CTkButton(self.button_frame, text="Add Driver", width=150,
                                                     font=(self.font, 15,'bold'), height=35, corner_radius=10,command=self.register_driver)
        self.save_button.place(relx=0.5, rely=0.1, anchor = "center")

        self.update_button = customtkinter.CTkButton(self.button_frame, text="Update", width=150, height=35,
                                                       font=(self.font, 15,'bold'), corner_radius=10)
        self.update_button.place(relx=0.5, rely=0.24, anchor = "center")

        self.delete_button = customtkinter.CTkButton(self.button_frame, text="Delete", width=150, height=35,
                                                       font=(self.font, 15,'bold'), corner_radius=10)
        self.delete_button.place(relx=0.5, rely=0.38, anchor = "center")

        self.line = Canvas(self.button_frame, bg="white", highlightthickness=0, height=3, width=200)
        self.line.place(x=0, y= 200)

        self.all_driver_button = customtkinter.CTkButton(self.button_frame, text="Driver Details", width=150,
                                                         height=35,
                                                         font=(self.font, 15,'bold'), corner_radius=10, command=self.driver_details_table)
        self.all_driver_button.place(relx=0.5, rely=0.55, anchor="center")


        self.available_button = customtkinter.CTkButton(self.button_frame, text="Available Driver", width=150, height=35,
                                                     font=(self.font, 15,'bold'), corner_radius=10)
        self.available_button.place(relx=0.5, rely=0.69, anchor="center")

        self.reserved_button = customtkinter.CTkButton(self.button_frame, text="Reserved Driver", width=150,
                                                        height=35,
                                                        font=(self.font, 15,'bold'), corner_radius=10)
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
            driver = Driver(driver_id=driver_id)
            searched_result = search_driver(driver)
            if not searched_result is None:
                self.clear_fields()
                self.name_entry.insert(0, searched_result[1])
                self.phone_entry.insert(0, searched_result[2])
                self.address_entry.insert(0, searched_result[3])
                self.license_entry.insert(0, searched_result[4])
                self.gender_value.set(searched_result[5])
                self.password_entry.insert(0, "password")
                self.password_entry.configure(show="*")
            else:
                messagebox.showerror("INVALID ENTRY", f"Driver with driver ID {driver_id} doesn't exists!")
                self.clear_fields()
        else:
            messagebox.showerror("ERROR", "please provide driver ID to get driver details")


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
                    messagebox.showinfo("Registration Success !", "Successfully Registered Driver")
                    self.set_all_driver_details()
                    self.clear_fields()
                else:
                    messagebox.showerror("Registration Failed", "Sorry Could't Register Driver!")
            else:
                messagebox.showerror("Registration Failed", "Sorry Could't Register User!")

        else:
            messagebox.showerror("Registration Failed", "Please Fill All The Details!")


    # ======== TO GET THE ALL DRIVER DETAILS ===========
    def driver_details_table(self):
        self.table_heading.configure(text="Driver Details")

        self.driver_details_table = tkinter.ttk.Treeview(self.driver_table_frame, columns=(
            "driver_id", "name", "phone_no", "address", "license_no", "gender", "driver_status"), height=9,
                                                         show="headings")

        self.driver_details_table.heading("driver_id", text="D-ID", anchor=CENTER)
        self.driver_details_table.heading("name", text="Name", anchor=CENTER)
        self.driver_details_table.heading("phone_no", text="Phone", anchor=CENTER)
        self.driver_details_table.heading("address", text="Address", anchor=CENTER)
        self.driver_details_table.heading("license_no", text="license No", anchor=CENTER)
        self.driver_details_table.heading("gender", text="Gender", anchor=CENTER)
        self.driver_details_table.heading("driver_status", text="Status", anchor=CENTER)

        self.driver_details_table.column("driver_id", width=60, anchor=CENTER)
        self.driver_details_table.column("name", width=100, anchor=CENTER)
        self.driver_details_table.column("phone_no", width=100, anchor=CENTER)
        self.driver_details_table.column("address", width=100, anchor=CENTER)
        self.driver_details_table.column("license_no", width=200, anchor=CENTER)
        self.driver_details_table.column("gender", width=100, anchor=CENTER)
        self.driver_details_table.column("driver_status", width=100, anchor=CENTER)

        self.driver_details_table.place(x=0, y=0)
        self.driver_details_table.bind("<ButtonRelease-1>", self.fill_all_driver_details)

        self.set_all_driver_details()

    def set_all_driver_details(self):
        result = get_all_driver()
        for item in self.driver_details_table.get_children():
            self.driver_details_table.delete(item)

        for row in result:
            self.driver_details_table.insert('', END, values=row)

    def fill_all_driver_details(self, event):
        view_info = self.driver_details_table.focus()
        driver_info = self.driver_details_table.item(view_info)

        row = driver_info.get('values')
        self.clear_fields()
        self.search_entry.delete(0, END)
        self.search_entry.insert(0, row[0])
        self.name_entry.insert(0, row[1])
        self.phone_entry.insert(0, row[2])
        self.address_entry.insert(0, row[3])
        self.license_entry.insert(0, row[4])
        self.gender_value.set(row[5])





    # ======== TO GET THE AVAILABLE DRIVER DETAILS =========
    def available_driver_table(self):
        pass

    # ========= TO GET THE ASSIGNED DRIVER DTAILS TABLE ===========
    def reserved_driver_table(self):
        pass

    def clear_fields(self):
        # self.search_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.gender_value.set("Gender")
        self.license_entry.delete(0, END)
        self.password_entry.delete(0, END)


if __name__ == '__main__':
    window = Tk()
    driverWindow = DriverWindow(window)
    driverWindow.show_driver_window()
    window.mainloop()

