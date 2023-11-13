from tkinter import *
from View.registration_page import RegistrationPage
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry

from Model.customer import *
from Model.user import *

from Controller.customer_registration_dbms import *
from Controller.login_dbms import *

class MainPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.title("Taxi Booking System")
        self.window.state("zoomed")
        self.window.resizable(0, 0)

        # Preload necessary resources for RegistrationPage
        self.preload_registration_resources()

        self.bg_frame = Image.open("Images/login_background.jpg")
        photo = ImageTk.PhotoImage(self.bg_frame)

        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill="both", expand="yes")

        self.navbar = Frame(self.bg_panel, bg="#2c2c2c", pady=20)
        self.navbar.pack(side="top", fill="x")

        self.taxi_logo = Image.open("Images/taxi.png")
        photo = ImageTk.PhotoImage(self.taxi_logo)

        self.taxi_logo_label = Label(self.navbar, image=photo, bg='#2c2c2c')
        self.taxi_logo_label.image = photo
        self.taxi_logo_label.place(x=20, y=0)

        self.slogan_label = Label(self.navbar, text="Ride Easy, Arrive Happy: Your Taxi, Your Way !",
                                  fg='white', bg='#2c2c2c', font=('times new roman', 25, 'bold'))
        self.slogan_label.pack()

        self.main_frame = Frame(self.window, bg='#040405', width='940', height='600')
        self.main_frame.place(x=310, y=120)

        self.text = "Taxi Booking System"
        self.heading = Label(self.main_frame, text=self.text, font=('Times New Roman', 20, 'bold'),
                             fg='white', bg='black')
        self.heading.place(x=350, y=30)

        self.side_image = Image.open("Images/login_side_image.png")
        side_photo = ImageTk.PhotoImage(self.side_image)

        self.side_image_label = Label(self.main_frame, image=side_photo, bg='#040405')
        self.side_image_label.image = side_photo
        self.side_image_label.place(x=4, y=160)

        self.login_frame()
    def login_frame(self):
        self.inner_login_frame = Frame(self.main_frame, bg="#040405", width="480", height="500")
        self.inner_login_frame.place(x=450, y=80)

        self.user_image = Image.open("Images/user.png")
        photo = ImageTk.PhotoImage(self.user_image)

        self.user_image_label = Label(self.inner_login_frame, image=photo, bg='#040405')
        self.user_image_label.image = photo
        self.user_image_label.place(x=210, y=50)

        self.sign_in_label = Label(self.inner_login_frame, text="Sign In", bg='#040405', fg='white',
                                   font=('yu gothic ui', 18, 'bold'))
        self.sign_in_label.place(x=210, y=140)

        self.username_image = Image.open("Images/username.png")
        photo = ImageTk.PhotoImage(self.username_image)

        self.username_image_label = Label(self.inner_login_frame, image=photo, bg='#040405')
        self.username_image_label.image = photo
        self.username_image_label.place(x=117, y=240)

        self.username_label = Label(self.inner_login_frame, text="Username", bg='#040405', fg='white',
                                    font=('yu gothic ui', 15, 'bold'))
        self.username_label.place(x=120, y=200)

        self.username_entry = Entry(self.inner_login_frame, highlightthickness=0, relief=FLAT, bg='#040404',
                                    fg='white',insertbackground="white", font=('yu gothic ui', 12, 'bold'))
        self.username_entry.place(x=145, y=235, width=250)

        self.username_line = Canvas(self.inner_login_frame, width=250, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=145, y=262, width=250)

        self.password_image = Image.open("Images/password1.png")
        photo = ImageTk.PhotoImage(self.password_image)

        self.password_image_label = Label(self.inner_login_frame, image=photo, bg='#040405')
        self.password_image_label.image = photo
        self.password_image_label.place(x=117, y=315)

        self.password_label = Label(self.inner_login_frame, text="Password", bg='#040405', fg='white',
                                    font=('yu gothic ui', 15, 'bold'))
        self.password_label.place(x=120, y=280)

        self.password_entry = Entry(self.inner_login_frame, show='*', relief=FLAT, bg='#040405',
                                    fg='white', insertbackground="white", font=('yu gothic ui', 12, 'bold'))

        self.password_entry.place(x=145, y=315, width=220)

        self.hide_password_image = Image.open("Images/hide.png")
        hide_photo = ImageTk.PhotoImage(self.hide_password_image)

        self.hide_password_image_label = Label(self.inner_login_frame, image=hide_photo, bg='white', cursor='hand2')
        self.hide_password_image_label.image = hide_photo
        self.hide_password_image_label.place(x=370, y=315)
        self.hide_password_image_label.bind("<Button-1>", self.hide_password)


        self.show_password_image = Image.open("Images/show.png")
        show_photo = ImageTk.PhotoImage(self.show_password_image)

        self.show_password_image_label = Label(self.inner_login_frame, image=show_photo, bg='white',cursor='hand2')
        self.show_password_image_label.image = show_photo
        self.show_password_image_label.place(x=370, y=315)
        self.show_password_image_label.bind("<Button-1>", self.show_password)


        self.password_line = Canvas(self.inner_login_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=145, y=342, width=250)

        self.forgot_password_label = Label(self.inner_login_frame, text="forgot password ?", fg='blue', bg='black',
                                           font=("times new roman", 14, 'underline'), cursor="hand2")
        self.forgot_password_label.place(x=260, y=350)
        self.forgot_password_label.bind("<Button-1>")

        self.login_button = Button(
            self.inner_login_frame,
            text="Login",
            command=self.login_user,
            font=('Helvetica', 14, 'bold'),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            bd=0,
            padx=110,
            pady=4
        )
        self.login_button.place(x=120, y=400)

        self.new_account_label = Label(self.inner_login_frame, text="Create A New Account ?",
                                       font=("times new roman", 14),
                                       fg="white", bg='black')
        self.new_account_label.place(x=130, y=460)

        self.signup_option_label = Label(self.inner_login_frame, text="Sign Up", fg="blue", bg="black",
                                         font=("times new roman", 15, 'underline'))
        self.signup_option_label.place(x=330, y=460)

        self.signup_option_label.bind("<Button-1>", self.toggle_frames)

    def registration_frame(self):
        style = ttk.Style()
        style.configure("TEntry", padding=3, relief="flat")

        self.inner_registration_frame = Frame(self.main_frame, bg="#040405", width="480", height="500")
        self.inner_registration_frame.place(x=450, y=80)

        self.signup_image = Image.open("Images/signup.png")
        photo = ImageTk.PhotoImage(self.signup_image)

        self.signup_image_label = Label(self.inner_registration_frame, image=photo, bg='#040405')
        self.signup_image_label.image = photo
        self.signup_image_label.place(x=145, y=10)

        self.text = "Sign Up"

        self.heading = Label(self.inner_registration_frame, text=self.text, font=('Times New Roman', 20, 'bold'),
                             fg='white', bg='black')
        self.heading.place(x=190, y=10)

        self.heading_line = Canvas(self.inner_registration_frame, width=80, height=3.0, bg='#bdb9b1',
                                   highlightthickness=0)
        # self.heading_line.place(x=90, y=40)
        # ==== FOR THE LEFT SIDE IMAGE ====
        # setting the background image

        # for the registratin form
        self.name_label = Label(self.inner_registration_frame, text="Name", fg="white", bg="#040405",
                                font=('yu gothic ui', 13))
        self.name_label.place(x=10, y=70)

        self.name_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry", width=15)
        self.name_entry.place(x=75, y=70)

        self.mobile_label = Label(self.inner_registration_frame, text="Mobile", fg="white", bg="#040405",
                                  font=('yu gothic ui', 13))
        self.mobile_label.place(x=250, y=70)

        self.mobile_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry",
                                      width=15)
        self.mobile_entry.place(x=320, y=70)

        self.email_label = Label(self.inner_registration_frame, text="Email", fg="white", bg="#040405",
                                 font=('yu gothic ui', 13))
        self.email_label.place(x=10, y=130)

        self.email_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry", width=15)
        self.email_entry.place(x=75, y=130)

        self.address_label = Label(self.inner_registration_frame, text="Address", fg="white", bg="#040405",
                                   font=('yu gothic ui', 13))
        self.address_label.place(x=250, y=130)

        self.address_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry",
                                       width=15)
        self.address_entry.place(x=320, y=130)

        self.dob_label = Label(self.inner_registration_frame, text="DOB", fg="white", bg="#040405",
                               font=('yu gothic ui', 13))
        self.dob_label.place(x=10, y=195)

        self.dob_entry = DateEntry(self.inner_registration_frame, font=('yu gothic ui', 12), selectmode='day',
                                   style='my.DateEntry', background="black",
                                   bordercolor="white",
                                   selectbackground="red", width=13, date_pattern='yyyy-mm-dd')

        self.dob_entry.place(x=75, y=195)

        self.gender_label = Label(self.inner_registration_frame, text="Gender", fg="white", bg="#040405",
                                  font=('yu gothic ui', 13))
        self.gender_label.place(x=250, y=195)

        self.gender_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry",
                                      width=15)
        self.gender_entry.place(x=320, y=195)

        self.password_label = Label(self.inner_registration_frame, text="Password", fg="white", bg="#040405",
                                    font=('yu gothic ui', 13))
        self.password_label.place(x=10, y=260)

        self.password_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry",
                                        width=15)
        self.password_entry.place(x=160, y=260)

        self.co_password_label = Label(self.inner_registration_frame, text="Confirm Password", fg="white", bg="#040405",
                                       font=('yu gothic ui', 13))
        self.co_password_label.place(x=10, y=315)

        self.co_password_entry = ttk.Entry(self.inner_registration_frame, font=('yu gothic ui', 12), style="TEntry",
                                           width=15)
        self.co_password_entry.place(x=160, y=315)

        self.signup_button = Button(
            self.inner_registration_frame,
            text="Sign Up",
            command=self.register_customer,
            font=('Helvetica', 14, 'bold'),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',  # Background color when button is clicked
            activeforeground='white',  # Text color when button is clicked
            bd=0,  # Border width
            padx=110,
            pady=4
        )
        self.signup_button.place(x=120, y=400)

        #         new account label
        self.signin_label = Label(self.inner_registration_frame, text="Already Have Account ?",
                                  font=("times new roman", 14), fg="white", bg='black')
        self.signin_label.place(x=140, y=460)

        #         for signup option
        self.signin_option_label = Label(self.inner_registration_frame, text="Sign In", fg="blue", bg="black",
                                         font=("times new roman", 15, 'underline'))
        self.signin_option_label.place(x=340, y=460)

        self.signin_option_label.bind("<Button-1>", self.toggle_frames)

    def toggle_frames(self, event):
        # Toggle between login and registration frames
        if hasattr(self, 'inner_login_frame') and hasattr(self, 'inner_registration_frame'):
            self.inner_login_frame.pack_forget()
            self.inner_registration_frame.pack_forget()

        if event.widget == self.signup_option_label:
            self.registration_frame()
        elif event.widget == self.signin_option_label:
            self.login_frame()

    def preload_registration_resources(self):
        # Preload resources for RegistrationPage here
        # You can load images, configure fonts, etc.
        pass

    def open_registration_page(self):
        # Destroy the current window
        self.window.destroy()

        # Create a new Tkinter window
        new_window = Tk()

        # Create an instance of the RegistrationPage
        registration_page = RegistrationPage(new_window)
        new_window.mainloop()

    def show_password(self, event):
        self.password_entry.configure(show='')
        self.show_password_image_label.pack_forget()
        self.hide_password_image_label.place(x=370, y=315)

    def hide_password(self, event):
        self.password_entry.configure(show='*')
        self.hide_password_image_label.pack_forget()
        self.show_password_image_label.place(x=370, y=315)

    def signup(self, event):
        print("Signup option clicked !")

    # to register user
    def register_customer(self):
        name = self.name_entry.get()
        phone_no = self.mobile_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        date_of_birth = self.dob_entry.get()
        gender = self.gender_entry.get()
        password = self.password_entry.get()
        confirm_password = self.co_password_entry.get()

        if not (name == "" or phone_no == "" or email=="" or address == "" or date_of_birth == "" or gender == "" or password == "" or confirm_password == ""):
            if password == confirm_password:
                if len(password) >= 8:
                    user = User(email= email, password= password,user_type="customer")

                    customer = Customer(name=name, phone_no= phone_no,payment="Online", address= address, date_of_birth = date_of_birth, gender= gender)

                    user_isregistered = register_user(user)
                    if user_isregistered:
                        customer_isregistered = register_customer(customer, user)
                        if customer_isregistered:
                            messagebox.showinfo("Registration Complete", "Successfully Registered Your Account, You Can Login Now.")
                            self.inner_registration_frame.pack_forget()
                            self.login_frame()
                        else:
                            messagebox.showerror("Registration ERROR", "Sorry Could't Register Your Account !")
                else:
                    messagebox.showwarning("Password ERROR!", "Password Should Be Atleast 8 Character Long !")

            else:
                messagebox.showwarning("Password ERROR", "Password Didn't Match !")

        else:
            messagebox.showwarning("Registration Incomplete", "Please Fill All The Details To Register Your Account !")

    # to check the login credentials
    def login_user(self):
        email = self.username_entry.get()
        password = self.password_entry.get()

        if not(email == "" or password == ""):
            user_is_authenticated = validate_credentials(email, password)

            if user_is_authenticated:
                messagebox.showinfo("Login Success" , "Successfully Logged In.")
            else:
                messagebox.showerror("Invalid Credentials", "Invalid Credentials !")
        else:
            messagebox.showwarning("Empty Field", "Please Provide Your Login Credentials !")


def page():
    window = Tk()
    MainPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()
