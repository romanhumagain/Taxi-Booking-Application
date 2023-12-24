import tkinter.ttk
from tkinter import *
from tkcalendar import DateEntry
import customtkinter
from Controller.booking_dbms import *
from PIL import Image, ImageTk
from tkinter import  messagebox
from Model import Global

class ApprovedBooking:
    def __init__(self, frame):
        self.frame = frame
        self.font = "Century Gothic"

    def show_approved_booking_window(self):
        self.approved_booking_window = Toplevel(self.frame, bg="#3c3c3c")
        self.approved_booking_window.title("Approved Booking")
        self.approved_booking_window.resizable(0,0)

        screen_width = self.approved_booking_window.winfo_screenwidth()
        screen_height = self.approved_booking_window.winfo_screenheight()

        window_width = 900
        window_height = 560

        x_position = (screen_width - window_width) // 2 + 140
        y_position = (screen_height - window_height) // 2 +45

        self.approved_booking_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # creating a frame to show the booking form content

        self.approved_booking_window.focus_force()
        self.approved_booking_window.attributes('-topmost', True)
        self.approved_booking_window.attributes('-topmost', False)

        self.approved_frame = Frame(self.approved_booking_window, bg="#2c2c2c", height=220)
        self.approved_frame.pack(side="top", fill="x")

        self.heading_label = Label(self.approved_frame, text="Approved Booking !",
                                   font=(self.font, 20), bg="#2c2c2c", fg="white")
        self.heading_label.place(relx=0.5, rely=0.1, anchor="center")

        heading_icon = ImageTk.PhotoImage(Image.open("Images/approved.png"))
        self.heading_icon_label = Label(self.approved_frame, image=heading_icon, bg='#2c2c2c')
        self.heading_icon_label.image = heading_icon
        # self.heading_icon_label.place(x=280, y=0)

        # Creating a textvariable for the entry box
        self.bookingId = StringVar()
        self.pickUpAddress = StringVar()
        self.pickUpDate = StringVar()
        self.pickUpTime = StringVar()
        self.dropOffAddress = StringVar()
        self.driverId = StringVar()



        self.address_label = Label(self.approved_frame, text="Pick Up Address", fg="white", bg="#2c2c2c",
                                     font=(self.font, 8))
        self.address_label.place(x=25, y=70)

        self.address_entry = customtkinter.CTkEntry(master=self.approved_frame, font=(self.font, 15),
                                                      width=170, placeholder_text="Drop Up Address", height=40, textvariable=self.pickUpAddress, state="readonly")
        self.address_entry.place(x=25, y=90)

        self.date_label = Label(self.approved_frame, text="Pick Up Date", fg="white", bg="#2c2c2c",
                                   font=(self.font, 8))
        self.date_label.place(x=230, y=70)

        self.date_entry = customtkinter.CTkEntry(master=self.approved_frame, font=(self.font, 15),
                                                    width=150, placeholder_text="Drop Up Date", height=40, textvariable=self.pickUpDate, state="readonly")
        self.date_entry.place(x=230, y=90)

        self.time_label = Label(self.approved_frame, text="Pick Up Time", fg="white", bg="#2c2c2c",
                                font=(self.font, 8))
        self.time_label.place(x=410, y=70)

        self.time_entry = customtkinter.CTkEntry(master=self.approved_frame, font=(self.font, 15),
                                                 width=150, placeholder_text="Drop Up Time", height=40, state="readonly", textvariable=self.pickUpTime)
        self.time_entry.place(x=410, y=90)

        self.dropoff_address_label = Label(self.approved_frame, text="Drop Off Address", fg="white", bg="#2c2c2c",
                                font=(self.font, 8))
        self.dropoff_address_label.place(x=590, y=70)

        self.dropoff_address_entry = customtkinter.CTkEntry(master=self.approved_frame, font=(self.font, 15),
                                                 width=170, placeholder_text="Drop Off Address", height=40, textvariable=self.dropOffAddress, state="readonly")
        self.dropoff_address_entry.place(x=590, y=90)

        self.driverid_label = Label(self.approved_frame, text="Driver ID", fg="white", bg="#2c2c2c",
                                           font=(self.font, 8))
        self.driverid_label.place(x=790, y=70)

        self.driverid_entry = customtkinter.CTkEntry(master=self.approved_frame, font=(self.font, 15),
                                                            width=80, placeholder_text="Driver ID", height=40,
                                                            textvariable=self.driverId, state="readonly")
        self.driverid_entry.place(x=790, y=90)

        exit_btn_image = ImageTk.PhotoImage(Image.open("Images/clear.png").resize((20,20), Image.ANTIALIAS))

        self.exit_button = customtkinter.CTkButton(master=self.approved_frame, image=exit_btn_image, text="Exit",
                                                     font=(self.font, 16, 'bold'), corner_radius=10, height=40, command=self.exit)
        self.exit_button.place(x=360, y=160)

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


        self.table_frame = Frame(self.approved_booking_window, bg="#2c2c2c", height=293)
        self.table_frame.pack(side="bottom", fill="x")

        # To show the table in the window
        # To show the vertical scroll bar in the table
        scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        #
        self.booking_records_table = tkinter.ttk.Treeview(self.table_frame, height=13, columns=("bookingid", "pickupaddress", "pickupdate", "pickuptime","dropoffaddress","driverid"), show="headings", yscrollcommand=scroll_y)
        scroll_y.pack(side="right", fill="y")


        # for the heading section

        self.booking_records_table.heading("bookingid", text="Booking ID",anchor=CENTER)
        self.booking_records_table.heading("pickupaddress", text="Pick Up Address",anchor=CENTER)
        self.booking_records_table.heading("pickupdate", text="Pick Up Date",anchor=CENTER)
        self.booking_records_table.heading("pickuptime", text="Pick Up Time",anchor=CENTER)
        self.booking_records_table.heading("dropoffaddress", text="Drop Off Address",anchor=CENTER)
        self.booking_records_table.heading("driverid", text="Driver ID", anchor=CENTER)

        # Configuring the style of the headings
        self.booking_records_table.tag_configure("Treeview.Heading", background="black", foreground="white")

        # for the column section
        self.booking_records_table.column("bookingid", width=50,anchor=CENTER)
        self.booking_records_table.column("pickupaddress", width=100,anchor=CENTER)
        self.booking_records_table.column("pickupdate", width=100,anchor=CENTER)
        self.booking_records_table.column("pickuptime", width=100,anchor=CENTER)
        self.booking_records_table.column("dropoffaddress", width=100,anchor=CENTER)
        self.booking_records_table.column("driverid", width=50,anchor=CENTER)


        self.booking_records_table.pack(fill=X, expand=0)
        self.booking_records_table.bind("<ButtonRelease-1>", self.fill_data)

        # ======== TO GET THE RESULT FROM THE CONTROLLER ============
        self.display_data()

    def display_data(self):
        booking =Booking(customer_id=Global.logged_in_customer[0])
        result = select_approved_booking(booking)
        print(result)
        if result is not None:
            self.booking_records_table.delete(*self.booking_records_table.get_children())

            for row in result:
                self.booking_records_table.insert('', END, values=row)
        pass

    def fill_data(self,event):
        view_info = self.booking_records_table.focus()
        customer_info = self.booking_records_table.item(view_info)

        row = customer_info.get('values')

        self.bookingId.set(row[0])
        self.pickUpAddress.set(row[1])
        self.pickUpDate.set(row[2])
        self.pickUpTime.set(row[3])
        self.dropOffAddress.set(row[4])
        self.driverId.set(row[5])

    def exit(self):
        self.approved_booking_window.destroy()


if __name__ == '__main__':
    window = Tk()
    approvedBooking = ApprovedBooking(window)
    approvedBooking.show_approved_booking_window()
    window.mainloop()