import tkinter.ttk
from tkinter import *
from tkinter import messagebox

import customtkinter
from PIL import ImageTk, Image

from Controller.driver_dbms import get_assigned_driver_details, search_assigned_driver
from Model import Global
from Model.customer import Customer
from Model.driver import Driver


class DriverFrame(Frame):
    def __init__(self, frame):
        self.frame = frame
        self.font = "Century Gothic"

    def show_driver_frame(self):
        self.driver_frame = Frame(self.frame, bg="white", width=900, height=600)
        self.driver_frame.place(x=0, y=0)

        self.top_frame = Frame(self.driver_frame, bg="#2c2c2c")
        self.top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.25)

        self.heading_label = Label(self.top_frame, text="Driver Details", font=(self.font, 26), bg="#2c2c2c",
                                   fg="white")
        self.heading_label.place(relx=0.5, rely=0.3, anchor="center")

        self.search_entry = customtkinter.CTkEntry(master=self.top_frame, width=100, height=36,
                                                   placeholder_text="Driver ID")
        self.search_entry.place(x=20, y=90)

        search_btn_image = ImageTk.PhotoImage(Image.open("Images/search.png").resize((20, 20), Image.ANTIALIAS))

        self.search_button = customtkinter.CTkButton(master=self.top_frame, width=60, height=35, text="search",
                                                     corner_radius=15, font=(self.font, 15), image=search_btn_image,command=self.search_driver_details
                                                     )
        self.search_button.place(x=130, y=92)


        # table to show the driver details

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
                         font=('Century Gothic', 11),
                         padding=(0, 8)
                         )

        style1.map("Treeview.Heading",
                   background=[('active', '#3c3c3c')],
                   foreground=[('active', 'white')])


        self.table_frame = Frame(self.driver_frame, bg="white", width=900, height=504)
        self.table_frame.place(x=0, y=150)

        self.driver_Detals_table = tkinter.ttk.Treeview(self.table_frame, height=24, show="headings", columns=("driver_id","name","phone_no", "address","pickupaddress", "dropoffaddress","date", "status"))

        self.driver_Detals_table.heading("driver_id", text="ID", anchor=CENTER)
        self.driver_Detals_table.heading("name", text="Name", anchor=CENTER)
        self.driver_Detals_table.heading("phone_no", text="Phone No.", anchor=CENTER)
        self.driver_Detals_table.heading("address", text="Address", anchor=CENTER)
        self.driver_Detals_table.heading("pickupaddress", text="Pickup Address", anchor=CENTER)
        self.driver_Detals_table.heading("dropoffaddress", text="Dropoff Address", anchor=CENTER)
        self.driver_Detals_table.heading("date", text="Date", anchor=CENTER)
        self.driver_Detals_table.heading("status", text="Status", anchor=CENTER)


        self.driver_Detals_table.column("driver_id", width=50, anchor=CENTER)
        self.driver_Detals_table.column("name",  width=110, anchor=CENTER)
        self.driver_Detals_table.column("phone_no",  width=100, anchor=CENTER)
        self.driver_Detals_table.column("address",  width=115, anchor=CENTER)
        self.driver_Detals_table.column("pickupaddress",  width=175, anchor=CENTER)
        self.driver_Detals_table.column("dropoffaddress",  width=175, anchor=CENTER)
        self.driver_Detals_table.column("date",  width=75, anchor=CENTER)
        self.driver_Detals_table.column("status",  width=100, anchor=CENTER)


        self.driver_Detals_table.pack(fill="both", expand=True)

        self.display_driver_data()

    def display_driver_data(self):
        customer = Customer(Global.logged_in_customer[0])
        result = get_assigned_driver_details(customer)

        for item in self.driver_Detals_table.get_children():
            self.driver_Detals_table.delete(item)

        for row in result:
            self.driver_Detals_table.insert('', END, values=row)

    def search_driver_details(self):
        driver_id = self.search_entry.get()
        if driver_id != "":
            driver = Driver(driver_id = driver_id)
            customer = Customer(customer_id=Global.logged_in_customer[0])
            result = search_assigned_driver(customer,driver)

            if len(result) != 0 :
                for item in self.driver_Detals_table.get_children():
                    self.driver_Detals_table.delete(item)

                for row in result:
                    self.driver_Detals_table.insert('', END, values=row)
            else:
                messagebox.showerror("INVALID DATA", f"Sorry Driver With Driver ID {driver_id} Doesn't Exists")
        else:
            messagebox.showerror("INVALID", f"Please Provide Driver ID To Search Driver Details.")


if __name__ == "__main__":
    root = Tk()
    root.geometry("850x600")
    main_frame = Frame(root, bg="white", width=850, height=600)
    main_frame.place(x=0, y=0)

    driver_frame_instance = DriverFrame(main_frame)
    driver_frame_instance.show_driver_frame()

    root.mainloop()
