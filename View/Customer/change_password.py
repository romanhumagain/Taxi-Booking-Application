from tkinter import *
import customtkinter

class ChangePassword:
    def __init__(self, frame):
        self.frame = frame
        self.font = "Century Gothic"

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")

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


        self.heading_label = Label(self.change_password_window, text="Change Your Password", font=(self.font, 15, 'bold'), bg="#2c2c2c",fg="white")
        self.heading_label.place(relx=0.5, rely=0.08, anchor="center")

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
                                                     font=(self.font, 15), corner_radius=8, height=35)
        self.change_button.place(x=70, y=330)

        self.cancel_button = customtkinter.CTkButton(master=self.change_password_window, text="Cancel", font=(self.font, 15),
                                                     corner_radius=8,  height=35)
        self.cancel_button.place(x=260, y=330)

if __name__ == '__main__':
    window = Tk()
    changePasword = ChangePassword(window)
    changePasword.show_change_password_window()
    window.mainloop()