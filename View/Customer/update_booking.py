import tkinter.ttk
from tkinter import *
from tkcalendar import DateEntry
import customtkinter
from Controller.booking_dbms import *
from PIL import Image, ImageTk
from tkinter import  messagebox
from Model import Global
class UpdateBooking:
    def __init__(self, frame):
        self.frame = frame
        self.font = "Century Gothic"

    def show_update_booking_window(self):
        self.update_booking_window = Toplevel(self.frame, bg="#3c3c3c")
        self.update_booking_window.title("Update Booking")
        self.update_booking_window.resizable(0,0)

        screen_width = self.update_booking_window.winfo_screenwidth()
        screen_height = self.update_booking_window.winfo_screenheight()

        window_width = 750
        window_height = 480

        x_position = (screen_width - window_width) // 2 + 140
        y_position = (screen_height - window_height) // 2

        self.update_booking_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # creating a frame to show the booking form content

        self.update_booking_window.focus_force()
        self.update_booking_window.attributes('-topmost', True)
        self.update_booking_window.attributes('-topmost', False)

        self.update_frame = Frame(self.update_booking_window, bg="#2c2c2c", height=273)
        self.update_frame.pack(side="top", fill="x")

        self.heading_label = Label(self.update_frame, text="Update Booking Details !",
                                   font=(self.font, 17), bg="#2c2c2c", fg="white")
        self.heading_label.place(relx=0.53, rely=0.085, anchor="center")

        heading_icon = ImageTk.PhotoImage(Image.open("Images/update1.png"))
        self.heading_icon_label = Label(self.update_frame, image=heading_icon, bg='#2c2c2c')
        self.heading_icon_label.image = heading_icon
        self.heading_icon_label.place(x=200, y=0)
        # Creating a textvariable for the entry box
        self.bookingId = StringVar()
        self.pickUpAddress = StringVar()
        self.pickUpDate = StringVar()
        self.pickUpTime = StringVar()
        self.dropOffAddress = StringVar()


        self.bookingid_label = Label(self.update_frame, text="ID", fg="white", bg="#2c2c2c",
                                    font=(self.font, 10), )
        self.bookingid_label.place(x=360, y=49)

        self.bookingid_entry = customtkinter.CTkEntry(master=self.update_frame, font=(self.font, 15),
                                                     width=100, placeholder_text="Booking ID", height=40, textvariable=self.bookingId, state="readonly")
        self.bookingid_entry.place(relx=0.5, rely=0.36, anchor="center")

        self.address_label = Label(self.update_frame, text="Pick Up Address", fg="white", bg="#2c2c2c",
                                     font=(self.font, 8))
        self.address_label.place(x=20, y=130)

        self.address_entry = customtkinter.CTkEntry(master=self.update_frame, font=(self.font, 15),
                                                      width=150, placeholder_text="Drop Up Address", height=40, textvariable=self.pickUpAddress)
        self.address_entry.place(x=20, y=150)

        self.date_label = Label(self.update_frame, text="Pick Up Date", fg="white", bg="#2c2c2c",
                                   font=(self.font, 8))
        self.date_label.place(x=200, y=130)

        self.date_entry = customtkinter.CTkEntry(master=self.update_frame, font=(self.font, 15),
                                                    width=150, placeholder_text="Drop Up Date", height=40, textvariable=self.pickUpDate)
        self.date_entry.place(x=200, y=150)

        self.time_label = Label(self.update_frame, text="Pick Up Time", fg="white", bg="#2c2c2c",
                                font=(self.font, 8))
        self.time_label.place(x=380, y=130)

        self.time_entry = customtkinter.CTkEntry(master=self.update_frame, font=(self.font, 15),
                                                 width=150, placeholder_text="Drop Up Time", height=40, textvariable=self.pickUpTime)
        self.time_entry.place(x=380, y=150)

        self.dropoff_address_label = Label(self.update_frame, text="Drop Off Address", fg="white", bg="#2c2c2c",
                                font=(self.font, 8))
        self.dropoff_address_label.place(x=560, y=130)

        self.dropoff_address_entry = customtkinter.CTkEntry(master=self.update_frame, font=(self.font, 15),
                                                 width=150, placeholder_text="Drop Off Address", height=40, textvariable=self.dropOffAddress)
        self.dropoff_address_entry.place(x=560, y=150)

        self.update_button = customtkinter.CTkButton(master=self.update_frame, text="Update Booking",
                                                     font=(self.font, 15), corner_radius=8, height=35, command=self.update_booking)
        self.update_button.place(x=213, y=220)

        self.clear_button = customtkinter.CTkButton(master=self.update_frame, text="Clear", font=(self.font, 15),
                                                     height=35,
                                                     corner_radius=8, command=self.clear_field)
        self.clear_button.place(x=382, y=220)


        style1 = tkinter.ttk.Style()
        style1.theme_use("default")
        style1.configure("Treeview",
                         background="#9c9c9c",
                         foreground="black",
                         rowheight=25,
                         fieldbackground="#9c9c9c",
                         bordercolor="black",
                         borderwidth=0,
                         font=(self.font, 12))
        style1.map('Treeview', background=[('selected', '#3c3c3c')])
        #
        style1.configure("Treeview.Heading",
                         background="#4c4c4c",
                         foreground="white",
                         relief="flat",
                         font=('Helvetica', 12),
                         padding=(0, 5)
                         )


        style1.map("Treeview.Heading",
                   background=[('active', '#7EC8E3')],
                   foreground = [('active', 'black')])

        self.table_frame = Frame(self.update_booking_window, bg="#2c2c2c", height=273)
        self.table_frame.pack(side="bottom", fill="x")

        # To show the table in the window
        # To show the vertical scroll bar in the table
        # scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        #
        self.booking_records_table = tkinter.ttk.Treeview(self.table_frame, height=10, columns=("bookingid", "pickupaddress", "pickupdate", "pickuptime","pickoffaddress"), show="headings")
        # scroll_y.pack(side="right", fill="y")


        # for the heading section

        self.booking_records_table.heading("bookingid", text="Booking ID",anchor=CENTER)
        self.booking_records_table.heading("pickupaddress", text="Pick Up Address",anchor=CENTER)
        self.booking_records_table.heading("pickupdate", text="Pick Up Date",anchor=CENTER)
        self.booking_records_table.heading("pickuptime", text="Pick Up Time",anchor=CENTER)
        self.booking_records_table.heading("pickoffaddress", text="Pick Off Address",anchor=CENTER)

        # Configuring the style of the headings
        self.booking_records_table.tag_configure("Treeview.Heading", background="black", foreground="white")

        # for the column section
        self.booking_records_table.column("bookingid", width=50,anchor=CENTER)
        self.booking_records_table.column("pickupaddress", width=100,anchor=CENTER)
        self.booking_records_table.column("pickupdate", width=100,anchor=CENTER)
        self.booking_records_table.column("pickuptime", width=100,anchor=CENTER)
        self.booking_records_table.column("pickoffaddress", width=100,anchor=CENTER)

        self.booking_records_table.pack(fill=X, expand=0)
        self.booking_records_table.bind("<ButtonRelease-1>", self.fill_data)

        # ======== TO GET THE RESULT FROM THE CONTROLLER ============
        self.display_data()

    def display_data(self):
        booking =Booking(customer_id=Global.logged_in_customer[0])
        result = select_pending_booking(booking)

        if result is not None:
            self.booking_records_table.delete(*self.booking_records_table.get_children())

            for row in result:
                self.booking_records_table.insert('', END, values=row)

    def fill_data(self,event):
        view_info = self.booking_records_table.focus()
        customer_info = self.booking_records_table.item(view_info)

        row = customer_info.get('values')

        self.clear_field()

        self.bookingId.set(row[0])
        self.pickUpAddress.set(row[1])
        self.pickUpDate.set(row[2])
        self.pickUpTime.set(row[3])
        self.dropOffAddress.set(row[4])

    def clear_field(self):
        self.bookingid_entry.configure(state="normal")
        self.bookingid_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.date_entry.delete(0, END)
        self.time_entry.delete(0, END)
        self.dropoff_address_entry.delete(0, END)

    def update_booking(self):
        bookingID = self.bookingid_entry.get()
        pickup_address = self.address_entry.get()
        pickup_date = self.date_entry.get()
        pickup_time = self.time_entry.get()
        dropoff_address = self.dropoff_address_entry.get()

        if not (bookingID == "" or pickup_address == "" or pickup_date == "" or pickup_time == "" or dropoff_address == ""):
            booking = Booking(booking_id=bookingID,pickup_address = pickup_address, pickup_date=pickup_date, pickup_time= pickup_time, dropoff_address = dropoff_address)
            is_updated = update_booking(booking)
            if is_updated:
                self.display_data()
                messagebox.showinfo("Update Success", "Successfully Updated Booking Details.",parent=self.update_booking_window)
                print("updated")
            else:
                messagebox.showerror("Update Failed", "Sorry, Could't Update Your Booking Details !")
        else:
            messagebox.showerror("Update Failed !", "Please Fill All The Details Properly!")















if __name__ == '__main__':
    window = Tk()
    updateBooking = UpdateBooking(window)
    updateBooking.show_update_booking_window()
    window.mainloop()