from tkinter import *
import customtkinter
from PIL import Image,  ImageTk
class DriverProfile:
    def __init__(self, window):
        self.window = window
        self.font = "Century Gothic"

    def show_driver_profile(self):
        self.driver_profile_window = Toplevel(self.window, width=720, height=460, bg="#2c2c2c")
        self.driver_profile_window.title("Driver Profile")
        self.driver_profile_window.resizable(0, 0)

        self.profile_frame = Frame(self.driver_profile_window, bg="#1c1c1c", width=720, height=460)
        self.profile_frame.place(x=0, y=0)

        # to place the profile icon image
        photo = ImageTk.PhotoImage(Image.open("Images/user_profile1.png").resize((75, 75), Image.ANTIALIAS))

        self.user_profile_image_label = Label(self.profile_frame, image=photo, bg='#1c1c1c')
        self.user_profile_image_label.image = photo
        self.user_profile_image_label.place(relx=0.5, rely=0.12, anchor='center')

        # to show the Customer Name
        self.user_name = Label(self.profile_frame, text="Roman Humagain", font=(self.font, 22), fg='white', bg='#1c1c1c')
        self.user_name.place(relx=0.5, rely=0.26, anchor='center')

        #   to show the personal information

        self.details_frame = customtkinter.CTkFrame(self.profile_frame, width=680, height=200, corner_radius=20)
        self.details_frame.place(x=20, y=170)

        self.email_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Email")
        self.email_label.place(x=40, y=20)

        self.user_email_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.user_email_label.place(x=40, y=45)

        self.email_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.email_line.place(x=40, y=70, width=225)

        self.mobile_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Phone No")
        self.mobile_label.place(x=320, y=20)

        self.user_mobile_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.user_mobile_label.place(x=320, y=45)

        self.mobile_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.mobile_line.place(x=322, y=70, width=135)

        self.address_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Address")
        self.address_label.place(x=520, y=20)

        self.user_address_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.user_address_label.place(x=520, y=45)

        self.address_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.address_line.place(x=522, y=70, width=145)

        self.gender_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Gender")
        self.gender_label.place(x=40, y=100)

        self.user_gender_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.user_gender_label.place(x=40, y=125)

        self.gender_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.gender_line.place(x=40, y=155, width=90)

        self.dob_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="D.O.B")
        self.dob_label.place(x=320, y=100)

        self.user_dob_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.user_dob_label.place(x=320, y=125)

        self.dob_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.dob_line.place(x=322, y=155, width=135)

        self.payment_label = customtkinter.CTkLabel(self.details_frame, font=(self.font, 12), text="Payment Method")
        self.payment_label.place(x=520, y=100)

        self.user_payment_label = customtkinter.CTkLabel(self.details_frame, text="", font=(self.font, 16))
        self.user_payment_label.place(x=520, y=125)

        self.payment_line = Canvas(self.details_frame, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.payment_line.place(x=520, y=155, width=145)

        #     to show the button for more functionality of the application
        update_btn_image = ImageTk.PhotoImage(Image.open("Images/update.png").resize((20, 20), Image.ANTIALIAS))

        self.update_button = customtkinter.CTkButton(master=self.profile_frame, image=update_btn_image,
                                                     text="Update Profile", font=(self.font, 16, 'bold'),
                                                     corner_radius=15, height=34, width=100)
        self.update_button.place(x=160, y=400)

        password_btn_image = ImageTk.PhotoImage(Image.open("Images/password1.png").resize((20, 20), Image.ANTIALIAS))

        self.change_password_button = customtkinter.CTkButton(master=self.profile_frame, image=password_btn_image,
                                                              text="Change Password", font=(self.font, 16, 'bold'),
                                                              corner_radius=15, height=34, width=100,)
        self.change_password_button.place(x=345, y=400)


if __name__ == '__main__':
    window = Tk()
    driverProfile = DriverProfile(window)
    driverProfile.show_driver_profile()
    window.mainloop()