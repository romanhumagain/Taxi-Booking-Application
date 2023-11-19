import tkinter.ttk
from tkinter import *
from tkinter import messagebox
from Model.booking import Booking
from Model import Global
from Controller.booking_dbms import select_all_booking

class BookingHistory():
    def __init__(self, frame):
        self.frame = frame
        self.font = "Century Gothic"

    def show_booking_history_window(self):
        self.booking_history_window = Toplevel(self.frame,bg="#2c2c2c", width=850)
        self.booking_history_window.title("Booking History")
        self.booking_history_window.resizable(0, 0)

        screen_width = self.booking_history_window.winfo_screenwidth()
        screen_height = self.booking_history_window.winfo_screenheight()

        window_width = 850
        window_height = 500

        x_position = (screen_width - window_width) // 2 + 140
        y_position = (screen_height - window_height) // 2

        self.top_frame = Frame(self.booking_history_window, bg="#2c2c2c", height=80)
        self.top_frame.pack(side="top", fill = "x")

        self.booking_history_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.heading_label = Label(self.top_frame, text="Booking History",
                                   font=(self.font, 24), bg="#2c2c2c", fg="white")
        self.heading_label.place(relx=0.5, rely=0.5, anchor="center")

        # CREATING A FRAME TO SHOW THE BOOKING HISTORY TABLE


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
                   foreground = [('active', 'black')])

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
                   foreground = [('active', 'white')])

        self.table_frame = Frame(self.booking_history_window, bg='white', width=850, height=350)
        self.table_frame.pack(side= "bottom", fill ="x")

        # ========== CREATE A SCROLLBAR FOR THE TABLE ============
        scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)

        self.booking_records_table = tkinter.ttk.Treeview(self.table_frame, height=17, columns = ("bookingid", "pickupaddress", "pickupdate", "pickuptime", "dropoffaddress", "status","driverid" ), show="headings", yscrollcommand=scroll_y)
        scroll_y.pack(side="right", fill="y")

        self.booking_records_table.pack(fill = X, expand =0)

        # ========= TO SET THE HEADINGS FOR THE TABLE ===========
        self.booking_records_table.heading("bookingid", text="Booking ID", anchor=CENTER)
        self.booking_records_table.heading("pickupaddress", text="Pick Up Address", anchor=CENTER)
        self.booking_records_table.heading("pickupdate", text="Pick Up Date", anchor=CENTER)
        self.booking_records_table.heading("pickuptime", text="Pick Up Time", anchor=CENTER)
        self.booking_records_table.heading("dropoffaddress", text="Drop Up Address", anchor=CENTER)
        self.booking_records_table.heading("status", text="Status", anchor=CENTER)
        self.booking_records_table.heading("driverid", text="Driver ID", anchor=CENTER)

        # =============== TO SET THE COLUMN FOR THE TABLE ===================
        self.booking_records_table.column("bookingid", width=50, anchor=CENTER)
        self.booking_records_table.column("pickupaddress", width=100, anchor=CENTER)
        self.booking_records_table.column("pickupdate", width=100, anchor=CENTER)
        self.booking_records_table.column("pickuptime", width=80, anchor=CENTER)
        self.booking_records_table.column("dropoffaddress", width=100, anchor=CENTER)
        self.booking_records_table.column("status", width=100, anchor=CENTER)
        self.booking_records_table.column("driverid", width=50, anchor=CENTER)

        self.display_data()

    def display_data(self):
        booking = Booking(customer_id=97)
        result = select_all_booking(booking)

        # first clear the data in the table
        for item in self.booking_records_table.get_children():
            self.booking_records_table.delete(item)

        # Insert the data in the table
        for row in result:
            self.booking_records_table.insert('', END , values=row)

if __name__ == '__main__':
    window = Tk()
    approvedBooking = BookingHistory(window)
    approvedBooking.show_booking_history_window()
    window.mainloop()


