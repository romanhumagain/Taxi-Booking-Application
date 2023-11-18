from tkinter import *
from PIL import Image as PILImage, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
import customtkinter

from Model.customer import *
from Model.user import *

from Controller.customer_registration_dbms import *
from Controller.login_dbms import *
# from customer_dashboard import CustomerDashboard

from Model import Global

class MainPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.title("Taxi Booking System")
        self.window.state("zoomed")
        self.window.resizable(0, 0)

        self.font = "Century Gothic"

        self.bg_frame = PILImage.open("Images/login_background.jpg")
        photo = ImageTk.PhotoImage(self.bg_frame)

        customtkinter.set_appearance_mode("System")
        # customtkinter.set_default_color_theme("green")


        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill="both", expand="yes")

        self.navbar = Frame(self.bg_panel, bg="#2c2c2c", pady=25)
        self.navbar.pack(side="top", fill="x")

        self.taxi_logo = PILImage.open("Images/taxi.png")
        photo = ImageTk.PhotoImage(self.taxi_logo)

        self.taxi_logo_label = Label(self.navbar, image=photo, bg='#2c2c2c')
        self.taxi_logo_label.image = photo
        self.taxi_logo_label.place(x=20, y=0)

        self.slogan_label = Label(self.navbar, text="Taxi Booking System",
                                  fg='white', bg='#2c2c2c', font=(self.font, 35))
        self.slogan_label.pack()

        self.main_frame = Frame(self.window, bg='#040405', width='900', height='600')
        self.main_frame.place(x=310, y=120)

        self.text = "Taxi Booking System"
        self.heading = Label(self.main_frame, text=self.text, font=('Century Gothic', 20),
                             fg='white', bg='black')
        # self.heading.place(x=350, y=30)

        self.side_image = PILImage.open("Images/login_side_image.png")
        side_photo = ImageTk.PhotoImage(self.side_image)

        self.side_image_label = Label(self.main_frame, image=side_photo, bg='#040405')
        self.side_image_label.image = side_photo
        self.side_image_label.place(x=4, y=160)

        self.login_frame()
    def login_frame(self):

        self.inner_login_frame = Frame(self.main_frame, bg="#040405", width="440", height="500")
        self.inner_login_frame.place(x=450, y=80)

        self.user_image = PILImage.open("Images/user.png")
        photo = ImageTk.PhotoImage(self.user_image)

        self.user_image_label = Label(self.inner_login_frame, image=photo, bg='#040405')
        self.user_image_label.image = photo
        self.user_image_label.place(x=180, y=50)

        self.sign_in_label = Label(self.inner_login_frame, text="Sign In", bg='#040405', fg='white',
                                   font=(self.font, 18), justify=CENTER)
        self.sign_in_label.place(x=180, y=140)

        self.username_image = PILImage.open("Images/username.png")
        photo = ImageTk.PhotoImage(self.username_image)

        self.username_image_label = Label(self.inner_login_frame, image=photo, bg='#040405')
        self.username_image_label.image = photo
        self.username_image_label.place(x=87, y=240)

        self.username_label = Label(self.inner_login_frame, text="Username", bg='#040405', fg='white',
                                    font=(self.font, 14))
        self.username_label.place(x=90, y=200)

        self.username_entry = Entry(self.inner_login_frame, highlightthickness=0, relief=FLAT, bg='#040404',
                                    fg='white',insertbackground="white", font=(self.font, 12))
        self.username_entry.place(x=115, y=235, width=250)

        self.username_line = Canvas(self.inner_login_frame, width=250, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=115, y=262, width=250)

        self.password_image = PILImage.open("Images/password1.png")
        photo = ImageTk.PhotoImage(self.password_image)

        self.password_image_label = Label(self.inner_login_frame, image=photo, bg='#040405')
        self.password_image_label.image = photo
        self.password_image_label.place(x=87, y=315)

        self.password_label = Label(self.inner_login_frame, text="Password", bg='#040405', fg='white',
                                    font=(self.font, 14))
        self.password_label.place(x=90, y=280)

        self.password_entry = Entry(self.inner_login_frame, show='•', relief=FLAT, bg='#040405',
                                    fg='white', insertbackground="white", font=(self.font, 12))

        self.password_entry.place(x=115, y=315, width=220)

        self.hide_icon = ImageTk.PhotoImage(PILImage.open("Images/hide.png"))
        self.show_icon = ImageTk.PhotoImage(PILImage.open("Images/show.png"))

        # self.show_hide_button = Button(self.inner_login_frame, image=self.show_icon,bd=0, relief="flat", highlightthickness=0)
        # self.show_hide_button.place(x=340, y=312)

        self.show_hide_password_label = Label(self.inner_login_frame, image=self.show_icon, bg='black',cursor='hand2')
        self.show_hide_password_label.place(x=340, y=310)
        self.show_hide_password_label.bind("<Button-1>", self.show_hide_password)


        self.password_line = Canvas(self.inner_login_frame, width=300, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.password_line.place(x=115, y=342, width=250)

        self.forgot_password_label = Label(self.inner_login_frame, text="forgot password ?", fg='white', bg='black',
                                           font=(self.font, 12), cursor="hand2")
        self.forgot_password_label.place(x=225, y=350)
        self.forgot_password_label.bind("<Button-1>")

        self.login_button = customtkinter.CTkButton(
            master=self.inner_login_frame,
            text="Login",
            command=self.login_user,
            font=(self.font, 20, 'bold'),
            height=36,
            width=250,
            corner_radius=7
        )
        self.login_button.place(x=115, y=400)

        self.new_account_label = Label(self.inner_login_frame, text="Create A New Account ?",
                                       font=(self.font, 12),
                                       fg="white", bg='black')
        self.new_account_label.place(x=106, y=460)

        self.signup_option_label = Label(self.inner_login_frame, text="Sign Up", fg="blue", bg="black",
                                         font=(self.font, 12))
        self.signup_option_label.place(x=316, y=460)

        self.signup_option_label.bind("<Button-1>", self.toggle_frames)

    def registration_frame(self):
        style = ttk.Style()
        style.configure("TEntry", padding=3, relief="flat")

        self.inner_registration_frame = Frame(self.main_frame, bg="#040405", width="440", height="500")
        self.inner_registration_frame.place(x=450, y=80)

        self.signup_image = PILImage.open("Images/signup.png")
        photo = ImageTk.PhotoImage(self.signup_image)

        self.signup_image_label = Label(self.inner_registration_frame, image=photo, bg='#040405')
        self.signup_image_label.image = photo
        self.signup_image_label.place(x=145, y=10)

        self.text = "Sign Up"

        self.heading = Label(self.inner_registration_frame, text=self.text, font=(self.font, 18),
                             fg='white', bg='black')
        self.heading.place(x=190, y=10)

        self.heading_line = Canvas(self.inner_registration_frame, width=80, height=3.0, bg='#bdb9b1',
                                   highlightthickness=0)
        # self.heading_line.place(x=90, y=40)
        # ==== FOR THE LEFT SIDE IMAGE ====
        # setting the background image

        # for the registratin form
        self.name_label = Label(self.inner_registration_frame, text="Name", fg="white", bg="#040405",
                                font=(self.font, 13))
        # self.name_label.place(x=10, y=70)

        self.name_entry = customtkinter.CTkEntry(master=self.inner_registration_frame, font = (self.font, 15), width=170, placeholder_text="Full Name", height=38)
        self.name_entry.place(x=35, y=70)

        self.mobile_label = Label(self.inner_registration_frame, text="Phone", fg="white", bg="#040405",
                                  font=(self.font, 13))
        # self.mobile_label.place(x=250, y=70)

        self.mobile_entry = customtkinter.CTkEntry(master=self.inner_registration_frame, font=(self.font, 15), width=170, placeholder_text="Phone No", height=38,
                                      )
        self.mobile_entry.place(x=250, y=70)

        self.email_label = Label(self.inner_registration_frame, text="Email", fg="white", bg="#040405",
                                 font=(self.font, 13))
        # self.email_label.place(x=10, y=130)

        self.email_entry = customtkinter.CTkEntry(master=self.inner_registration_frame, font=(self.font, 13), width=170, placeholder_text="example@gmail.com", height=38)
        self.email_entry.place(x=35, y=130)

        self.address_label = Label(self.inner_registration_frame, text="Address", fg="white", bg="#040405",
                                   font=(self.font, 13))
        # self.address_label.place(x=250, y=130)

        self.address_entry = customtkinter.CTkEntry(master=self.inner_registration_frame, font=(self.font, 15), width=170, placeholder_text="Current Address", height=38)
        self.address_entry.place(x=250, y=130)

        self.gender_label = Label(self.inner_registration_frame, text="Gender", fg="white", bg="#040405",
                                  font=(self.font, 13))
        # self.gender_label.place(x=250, y=195)

        gender_var = customtkinter.StringVar(value = "Gender")

        self.gender_entry = customtkinter.CTkComboBox(master = self.inner_registration_frame, values=["Male", "Female", "Others"], variable=gender_var, width=170, height=40)
        self.gender_entry.place(x=35, y=195)

        payment_methods = StringVar(value="Payment Method")
        self.payment_entry = customtkinter.CTkComboBox(master = self.inner_registration_frame,values=["Online", "Cash"], variable=payment_methods, width=170, height=40)
        self.payment_entry.place(x=250, y=195)

        self.password_label = Label(self.inner_registration_frame, text="Password", fg="white", bg="#040405",
                                    font=(self.font, 13))
        # self.password_label.place(x=10, y=260)

        self.password_entry = customtkinter.CTkEntry(master=self.inner_registration_frame, font=(self.font, 15), width=170, placeholder_text="Password", height=40)
        self.password_entry.place(x=35, y=260)

        self.co_password_label = Label(self.inner_registration_frame, text="Confirm Password", fg="white", bg="#040405",
                                       font=(self.font, 13))
        # self.co_password_label.place(x=10, y=315)

        self.co_password_entry = customtkinter.CTkEntry(master=self.inner_registration_frame, font=(self.font, 15),width=170, placeholder_text="Confirm Password", height=40)
        self.co_password_entry.place(x=35, y=315)

        self.dob_label = Label(self.inner_registration_frame, text="DOB", fg="white", bg="#040405",
                               font=(self.font, 12))
        self.dob_label.place(x=239, y=260)

        self.dob_entry = DateEntry(self.inner_registration_frame, font=('yu gothic ui', 12), selectmode='day',
                                   style='my.DateEntry', background="black",
                                   bordercolor="white",
                                   selectbackground="red", width=12, date_pattern='yyyy-mm-dd')

        self.dob_entry.place(x=284, y=260)

        self.signup_button = customtkinter.CTkButton(
            master=self.inner_registration_frame,
            text="Sign Up",
            command=self.register_customer,
            font=(self.font, 20, 'bold'),
            height=36,
            width=290,
            corner_radius=7

        )
        self.signup_button.place(x=90, y=400)

        #         new account label
        self.signin_label = Label(self.inner_registration_frame, text="Already Have Account ?",
                                  font=(self.font, 13), fg="white", bg='black')
        self.signin_label.place(x=100, y=460)

        #         for signup option
        self.signin_option_label = Label(self.inner_registration_frame, text="Sign In", fg="blue", bg="black",
                                         font=(self.font, 13))
        self.signin_option_label.place(x=320, y=460)

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

    def show_hide_password(self, event):
        if self.password_entry['show'] == '':
            self.show_hide_password_label.config(image=self.show_icon)
            self.password_entry.config(show="•")
        else:
            self.show_hide_password_label.config(image=self.hide_icon)
            self.password_entry.config(show='')

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

        if not (name == "" or phone_no == "" or email=="" or address == "" or date_of_birth == "" or gender == "Gender" or password == "" or confirm_password == ""):
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
        from customer_dashboard import CustomerDashboard
        email = self.username_entry.get()
        password = self.password_entry.get()

        if not(email == "" or password == ""):
            user, customer = validate_credentials(email, password)

            if user is not None:
                Global.current_user = user
                Global.logged_in_customer = customer
                messagebox.showinfo("Login Success" , "Successfully Logged In.")
                self.window.destroy()

                # Create a new Toplevel window for the CustomerDashboard
                customer_dashboard_window = Tk()
                customer_dashboard = CustomerDashboard(customer_dashboard_window)
                customer_dashboard_window.mainloop()

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
