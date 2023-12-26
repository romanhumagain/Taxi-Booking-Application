import tkinter.ttk
from tkinter import *
from tkinter import messagebox

import customtkinter
from PIL import ImageTk, Image

from Controller.payment_dbms import fetch_customer_completed_payment, search_customer_completed_payment
from Model import Global
from Model.customer import Customer
from Model.payment import Payment


class PaymentFrame():
    def __init__(self, frame):
        self.frame = frame
        self.font = "Century Gothic"

    def show_payment_frame(self):
        self.payment_frame = Frame(self.frame, bg="#3c3c3c", width=900, height=600)
        self.payment_frame.place(x=0, y=0)

        self.top_frame = customtkinter.CTkFrame(self.payment_frame,width=870, height=110, corner_radius=25 )
        self.top_frame.place(x=15, y=10)

        self.heading_label = customtkinter.CTkLabel(self.top_frame, text="Payment Details", font=(self.font, 30),
                                   )
        self.heading_label.place(relx=0.5, rely=0.5, anchor="center")

        self.search_entry = customtkinter.CTkEntry(master=self.payment_frame, width=100, height=36,
                                                   placeholder_text="Invoice No.")
        self.search_entry.place(x=20, y=140)

        search_btn_image = ImageTk.PhotoImage(Image.open("Images/search.png").resize((20, 20), Image.ANTIALIAS))

        self.search_button = customtkinter.CTkButton(master=self.payment_frame, width=60, height=35, text="Search",
                                                     corner_radius=15, font=(self.font, 15), image=search_btn_image,command=self.search_completed_payment_details
                                                     )
        self.search_button.place(x=130, y=142)

        download_btn_image = ImageTk.PhotoImage(Image.open("Images/download.png").resize((20,20), Image.ANTIALIAS))


        self.download_button = customtkinter.CTkButton(master=self.payment_frame, text="Download Receipt",image=download_btn_image,
                                                    font=(self.font, 15), corner_radius=10, height=34, width=40)
        self.download_button.place(x=360, y=140)

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


        self.table_frame = customtkinter.CTkFrame(self.payment_frame, width=870, height=380, corner_radius=20)
        self.table_frame.place(x=15, y=200)

        self.completed_payment_table = tkinter.ttk.Treeview(
            self.table_frame,
            columns=("bill_id", "booking_id", "pickup_address", "dropoff_address", "date", "distance",
                     "total_amount"),
            show="headings",
            height=14,
        )

        self.completed_payment_table.place(x=0, y=0)

        self.completed_payment_table.heading("bill_id", text="Bill No.", anchor=CENTER)
        self.completed_payment_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.completed_payment_table.heading("pickup_address", text="Pickup Address", anchor=CENTER)
        self.completed_payment_table.heading("dropoff_address", text="Dropoff Address", anchor=CENTER)
        self.completed_payment_table.heading("date", text="Bill Date", anchor=CENTER)
        self.completed_payment_table.heading("distance", text="Distance(KM)", anchor=CENTER)
        self.completed_payment_table.heading("total_amount", text="Total Amount", anchor=CENTER)

        self.completed_payment_table.column("bill_id", width=60, anchor=CENTER)
        self.completed_payment_table.column("booking_id", width=50, anchor=CENTER)
        self.completed_payment_table.column("pickup_address", width=210, anchor=CENTER)
        self.completed_payment_table.column("dropoff_address", width=210, anchor=CENTER)
        self.completed_payment_table.column("date", width=90, anchor=CENTER)
        self.completed_payment_table.column("distance", width=100, anchor=CENTER)
        self.completed_payment_table.column("total_amount", width=150, anchor=CENTER)

        self.get_completed_payment_details()

        # self.pending_booking_table.bind("<ButtonRelease-1>", self.select_booking)

    def get_completed_payment_details(self):
        customer = Customer(customer_id=Global.logged_in_customer[0])
        result = fetch_customer_completed_payment(customer)

        if result is not None:
            for item in self.completed_payment_table.get_children():
                self.completed_payment_table.delete(item)
            for row in result:
                self.completed_payment_table.insert('', END, values=row)

    def search_completed_payment_details(self):
        payment_id = self.search_entry.get()
        if payment_id != "":

            customer = Customer(customer_id=Global.logged_in_customer[0])
            payment = Payment(payment_id=payment_id)

            result = search_customer_completed_payment(customer, payment)

            if len(result) != 0:
                for item in self.completed_payment_table.get_children():
                    self.completed_payment_table.delete(item)
                for row in result:
                    self.completed_payment_table.insert('', END, values=row)
            else:
                messagebox.showerror("ERROR", f"Invoice With ID No. {payment_id} Doesn't Exists !")
        else:
            messagebox.showerror("ERROR", "Please Provide Invoice No. To Search!")



if __name__ == "__main__":
    root = Tk()
    root.geometry("850x600")
    main_frame = Frame(root, bg="white", width=850, height=600)
    main_frame.place(x=0, y=0)

    payment_frame_instance = PaymentFrame(main_frame)
    payment_frame_instance.show_payment_frame()

    root.mainloop()
