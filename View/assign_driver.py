import tkinter.ttk
from tkinter import *
from PIL import Image, ImageTk
import customtkinter

from Controller.driver_dbms import fetch_available_driver


class AssignDriverPage:
    def __init__(self, window, selected_details_list):
        self.window = window
        self.font = "Century Gothic"
        self.details = selected_details_list

        self.available_window = None

    def show_assign_driver_window(self):
        self.assign_window = Toplevel(self.window, bg="#2c2c2c", width=750, height=490)
        self.assign_window.title("Assign Driver")
        self.assign_window.resizable(0, 0)

        screen_width = self.assign_window.winfo_screenwidth()
        screen_height = self.assign_window.winfo_screenheight()

        window_width = 750
        window_height = 490

        x_position = (screen_width - window_width) // 2 -60
        y_position = (screen_height - window_height) // 2

        self.assign_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


        self.assign_window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.main_frame = customtkinter.CTkFrame(self.assign_window, width=750, height=600)
        self.main_frame.place(x=0, y=0)

        self.top_frame = customtkinter.CTkFrame(self.main_frame, width=710, height=80, corner_radius=15)
        self.top_frame.place(x=20, y=10)

        self.top_heading_lbl = customtkinter.CTkLabel(self.top_frame, text="Assign Driver", font=(self.font, 28))
        self.top_heading_lbl.place(relx=0.5, rely=0.5, anchor="center")

        self.left_frame = customtkinter.CTkFrame(self.main_frame, width=520, height=370, corner_radius=15)
        self.left_frame.place(x=20, y=100)

        entry_font = (self.font, 16)
        self.booking_id_lbl = customtkinter.CTkLabel(self.left_frame, text="Booking ID", font=(self.font, 15, 'bold'))
        self.booking_id_lbl.place(x=20, y=20)
        self.booking_id_ent = customtkinter.CTkEntry(self.left_frame, width=150, height=35, font=entry_font)
        self.booking_id_ent.place(x=150, y=20)

        self.name_lbl = customtkinter.CTkLabel(self.left_frame, text="C-Name", font=(self.font, 15, 'bold'))
        self.name_lbl.place(x=20, y=80)
        self.name_ent = customtkinter.CTkEntry(self.left_frame, width=150, height=35, font=entry_font)
        self.name_ent.place(x=150, y=80)

        self.pickup_address_lbl = customtkinter.CTkLabel(self.left_frame, text="Pickup Address",
                                                         font=(self.font, 15, 'bold'))
        self.pickup_address_lbl.place(x=20, y=140)
        self.pickup_address_ent = customtkinter.CTkEntry(self.left_frame, width=150, height=35, font=entry_font)
        self.pickup_address_ent.place(x=150, y=140)

        self.date_lbl = customtkinter.CTkLabel(self.left_frame, text="Date", font=(self.font, 15, 'bold'))
        self.date_lbl.place(x=20, y=200)
        self.date_ent = customtkinter.CTkEntry(self.left_frame, width=150, height=35, font=entry_font)
        self.date_ent.place(x=150, y=200)

        self.time_lbl = customtkinter.CTkLabel(self.left_frame, text="Time", font=(self.font, 15, 'bold'))
        self.time_lbl.place(x=20, y=260)
        self.time_ent = customtkinter.CTkEntry(self.left_frame, width=150, height=35, font=entry_font)
        self.time_ent.place(x=150, y=260)

        self.dropoff_address_lbl = customtkinter.CTkLabel(self.left_frame, text="Dropoff Address",
                                                          font=(self.font, 15, 'bold'))
        self.dropoff_address_lbl.place(x=20, y=320)
        self.dropoff_address_ent = customtkinter.CTkEntry(self.left_frame, width=150, height=35, font=entry_font)
        self.dropoff_address_ent.place(x=150, y=320)

        self.driver_id = customtkinter.CTkLabel(self.left_frame, text="Driver ID", font=(self.font, 12))
        self.driver_id.place(x=350, y=80)

        self.driver_id_ent = customtkinter.CTkEntry(self.left_frame, width=130, height=35)
        self.driver_id_ent.place(x=350, y=120)

        self.driver_name = customtkinter.CTkLabel(self.left_frame, text="D-Name", font=(self.font, 12))
        self.driver_name.place(x=350, y=170)

        self.driver_name_ent = customtkinter.CTkEntry(self.left_frame, width=130, height=35)
        self.driver_name_ent.place(x=350, y=200)

        self.button_frame = customtkinter.CTkFrame(self.main_frame, width=180, height=370, corner_radius=15)
        self.button_frame.place(x=545, y=100)

        self.assign_button = customtkinter.CTkButton(self.button_frame, text="Assign Driver",
                                                     font=(self.font, 16, 'bold'), width=150, height=35,
                                                     corner_radius=10)
        self.assign_button.place(x=10, y=125)

        self.available_button = customtkinter.CTkButton(self.button_frame, text="Available Driver",
                                                        font=(self.font, 16, 'bold'), width=150, height=35,
                                                        corner_radius=10, command=self.show_available_driver_window)
        self.available_button.place(x=10, y=185)

        # ============= CALLING FUNCTION TO FILL THE DATA IN THE ENTRY FIELD ===============
        self.fill_details()

    def show_available_driver_window(self):
        if self.available_window is not None:
            self.available_window.destroy()

        self.available_window = Toplevel(self.window, bg="#2c2c2c", width=400, height=490)
        self.available_window.title("Available Driver")
        self.available_window.resizable(0, 0)

        screen_width = self.available_window.winfo_screenwidth()
        screen_height = self.available_window.winfo_screenheight()

        window_width = 400
        window_height = 490

        x_position = (screen_width - window_width) // 2 +525
        y_position = (screen_height - window_height) // 2

        self.available_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.frame = customtkinter.CTkFrame(self.available_window, width=400, height=600)
        self.frame.place(x=0, y=0)

        self.topFrame = customtkinter.CTkFrame(self.frame, width=360, height=80, corner_radius=20)
        self.topFrame.place(x=20, y=10)

        self.top_lbl = customtkinter.CTkLabel(self.topFrame, text="Available Drivers", font=(self.font, 28))
        self.top_lbl.place(relx=0.5, rely=0.5, anchor="center")

        self.tableFrame = customtkinter.CTkFrame(self.frame, width=360, height=350, corner_radius=20)
        self.tableFrame.place(x=20, y=110)

        self.available_driver_table = tkinter.ttk.Treeview(self.tableFrame,
                                                           columns=("driver_id", "driver_name", "phone_no", "license"),
                                                           show="headings",
                                                           height=12,
                                                           cursor="hand2")

        self.available_driver_table.heading("driver_id", text="D-ID", anchor=CENTER)
        self.available_driver_table.heading("driver_name", text="Name", anchor=CENTER)
        self.available_driver_table.heading("phone_no", text="Phone", anchor=CENTER)
        self.available_driver_table.heading("license", text="License", anchor=CENTER)

        self.available_driver_table.column("driver_id", width=50, anchor=CENTER)
        self.available_driver_table.column("driver_name", width=100, anchor=CENTER)
        self.available_driver_table.column("phone_no", width=100, anchor=CENTER)
        self.available_driver_table.column("license", width=110, anchor=CENTER)

        self.available_driver_table.place(x=2, y=0)
        self.available_driver_table.bind("<ButtonRelease-1>", self.select_driver)

        self.display_available_driver()

    def display_available_driver(self):
        available_driver = fetch_available_driver()

        # to delete the data in the table first
        for item in self.available_driver_table.get_children():
            self.available_driver_table.delete(item)

        for row in available_driver:
            self.available_driver_table.insert('', END, values=row)

    def select_driver(self, event):
        value_info = self.available_driver_table.focus()
        driver_info = self.available_driver_table.item(value_info)

        row = driver_info.get('values')

        self.driver_id_ent.delete(0, END)
        self.driver_name_ent.delete(0, END)

        self.driver_id_ent.insert(0,row[0])
        self.driver_name_ent.insert(0, row[1])

    def fill_details(self):
        self.clear_fields()

        self.booking_id_ent.insert(0, self.details[0])

        self.name_ent.insert(0, self.details[2])
        self.pickup_address_ent.insert(0, self.details[3])
        self.date_ent.insert(0, self.details[4])
        self.time_ent.insert(0, self.details[5])
        self.dropoff_address_ent.insert(0, self.details[6])

        self.booking_id_ent.configure(state="readonly")

    def clear_fields(self):
        self.booking_id_ent.delete(0, END)
        self.name_ent.delete(0, END)
        self.pickup_address_ent.delete(0, END)
        self.date_ent.delete(0, END)
        self.time_ent.delete(0, END)
        self.dropoff_address_ent.delete(0, END)

    def on_close(self):
        self.assign_window.destroy()


if __name__ == '__main__':
    window = Tk()
    assignDriverPage = AssignDriverPage(window)
    assignDriverPage.show_assign_driver_window()
    window.mainloop()
