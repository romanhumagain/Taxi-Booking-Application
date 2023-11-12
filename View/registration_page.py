from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
# creating a class
class RegistrationPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718") # set the window size
        self.window.title("Taxi Booking System Registration Page")
        self.window.state("zoomed") # to automatically zoomed to full page
        self.window.resizable(0, 0) # to set the window resizable to false

        style = ttk.Style()
        style.configure("TEntry", padding=3, relief="flat")

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
        self.slogan_label = Label(self.navbar, text="New Here? Register Today for Instant Taxi Access", fg='#2ec4b6',
                                  bg='#2c2c2c', font=('times new roman', 25, 'bold'))
        self.slogan_label.pack()

        # for the signup option in the navbar
        self.sign_in_label = Label(self.navbar, text='Sign In ?', fg='white', bg='#2c2c2c', font=('yu gothic ui', 15, 'underline'), cursor="hand2")
        self.sign_in_label.place(x=1400, y=5)
        self.sign_in_label.bind("<Button-1>", self.signin)

        # ==== To create a registration frame ====
        self.registration_frame = Frame(self.window, bg='#040405', width='940', height='600')
        self.registration_frame.place(x=310, y=120)

        # ==== FOR THE LEFT SIDE IMAGE ====
        # setting the background image

        self.side_image = Image.open("Images/login_side_image.png")
        side_photo = ImageTk.PhotoImage(self.side_image)

        self.side_image_label = Label(self.registration_frame, image=side_photo, bg='#040405')
        self.side_image_label.image = side_photo
        self.side_image_label.place(x=4, y=140)

        self.inner_registration_frame = Frame(self.registration_frame, bg="#040405", width="480", height="500")
        self.inner_registration_frame.place(x=450, y=80)

        self.text = "Sign Up"
        self.heading = Label(self.inner_registration_frame, text=self.text, font=('Times New Roman', 20, 'bold'), fg='white', bg='black')
        self.heading.place(x=190, y = 10)

        self.heading_line = Canvas(self.inner_registration_frame, width=80, height=3.0, bg='#bdb9b1', highlightthickness=0)
        # self.heading_line.place(x=90, y=40)
        # ==== FOR THE LEFT SIDE IMAGE ====
        # setting the background image

        # for the registratin form
        self.name_label = Label(self.inner_registration_frame, text="Name", fg="white", bg="#040405", font=('yu gothic ui', 13 ))
        self.name_label.place(x=10,y=70)

        self.name_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry", width=15)
        self.name_entry.place(x=75, y=70)

        self.mobile_label = Label(self.inner_registration_frame, text="Mobile", fg="white", bg="#040405",
                                font=('yu gothic ui', 13))
        self.mobile_label.place(x=250, y=70)

        self.mobile_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry", width=15)
        self.mobile_entry.place(x=320, y=70)

        self.email_label = Label(self.inner_registration_frame, text="Email", fg="white", bg="#040405",
                                font=('yu gothic ui', 13))
        self.email_label.place(x=10, y=130)

        self.email_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry", width=15)
        self.email_entry.place(x=75, y=130)

        self.address_label = Label(self.inner_registration_frame, text="Address", fg="white", bg="#040405",
                                font=('yu gothic ui', 13))
        self.address_label.place(x=250, y=130)

        self.address_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry", width=15)
        self.address_entry.place(x=320, y=130)

        self.dob_label = Label(self.inner_registration_frame, text="DOB", fg="white", bg="#040405",
                                font=('yu gothic ui', 13))
        self.dob_label.place(x=10, y=195)

        self.dob_entry = DateEntry(self.inner_registration_frame, font=('yu gothic ui', 12), selectmode='day', style='my.DateEntry', background="black",
                            bordercolor="white",
                            selectbackground="red", width=13, date_pattern='yyyy-mm-dd')

        self.dob_entry.place(x=75, y=195)

        self.gender_label = Label(self.inner_registration_frame, text="Gender", fg="white", bg="#040405",
                                   font=('yu gothic ui', 13))
        self.gender_label.place(x=250, y=195)

        self.gender_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry", width=15)
        self.gender_entry.place(x=320, y=195)

        self.password_label = Label(self.inner_registration_frame, text="Password", fg="white", bg="#040405",
                                 font=('yu gothic ui', 13))
        self.password_label.place(x=10, y=260)

        self.password_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry", width=15)
        self.password_entry.place(x=160, y=260)

        self.co_password_label = Label(self.inner_registration_frame, text="Confirm Password", fg="white", bg="#040405",
                                   font=('yu gothic ui', 13))
        self.co_password_label.place(x=10, y=315)

        self.co_password_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry", width=15)
        self.co_password_entry.place(x=160, y=315)

        self.signup_button = Button(
            self.inner_registration_frame,
            text="Sign Up",
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
        self.signup_button.place(x=120, y=400)

#         new account label
        self.signin_label = Label(self.inner_registration_frame, text="Already Have Account ?", font=("times new roman", 14), fg="white", bg='black')
        self.signin_label.place(x=140, y=460)

#         for signup option
        self.signin_option_label = Label(self.inner_registration_frame, text="Sign In", fg="blue", bg="black", font=("times new roman", 15, 'underline'))
        self.signin_option_label.place(x=340, y=460)



    def signin(self, event):
        print("Sign In option clicked !")
def page():
    window = Tk()
    RegistrationPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()