from tkinter import *

from PIL import Image, ImageTk

# creating a class
class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718") # set the window size
        self.window.title("Taxi Booking System")
        self.window.state("zoomed") # to automatically zoomed to full page
        self.window.resizable(0, 0) # to set the window resizable to false

        # ===== To set the background image ====
        self.bg_frame = Image.open("Images/login_background.jpg")
        photo = ImageTk.PhotoImage(self.bg_frame)

        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill = "both", expand = "yes")

        # to create a navbar frame
        self.navbar = Frame(self.bg_panel,bg="#2c2c2c", pady=20)
        self.navbar.pack(side = "top", fill = "x")

        # for the application logo
        self.taxi_logo = Image.open("Images/taxi.png")
        photo = ImageTk.PhotoImage(self.taxi_logo)

        self.taxi_logo_label = Label(self.navbar, image=photo, bg='#2c2c2c')
        self.taxi_logo_label.image = photo
        self.taxi_logo_label.place(x=20, y=-30)

        # for the heading slogan
        self.slogan_label = Label(self.navbar, text="Ride Easy, Arrive Happy: Your Taxi, Your Way !", fg='#2ec4b6',
                                  bg='#2c2c2c', font=('times new roman', 25, 'bold'))
        self.slogan_label.pack()

        # ==== To create a login frame ====
        self.login_frame = Frame(self.window, bg='#040405', width='950', height='600')
        self.login_frame.place(x=290, y=120)

        self.text = "Welcome To Taxi Booking System"
        self.heading = Label(self.login_frame, text=self.text, font=('Times New Roman', 20, 'bold'), fg='white', bg='black')
        self.heading.place(x=240, y = 30)

        # ==== FOR THE LEFT SIDE IMAGE ====
        # setting the background image

        self.side_image = Image.open("Images/login_side_image.png")
        side_photo = ImageTk.PhotoImage(self.side_image)

        self.side_image_label = Label(self.login_frame, image=side_photo, bg='#040405')
        self.side_image_label.image = side_photo
        self.side_image_label.place(x=4, y = 160)

#         for user logo
        self.user_image = Image.open("Images/user.png")
        photo = ImageTk.PhotoImage(self.user_image)

        self.user_image_label = Label(self.login_frame, image=photo, bg='#040405')
        self.user_image_label.image = photo

        self.user_image_label.place(x=606, y =140)

        self.sign_in_label = Label(self.login_frame, text="Sign In", bg='#040405', fg='white', font=('yu gothic ui', 18, 'bold'))
        self.sign_in_label.place(x=610, y=240)

#         for username
        self.username_label = Label(self.login_frame, text="Username", bg='#040405', fg='#4f4e5d', font=('yu gothic ui', 15, 'bold'))
        self.username_label.place(x=520, y=300)

        self.username_entry = Entry(self.login_frame, highlightthickness=0, relief=FLAT, bg ='#040404', fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
        self.username_entry.place(x=525, y=335, width=280)

        self.username_line = Canvas(self.login_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=525, y=362, width=280)

#         for password
        self.password_label = Label(self.login_frame, text="Password", bg='#040405', fg='#4f4e5d', font=('yu gothic ui', 15, 'bold'))
        self.password_label.place(x=520, y=380)

        self.password_entry = Entry(self.login_frame, highlightthickness=0, relief=FLAT, bg ='#040404', fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
        self.password_entry.place(x=525, y=415, width=280)

        self.password_line = Canvas(self.login_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=525, y=442, width=280)

        # for forgot password
        self.forgot_password_label = Label(self.login_frame, text="forgot password ?", fg='blue', bg='black', font=("times new roman", 14, 'underline'), cursor="hand2")
        self.forgot_password_label.place(x=670, y=460)
        self.forgot_password_label.bind("<Button-1>")

        self.login_button = Button(
            self.login_frame,
            text="Login",
            # command=self.login,
            font=('Helvetica', 14, 'bold'),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',  # Background color when button is clicked
            activeforeground='white',     # Text color when button is clicked
            bd=0,  # Border width
            padx=110,
            pady=4
        )
        self.login_button.place(x=520, y=500)

#         new account label
        self.new_account_label = Label(self.window, text="Create A New Account ?", font=("times new roman", 14), fg="white", bg='black')
        self.new_account_label.place(x=810, y=690)

#         for signup option
        self.signup_option_label = Label(self.window, text="Sign Up", fg="blue", bg="black", font=("times new roman", 15, 'underline'))
        self.signup_option_label.place(x=1005, y=690)
def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()

if __name__ == '__main__':
    page()