import tkinter.ttk
from tkinter import  *
from PIL import Image, ImageTk
from Controller.login_activity_dbms import fetch_login_details
from Model import  login_activity
from Model import Global
class LoginActivity():
    def __init__(self, window):
        self.window = window
        self.font ="Century Gothic"

    def show_login_activity_window(self):
        self.login_activity_window = Toplevel(self.window, width=850, height=600, bg="#3c3c3c")
        self.login_activity_window.title("Login Details ")
        self.login_activity_window.resizable(0,0)

        screen_width = self.login_activity_window.winfo_screenwidth()
        screen_height = self.login_activity_window.winfo_screenheight()

        window_width = 870
        window_height = 580

        x_position = (screen_width-window_width) // 2 + 140
        y_position = (screen_height-window_height) // 2 +25

        self.login_activity_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.top_frame = Frame(self.login_activity_window, bg="#2c2c2c", height=100)
        self.top_frame.pack(side="top", fill="x")

        heading_icon = ImageTk.PhotoImage(Image.open("Images/login_details.png"))

        self.heading_icon_label = Label(self.top_frame, image=heading_icon, bg='#2c2c2c')
        self.heading_icon_label.image = heading_icon
        self.heading_icon_label.place(x=240, y=20)

        self.heading_label = Label(self.top_frame, text="Your Login Details ", font=(self.font, 26), bg="#2c2c2c", fg="white")
        self.heading_label.place(relx=0.542, rely=0.5, anchor="center")

        # ================= CREATING A TABLE TO DISPLAY THE LOGIN DETAILS ====================
#


        style1 = tkinter.ttk.Style()
        style1.theme_use("default")
        style1.configure("Treeview",
                         background="#F4F4F4",
                         foreground="black",
                         rowheight=25,
                         fieldbackground="#F5F5F5",
                         bordercolor="black",
                         borderwidth=0,
                         font=(self.font, 12))
        style1.map('Treeview', background=[('selected', '#7EC8E3')],
                   foreground = [('active', 'black')])

        #
        style1.configure("Treeview.Heading",
                         background="#4c4c4c",
                         foreground="white",
                         relief="flat",
                         font=('Century Gothic', 11),
                         padding=(0, 8)
                         )


        style1.map("Treeview.Heading",
                   background=[('active', '#3c3c3c')],
                   foreground = [('active', 'white')])


        self.table_frame = Frame(self.login_activity_window, bg="white", height=450)
        self.table_frame.pack(side="bottom", fill = "x")

        scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)

        self.login_activity_table = tkinter.ttk.Treeview(self.table_frame, height=20,columns=("activity_id", "device_type", "operating_system", "processor","node_device_name", "login_date", "login_time"), show="headings", yscrollcommand=scroll_y)
        scroll_y.pack(side = "right", fill = "y")


        self.login_activity_table.heading("activity_id", text="ID", anchor=CENTER)
        self.login_activity_table.heading("device_type", text="Device Type", anchor=CENTER)
        self.login_activity_table.heading("operating_system", text="Operating System", anchor=CENTER)
        self.login_activity_table.heading("processor", text="Processor", anchor=CENTER)
        self.login_activity_table.heading("node_device_name", text="Node Device Name", anchor=CENTER)
        self.login_activity_table.heading("login_date", text="Date", anchor=CENTER)
        self.login_activity_table.heading("login_time", text="Time", anchor=CENTER)


        self.login_activity_table.column("activity_id", width=30, anchor=CENTER)
        self.login_activity_table.column("device_type", width=100, anchor=CENTER)
        self.login_activity_table.column("operating_system", width=100, anchor=CENTER)
        self.login_activity_table.column("processor", width=150, anchor=CENTER)
        self.login_activity_table.column("node_device_name", width=150, anchor=CENTER)
        self.login_activity_table.column("login_date", width=50, anchor=CENTER)
        self.login_activity_table.column("login_time", width=50, anchor=CENTER)


        # Configure the weight of column 0 to make it expand with the frame
        # self.table_frame.columnconfigure(0, weight=1)

        self.login_activity_table.pack(fill = X, expand = 0)
        self.fetch_login_activity()

    def fetch_login_activity(self):
        loginActivity = login_activity.LoginActivity(user_id=Global.current_user[0])
        result = fetch_login_details(loginActivity)

        # FIRST DELETE THE ROWS IN THE TABLE
        for item in self.login_activity_table.get_children():
            self.login_activity_table.delete(item)

        for row in result:
            self.login_activity_table.insert('', END, values=row)

#
#
#
#





if __name__ == '__main__':
    window = Tk()
    activityFrame = LoginActivity(window)
    activityFrame.show_login_activity_window()
    window.mainloop()


