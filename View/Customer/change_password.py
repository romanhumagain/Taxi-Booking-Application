from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from Controller.user_dbms import change_user_password
from Model.user import User
from Model import Global
from main_page import MainPage

class ChangePassword:
    def __init__(self, frame, main_dashboard):
        self.frame = frame
        self.main_dashboard = main_dashboard
        self.font = "Century Gothic"

        customtkinter.set_appearance_mode("System")
        # customtkinter.set_default_color_theme("green")

    def show_change_password_window(self):
        self.change_password_window = Toplevel(self.frame, bg="#2c2c2c")
        self.change_password_window.title("Change Password")
        self.change_password_window.resizable(0, 0)

        screen_width = self.change_password_window.winfo_screenwidth()
        screen_height = self.change_password_window.winfo_screenheight()

        window_width = 440
        window_height = 420

        x_position = (screen_width - window_width) // 2 + 140
        y_position = (screen_height - window_height) // 2

        self.change_password_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        heading_icon = ImageTk.PhotoImage(Image.open("Images/change_password.png"))
        self.heading_icon_label = Label(self.change_password_window, image=heading_icon, bg='#2c2c2c')
        self.heading_icon_label.image = heading_icon
        self.heading_icon_label.place(x=60, y=5)

        self.heading_label = Label(self.change_password_window, text="Change Your Password", font=(self.font, 17), bg="#2c2c2c",fg="white")
        self.heading_label.place(relx=0.56, rely=0.08, anchor="center")

        self.password_label = Label(self.change_password_window, text="Password", fg="white", bg="#2c2c2c",
                                    font=(self.font, 10))
        self.password_label.place(x=100, y=94)

        self.password_entry = customtkinter.CTkEntry(master=self.change_password_window, font=(self.font, 15),
                                                     width=240, placeholder_text="Password", height=40)
        self.password_entry.place(relx=0.5, rely=0.33, anchor="center")

        self.co_password_label = Label(self.change_password_window, text="Confirm Password", fg="white", bg="#2c2c2c",
                                       font=(self.font, 10))
        self.co_password_label.place(x=100, y=200)

        self.co_password_entry = customtkinter.CTkEntry(master=self.change_password_window, font=(self.font, 15),
                                                        width=240, placeholder_text="Confirm Password", height=40)
        self.co_password_entry.place(relx=0.5, rely=0.59, anchor="center")

        self.change_button = customtkinter.CTkButton(master=self.change_password_window, text="Change Password",
                                                     font=(self.font, 15), corner_radius=8, height=35, command=self.change_password)
        self.change_button.place(x=70, y=330)

        self.exit_button = customtkinter.CTkButton(master=self.change_password_window, text="Exit", font=(self.font, 16),
                                                     corner_radius=8,  height=35, command=self.cancel_window)
        self.exit_button.place(x=260, y=330)

    def cancel_window(self):
        self.change_password_window.destroy()

    def change_password(self):
        password = self.password_entry.get()
        confirm_password = self.co_password_entry.get()

        if password == confirm_password:
            if len(password) >= 8:
                user = User(user_id = Global.current_user[0], password=password)
                password_changed = change_user_password(user)
                if password_changed:
                    messagebox.showinfo("Password Changed Successfully", "Your password has been changed successfully.\n\n Please RE-LOGIN your account.", parent = self.change_password_window)
                    self.cancel_window()
                    self.main_dashboard.destroy()

                    login_page_window = Tk()
                    login_page = MainPage(login_page_window)
                    login_page_window.mainloop()



                else:
                    messagebox.showerror("Password Changed Failed", "Sorry, could't change your password !")
            else:
                messagebox.showerror("Invalid Entry", "password should be atleast 8 character long.", parent = self.change_password_window)




        else:
            messagebox.showerror("Invalid Entry", "Password Didn't Matched !", parent = self.change_password_window)




if __name__ == '__main__':
    window = Tk()
    changePasword = ChangePassword(window)
    changePasword.show_change_password_window()
    window.mainloop()