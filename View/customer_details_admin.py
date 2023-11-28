import tkinter
from tkinter import *
from tkinter.ttk import Treeview

from PIL import Image, ImageTk
from Controller.customer_dbms import fetch_all_customer, search_customer
import customtkinter
from Model.customer import Customer
from tkinter import messagebox

class CustomerDetails:
    def __init__(self, window):
        self.window = window
        self.font = "Century Gothic"

    def show_customer_details_window(self):
        self.customer_details_window = Toplevel(self.window, bg="#2c2c2c")
        self.customer_details_window.title("Customer Details")
        self.customer_details_window.resizable(0,0)

        width = 820
        height = 490

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_position =  (screen_width - width) // 2 + 145
        y_position = (screen_height - height) // 2 + 10

        self.customer_details_window.geometry(f"{width}x{height}+{x_position}+{y_position}")

        self.main_frame = customtkinter.CTkFrame(master=self.customer_details_window, width=820, height=490)
        self.main_frame.place(x=0, y=0)

        self.inner_top_frame = customtkinter.CTkFrame(master=self.main_frame, width=810, height=60,
                                                      corner_radius=20)
        self.inner_top_frame.place(x=5, y=10)

        self.heading_label = customtkinter.CTkLabel(self.inner_top_frame, text="Customer Details", font=(self.font, 30))
        self.heading_label.place(relx=0.5, rely=0.5, anchor = CENTER)

        #  for search entry
        self.search_entry = customtkinter.CTkEntry(master=self.main_frame, width=150, height=36, placeholder_text="Customer ID")
        self.search_entry.place(x=30, y=90)

        search_btn_image = ImageTk.PhotoImage(Image.open("Images/search.png").resize((25,25), Image.ANTIALIAS))


        search_button = customtkinter.CTkButton(master=self.main_frame, width=80, height=35, text="search",image=search_btn_image,font=(self.font, 16),
                                                corner_radius=15, command=self.search_customer)
        search_button.place(x=190, y=92)

        # ======= CREATING A FRAME TO SHOW THE CUSTOMER DETAILS TABLE =============

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
                         padding=(0, 8)
                         )

        style1.map("Treeview.Heading",
                   background=[('active', '#3c3c3c')],
                   foreground=[('active', 'white')])


        self.table_frame = Frame(self.main_frame, bg="white", width=780, height=260)
        self.table_frame.place(x=20, y=150)

        scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)

        self.customer_details_table = Treeview(
            self.table_frame,
            columns=("customer_id", "customer_name","email", "Phone_no", "payment", "address", "dob","gender"),
            show="headings",
            height=8,
            yscrollcommand=scroll_y
        )
        scroll_y.place(x=140, y=0)
        # scroll_y.config(command=self.customer_details_table.yview)
        self.customer_details_table.place(x=0, y=0)


        self.customer_details_table.heading("customer_id", text="C-ID", anchor=CENTER)
        self.customer_details_table.heading("customer_name", text="Name", anchor=CENTER)
        self.customer_details_table.heading("email", text="Email", anchor=CENTER)
        self.customer_details_table.heading("Phone_no", text="Phone No", anchor=CENTER)
        self.customer_details_table.heading("payment", text="Payment", anchor=CENTER)
        self.customer_details_table.heading("address", text="Address", anchor=CENTER)
        self.customer_details_table.heading("dob", text="D.O.B", anchor=CENTER)
        self.customer_details_table.heading("gender", text="Gender", anchor=CENTER)

        self.customer_details_table.column("customer_id", width=50, anchor=CENTER)
        self.customer_details_table.column("customer_name", width=140, anchor=CENTER)
        self.customer_details_table.column("email", width=160, anchor=CENTER)
        self.customer_details_table.column("Phone_no", width=100, anchor=CENTER)
        self.customer_details_table.column("payment", width=80, anchor=CENTER)
        self.customer_details_table.column("address", width=100, anchor=CENTER)
        self.customer_details_table.column("dob", width=70, anchor=CENTER)
        self.customer_details_table.column("gender", width=80, anchor=CENTER)

        # ======= SETTING BUTTONS FOR MORE FUNCTIONALITY ============
        delete_btn_image = ImageTk.PhotoImage(Image.open("Images/delete.png").resize((30,30), Image.ANTIALIAS))


        self.delete_customer_button = customtkinter.CTkButton(master=self.main_frame, width=120,
                                                             font=(self.font, 17, 'bold'), text="Delete User", height=36,
                                                             corner_radius=20, image=delete_btn_image)
        self.delete_customer_button.place(x=330, y=435)

        self.get_customer_details()

    def get_customer_details(self):
        fetched_result = fetch_all_customer()
        for item in self.customer_details_table.get_children():
            self.customer_details_table.delete(item)

        for row in fetched_result:
            self.customer_details_table.insert('', END, values=row)

    def search_customer(self):
        customer_id = self.search_entry.get()
        if not customer_id == "":
            customer = Customer(customer_id=customer_id)

            searched_data = search_customer(customer)
            if len(searched_data) != 0 :
                for item in self.customer_details_table.get_children():
                    self.customer_details_table.delete(item)

                for row in searched_data:
                    self.customer_details_table.insert('', END, values=row)
            else:
                messagebox.showerror("ERROR", f"Customer with customer ID {customer_id} doesn't exists.", parent = self.customer_details_window)

        else:
            messagebox.showerror("ERROR", "Please Provide Customer ID", parent = self.customer_details_window)

if __name__ == '__main__':
    window = Tk()
    customerDetails = CustomerDetails(window)
    customerDetails.show_customer_details_window()
    window.mainloop()