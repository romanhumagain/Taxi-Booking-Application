from tkinter import *
from tkcalendar import calendar_, DateEntry
import  customtkinter
class UpdateProfile:
    def __init__(self, frame):
        self.frame = frame
        self.font = "Century Gothic"
        # customtkinter.set_default_color_theme("green")

    def show_update_profile_window(self):
        update_profile_window = Toplevel(self.frame)
        update_profile_window.title("Update Profile")
        update_profile_window.config(bg="#2c2c2c")
        update_profile_window.resizable(0, 0)

        screen_width = update_profile_window.winfo_screenwidth()
        screen_height = update_profile_window.winfo_screenheight()

        window_width = 440
        window_height = 420

        x_position = (screen_width - window_width) // 2 + 140
        y_position = (screen_height - window_height) // 2

        update_profile_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


        self.heading_label = Label(update_profile_window, text="Update Your Profile", font=(self.font, 17), bg="#2c2c2c", fg="white")
        self.heading_label.place(relx=0.5, rely=0.06, anchor="center")

        self.name_entry = customtkinter.CTkEntry(master=update_profile_window, font=(self.font, 15), width=170,placeholder_text="Full Name", height=38)
        self.name_entry.place(x=35, y=70)


        self.mobile_entry = customtkinter.CTkEntry(master=update_profile_window, font=(self.font, 15),width=170, placeholder_text="Phone No", height=38,
                                                   )
        self.mobile_entry.place(x=250, y=70)

        self.email_entry = customtkinter.CTkEntry(master=update_profile_window, font=(self.font, 13), width=170,placeholder_text="example@gmail.com", height=38)
        self.email_entry.place(x=35, y=130)


        self.address_entry = customtkinter.CTkEntry(update_profile_window, font=(self.font, 15),
                                                    width=170, placeholder_text="Current Address", height=38)
        self.address_entry.place(x=250, y=130)

        payment_method = customtkinter.StringVar(value="Payment Method")
        self.payment_entry = customtkinter.CTkComboBox(master=update_profile_window, values=['Online', 'Cash'],
                                                       variable=payment_method, width=170, height=40)
        self.payment_entry.place(x=35, y=195)

        gender_var = customtkinter.StringVar(value="Gender")

        self.gender_entry = customtkinter.CTkComboBox(master=update_profile_window,
                                                      values=["Male", "Female", "Others"], variable=gender_var,
                                                      width=170, height=40)
        self.gender_entry.place(x=250, y=195)

        self.dob_label = Label(update_profile_window, text="DOB", fg="white", bg="#2c2c2c",
                               font=(self.font, 12))
        self.dob_label.place(x=26, y=275)

        self.dob_entry = DateEntry(update_profile_window, font=('yu gothic ui', 12), selectmode='day',
                                   style='my.DateEntry', background="black",
                                   bordercolor="white",
                                   selectbackground="red", width=12, date_pattern='yyyy-mm-dd')

        self.dob_entry.place(x=70, y=275)

        self.update_button = customtkinter.CTkButton(master = update_profile_window, text="Update Profile", font=(self.font, 15), corner_radius=8,height=35)
        self.update_button.place(x=70, y=350)

        self.cancel_button = customtkinter.CTkButton(master=update_profile_window, text="Cancel", font=(self.font, 15),height=35,
                                       corner_radius=8)
        self.cancel_button.place(x=260, y=350)

if __name__ == '__main__':
    window = Tk()
    update_profile = UpdateProfile(window)
    update_profile.show_update_profile_window()
    window.mainloop()
