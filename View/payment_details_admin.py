import tkinter
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from tkinter.ttk import Treeview

import customtkinter
from Controller.payment_dbms import fetch_pending_payment, fetch_pending_payment_details, generate_payment, \
    fetch_completed_payment
from datetime import datetime

from Model.payment import Payment
from View.Invoice import InvoiceFrame


class PaymentDetails:
    def __init__(self, window,top_levels= []):
        self.window = window
        self.font = "Century Gothic"
        if top_levels is None:
            self.top_levels = top_levels
        self.top_levels = top_levels

        date_time = datetime.now()
        self.date = date_time.date()

        self.bill_no =0

        style1 = tkinter.ttk.Style()
        style1.theme_use("default")
        style1.configure("Treeview",
                         background="#F4F4F4",
                         foreground="black",
                         rowheight=25,
                         fieldbackground="#F5F5F5",
                         bordercolor="black",
                         borderwidth=0,
                         font=(self.font, 11))
        style1.map('Treeview', background=[('selected', '#7EC8E3')],
                   foreground=[('active', 'black')])

        #
        style1.configure("Treeview.Heading",
                         background="#4c4c4c",
                         foreground="white",
                         relief="flat",
                         font=('Century Gothic', 11),
                         padding=(0, 6)
                         )

        style1.map("Treeview.Heading",
                   background=[('active', '#3c3c3c')],
                   foreground=[('active', 'white')])

    def show_payment_details_window(self):
        self.payment_details_window = Toplevel(self.window, bg="#3c3c3c")
        self.payment_details_window.title("Payment Management Portal")
        self.payment_details_window.resizable(False, False)

        self.top_levels.append(self.payment_details_window)

        width = 900
        height = 520

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x_position = (screen_width - width) // 2 + 140
        y_position = (screen_height - height) // 2

        self.payment_details_window.geometry(f"{width}x{height}+{x_position}+{y_position}")

        self.top_frame = customtkinter.CTkFrame(self.payment_details_window, width=880, height=80, corner_radius=20)
        self.top_frame.place(x=10, y=20)

        self.heading_label = customtkinter.CTkLabel(self.top_frame, text="Payment Management Portal",
                                                    font=(self.font, 30))
        self.heading_label.place(relx=0.5, rely=0.5, anchor="center")

        self.tab_frame = customtkinter.CTkFrame(self.payment_details_window,width=880, height=395, corner_radius=10)
        self.tab_frame.place(x=10, y=120)


        self.tab_view = customtkinter.CTkTabview(self.tab_frame, width=870, height=397, corner_radius=15)
        self.tab_view.place(x=5, y= -10)

        self.generate_tab = self.tab_view.add("Generate Invoice")
        self.pending_tab = self.tab_view.add("Pending Payment")
        self.completed_tab = self.tab_view.add("Completed Payment")


        # to set the currently visible tab
        self.tab_view.set("Generate Invoice")

        self.payment_frame = customtkinter.CTkFrame(self.generate_tab, width=350, height=400)
        self.payment_frame.place(x=0, y=10)

        self.booking_id = customtkinter.CTkLabel(self.payment_frame, text="Booking ID", font=(self.font, 10))
        self.booking_id.place(x=20, y=10)

        self.bookingid_entry = customtkinter.CTkEntry(self.payment_frame, width=140, height=36, font=(self.font, 13),
                                                      placeholder_text="Booking ID")
        self.bookingid_entry.place(x=20, y=35)

        self.customer_id = customtkinter.CTkLabel(self.payment_frame, text="Customer ID", font=(self.font, 10))
        self.customer_id.place(x=200, y=10)

        self.customerid_entry = customtkinter.CTkEntry(self.payment_frame, width=140, height=36, font=(self.font, 13),
                                                       placeholder_text="Customer ID")
        self.customerid_entry.place(x=200, y=35)

        self.pickup_address = customtkinter.CTkLabel(self.payment_frame, text="Pickup Address", font=(self.font, 10))
        self.pickup_address.place(x=20, y=95)

        self.pickup_address_entry = customtkinter.CTkEntry(self.payment_frame, width=140, height=35, font=(self.font, 13),
                                                           placeholder_text="Pickup Address")
        self.pickup_address_entry.place(x=20, y=120)

        self.dropoff_address = customtkinter.CTkLabel(self.payment_frame, text="Dropoff Address", font=(self.font, 10))
        self.dropoff_address.place(x=200, y=95)

        self.dropoff_address_entry = customtkinter.CTkEntry(self.payment_frame, width=140, height=35,
                                                            font=(self.font, 13), placeholder_text="Dropoff Address")
        self.dropoff_address_entry.place(x=200, y=120)

        self.km = customtkinter.CTkLabel(self.payment_frame, text="K.M", font=(self.font, 10))
        self.km.place(x=20, y=183)

        # Use a StringVar to store the value of the Spinbox
        self.km_var = StringVar()
        self.km_spinbox = Spinbox(self.payment_frame, from_=0, to=1000, width=5, font=(self.font, 16),
                                  textvariable=self.km_var)
        self.km_spinbox.place(x=20, y=208)

        # Trace the changes to the StringVar and call the update_total_amount method
        self.km_var.trace_add('write', lambda *args: self.update_total_amount())

        self.total_amount = customtkinter.CTkLabel(self.payment_frame, text="Total Amount", font=(self.font, 10))
        self.total_amount.place(x=200, y=180)

        self.total_amount_entry = customtkinter.CTkEntry(self.payment_frame, width=140, height=35, font=(self.font, 13),
                                                 placeholder_text="Amount")
        self.total_amount_entry.place(x=200, y=205)

        generate_payment_btn_image = ImageTk.PhotoImage(
            Image.open("Images/payment1.png").resize((25, 25), Image.ANTIALIAS))

        self.generate_payment_button = customtkinter.CTkButton(self.payment_frame, text="Generate Bill",
                                                               font=(self.font, 18), corner_radius=15,
                                                                height=34,
                                                               image=generate_payment_btn_image, command=self.generate_bill)
        self.generate_payment_button.place(relx=0.5, rely=0.72, anchor="center")

        self.table_frame = customtkinter.CTkFrame(self.generate_tab, width=500, height=400)
        self.table_frame.place(x=360, y=10)
        self.generate_bill_table =Treeview(
            self.table_frame,
            columns=("booking_id", "customer_id", "pickup_address", "dropoff_address","date"),
            show="headings",
            height=15,
        )
        self.generate_bill_table.place(x=0, y=0)
        # self.generate_bill_table.bind("<ButtonRelease-1>", self.select_booking)

        self.generate_bill_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.generate_bill_table.heading("customer_id", text="C-ID", anchor=CENTER)
        self.generate_bill_table.heading("pickup_address", text="Pickup", anchor=CENTER)
        self.generate_bill_table.heading("dropoff_address", text="Dropoff", anchor=CENTER)
        self.generate_bill_table.heading("date", text="Date", anchor=CENTER)

        self.generate_bill_table.column("booking_id", width=40, anchor=CENTER)
        self.generate_bill_table.column("customer_id", width=40, anchor=CENTER)
        self.generate_bill_table.column("pickup_address", width=165, anchor=CENTER)
        self.generate_bill_table.column("dropoff_address", width=165, anchor=CENTER)
        self.generate_bill_table.column("date", width=70, anchor=CENTER)

        self.generate_bill_table.bind("<ButtonRelease-1>", self.select_pending_payment)
        self.get_pending_payment()

        # ====== frame to show the pending payement details ===============
        self.pending_payment_frame = customtkinter.CTkFrame(self.pending_tab, width=840, height=330, corner_radius=15)
        self.pending_payment_frame.place(x=0,y=0)

        self.pending_payment_table = tkinter.ttk.Treeview(
            self.pending_payment_frame,
            columns=("booking_id", "customer_id", "customer_name", "pickup_address", "dropoff_address","date","payment_status"),
            show="headings",
            height=14,
        )

        self.pending_payment_table.place(x=0, y=0)
        # self.pending_payment_table.bind("<ButtonRelease-1>", self.select_booking)

        self.pending_payment_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.pending_payment_table.heading("customer_id", text="C-ID", anchor=CENTER)
        self.pending_payment_table.heading("customer_name", text="Name", anchor=CENTER)
        self.pending_payment_table.heading("pickup_address", text="Pickup Address", anchor=CENTER)
        self.pending_payment_table.heading("dropoff_address", text="Dropoff Address", anchor=CENTER)
        self.pending_payment_table.heading("date", text="Date", anchor=CENTER)
        self.pending_payment_table.heading("payment_status", text="Status", anchor=CENTER)

        self.pending_payment_table.column("booking_id", width=50, anchor=CENTER)
        self.pending_payment_table.column("customer_id", width=50, anchor=CENTER)
        self.pending_payment_table.column("customer_name", width=110, anchor=CENTER)
        self.pending_payment_table.column("pickup_address", width=210, anchor=CENTER)
        self.pending_payment_table.column("dropoff_address", width=210, anchor=CENTER)
        self.pending_payment_table.column("date", width=100, anchor=CENTER)
        self.pending_payment_table.column("payment_status", width=110, anchor=CENTER)

        self.get_pending_payment_details()

        # ====== frame to show the completed payement details ===============
        self.completed_payment_frame = customtkinter.CTkFrame(self.completed_tab, width=840, height=290, corner_radius=15)
        self.completed_payment_frame.place(x=0, y=50)

        download_bill_btn_image = ImageTk.PhotoImage(
            Image.open("Images/download.png").resize((17, 17), Image.ANTIALIAS))

        self.download_bill_button = customtkinter.CTkButton(self.completed_tab,
                                                               font=(self.font, 18), corner_radius=15,text="",width=30,
                                                               height=34,
                                                               image=download_bill_btn_image,command=self.print_invoice)
        self.download_bill_button.place(x=780, y=0)

        self.completed_payment_table = tkinter.ttk.Treeview(
            self.completed_payment_frame,
            columns=("bill_id","booking_id","pickup_address", "dropoff_address", "date","km",
                     "total_amount"),
            show="headings",
            height=10,
        )

        self.completed_payment_table.place(x=0, y=0)
        self.completed_payment_table.bind("<ButtonRelease-1>", self.select_payment_details)

        self.completed_payment_table.heading("bill_id", text="Bill No.", anchor=CENTER)
        self.completed_payment_table.heading("booking_id", text="B-ID", anchor=CENTER)
        self.completed_payment_table.heading("pickup_address", text="Pickup Address", anchor=CENTER)
        self.completed_payment_table.heading("dropoff_address", text="Dropoff Address", anchor=CENTER)
        self.completed_payment_table.heading("date", text="Bill Date", anchor=CENTER)
        self.completed_payment_table.heading("km", text="K.M", anchor=CENTER)
        self.completed_payment_table.heading("total_amount", text="Total Amount", anchor=CENTER)


        self.completed_payment_table.column("bill_id", width=80, anchor=CENTER)
        self.completed_payment_table.column("booking_id", width=50, anchor=CENTER)
        self.completed_payment_table.column("pickup_address", width=200, anchor=CENTER)
        self.completed_payment_table.column("dropoff_address", width=200, anchor=CENTER)
        self.completed_payment_table.column("date", width=100, anchor=CENTER)
        self.completed_payment_table.column("km", width=80, anchor=CENTER)
        self.completed_payment_table.column("total_amount", width=140, anchor=CENTER)

        self.get_completed_payment_details()

    # to update the total amount automatically
    def update_total_amount(self):
        km = self.km_spinbox.get()
        if km != "":
            km_value = float(km)  # Retrieve the value from the Spinbox
            cost_per_km = 100

            total_amount = km_value * cost_per_km

            self.total_amount_entry.delete(0, END)
            self.total_amount_entry.insert(0, f"{total_amount:.2f}")
    def get_pending_payment(self):
        result = fetch_pending_payment()

        if result is not None:
            for item in self.generate_bill_table.get_children():
                self.generate_bill_table.delete(item)
            for row in result:
                self.generate_bill_table.insert('', END, values=row)

    def select_pending_payment(self, event):
        self.clear_fields()

        value_info = self.generate_bill_table.focus()
        payment_details = self.generate_bill_table.item(value_info)

        row = payment_details.get('values')
        if row != "":
            self.bookingid_entry.insert(0, row[0])
            self.customerid_entry.insert(0, row[1])
            self.pickup_address_entry.insert(0, row[2])
            self.dropoff_address_entry.insert(0, row[3])

    def clear_fields(self):
        self.bookingid_entry.delete(0, END)
        self.customerid_entry.delete(0, END)
        self.pickup_address_entry.delete(0, END)
        self.dropoff_address_entry.delete(0, END)
        self.km_spinbox.delete(0, END)
        self.total_amount_entry.delete(0, END)


    def get_pending_payment_details(self):
        result = fetch_pending_payment_details()

        if result is not None:
            for item in self.pending_payment_table.get_children():
                self.pending_payment_table.delete(item)
            for row in result:
                self.pending_payment_table.insert('', END, values=row)

    def get_completed_payment_details(self):
        result = fetch_completed_payment()

        if result is not None:
            for item in self.completed_payment_table.get_children():
                self.completed_payment_table.delete(item)
            for row in result:
                self.completed_payment_table.insert('', END, values=row)

    def generate_bill(self):
        booking_id = self.bookingid_entry.get()
        current_date = self.date
        distance = self.km_spinbox.get()
        total_amount = self.total_amount_entry.get()
        is_generated = True

        if not (booking_id == "" or distance == "" or total_amount == ""):
            payment = Payment(distance=distance, total_amount=total_amount, is_generated= is_generated, date=current_date, booking_id=booking_id)
            generated = generate_payment(payment)
            if generated:
                messagebox.showinfo("SUCCESS", f"Successfully Generated Bill For The Booking ID {booking_id}",parent = self.payment_details_window)
                self.get_pending_payment()
            else:
                messagebox.showerror("ERROR", "Sorry, Couldn't Generate Bill", parent=self.payment_details_window)
        else:
            messagebox.showerror("ERROR", "Please Fill All The Details", parent = self.payment_details_window)



    def select_payment_details(self, event):
        value = self.completed_payment_table.focus()
        payment_details = self.completed_payment_table.item(value)

        row = payment_details.get('values')
        self.bill_no = row[0]

    def print_invoice(self):
        print(self.bill_no)
        if self.bill_no !=0:
            invoiceFrame = InvoiceFrame(self.payment_frame, self.bill_no)
            invoiceFrame.show_invoice_window()

            screen_width = self.payment_frame.winfo_screenwidth()
            screen_height = self.payment_frame.winfo_screenheight()

            window_width = 550
            window_height = 500

            x_position = (screen_width - window_width) // 2 + 150
            y_position = (screen_height - window_height) // 2

            invoiceFrame.invoice_frame.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        else:
            messagebox.showerror("ERROR", "Please Select The Payment Details From The Table To Print Invoice!", parent = self.payment_details_window)


if __name__ == '__main__':
    window = Tk()
    paymentDetails = PaymentDetails(window)
    paymentDetails.show_payment_details_window()
    window.mainloop()