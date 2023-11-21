import tkinter.ttk
from tkinter import *
import customtkinter

class PaymentFrame():
    def __init__(self, frame):
        self.frame = frame
        self.font = "Century Gothic"

    def show_payment_frame(self):
        self.payment_frame = Frame(self.frame, bg="white", width=850, height=600)
        self.payment_frame.place(x=0, y=0)

        self.top_frame = Frame(self.payment_frame, bg="#2c2c2c")
        self.top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.27)

        self.heading_label = Label(self.top_frame, text="Payment Details", font=(self.font, 26), bg="#2c2c2c",
                                   fg="white")
        self.heading_label.place(relx=0.5, rely=0.35, anchor="center")

        self.download_button = customtkinter.CTkButton(master=self.top_frame, text="Download Receipt",
                                                    font=(self.font, 15), corner_radius=10, height=34, width=40)
        self.download_button.place(x=350, y=100)

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


        self.table_frame = Frame(self.payment_frame, bg="white", width=850, height=450)
        self.table_frame.place(x=0, y=160)

        self.payment_detals_table = tkinter.ttk.Treeview(self.table_frame, height= 16, show="headings", columns=("payment_id","booking_id","pickupaddreess", "dropoffaddress","distance", "unit","total_amount", "date"))

        self.payment_detals_table.heading("payment_id", text="Invoice_no", anchor=CENTER)
        self.payment_detals_table.heading("booking_id", text="B_ID", anchor=CENTER)
        self.payment_detals_table.heading("pickupaddreess", text="Pickup Address", anchor=CENTER)
        self.payment_detals_table.heading("dropoffaddress", text="Dropoff Address", anchor=CENTER)
        self.payment_detals_table.heading("distance", text="Distance", anchor=CENTER)
        self.payment_detals_table.heading("unit", text="Unit", anchor=CENTER)
        self.payment_detals_table.heading("total_amount", text="Amount", anchor=CENTER)
        self.payment_detals_table.heading("date", text="Date", anchor=CENTER)


        self.payment_detals_table.column("payment_id", width=100, anchor=CENTER)
        self.payment_detals_table.column("booking_id",  width=50, anchor=CENTER)
        self.payment_detals_table.column("pickupaddreess",  width=190, anchor=CENTER)
        self.payment_detals_table.column("dropoffaddress",  width=190, anchor=CENTER)
        self.payment_detals_table.column("distance",  width=90, anchor=CENTER)
        self.payment_detals_table.column("unit",  width=60, anchor=CENTER)
        self.payment_detals_table.column("total_amount",  width=120, anchor=CENTER)
        self.payment_detals_table.column("date",  width=50, anchor=CENTER)


        self.payment_detals_table.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = Tk()
    root.geometry("850x600")
    main_frame = Frame(root, bg="white", width=850, height=600)
    main_frame.place(x=0, y=0)

    payment_frame_instance = PaymentFrame(main_frame)
    payment_frame_instance.show_payment_frame()

    root.mainloop()
