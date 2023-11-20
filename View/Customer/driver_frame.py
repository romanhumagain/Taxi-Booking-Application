import tkinter.ttk
from tkinter import *

class DriverFrame(Frame):
    def __init__(self, frame):
        self.frame = frame
        self.font = "Century Gothic"

    def show_driver_frame(self):
        self.driver_frame = Frame(self.frame, bg="white", width=850, height=600)
        self.driver_frame.place(x=0, y=0)

        self.top_frame = Frame(self.driver_frame, bg="#2c2c2c")
        self.top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.19)

        self.heading_label = Label(self.top_frame, text="Driver Details", font=(self.font, 26), bg="#2c2c2c",
                                   fg="white")
        self.heading_label.place(relx=0.5, rely=0.5, anchor="center")

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


        self.table_frame = Frame(self.driver_frame, bg="red", width=850, height=504)
        self.table_frame.place(x=0, y=110)

        self.driver_Detals_table = tkinter.ttk.Treeview(self.table_frame, height=24, show="headings", columns=("driver_id","name","phone_no", "address","pickupaddress", "dropoffaddress","date", "time"))

        self.driver_Detals_table.heading("driver_id", text="ID", anchor=CENTER)
        self.driver_Detals_table.heading("name", text="Name", anchor=CENTER)
        self.driver_Detals_table.heading("phone_no", text="Phone No.", anchor=CENTER)
        self.driver_Detals_table.heading("address", text="Address", anchor=CENTER)
        self.driver_Detals_table.heading("pickupaddress", text="Pickup Address", anchor=CENTER)
        self.driver_Detals_table.heading("dropoffaddress", text="Dropoff Address", anchor=CENTER)
        self.driver_Detals_table.heading("date", text="Date", anchor=CENTER)
        self.driver_Detals_table.heading("time", text="Time", anchor=CENTER)


        self.driver_Detals_table.column("driver_id", width=50, anchor=CENTER)
        self.driver_Detals_table.column("name",  width=100, anchor=CENTER)
        self.driver_Detals_table.column("phone_no",  width=100, anchor=CENTER)
        self.driver_Detals_table.column("address",  width=100, anchor=CENTER)
        self.driver_Detals_table.column("pickupaddress",  width=175, anchor=CENTER)
        self.driver_Detals_table.column("dropoffaddress",  width=175, anchor=CENTER)
        self.driver_Detals_table.column("date",  width=75, anchor=CENTER)
        self.driver_Detals_table.column("time",  width=75, anchor=CENTER)


        self.driver_Detals_table.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = Tk()
    root.geometry("850x600")
    main_frame = Frame(root, bg="white", width=850, height=600)
    main_frame.place(x=0, y=0)

    driver_frame_instance = DriverFrame(main_frame)
    driver_frame_instance.show_driver_frame()

    root.mainloop()
