import tkinter.ttk
from tkinter import *
from tkinter import  messagebox
import  mysql.connector
class TableWindow:
    def __init__(self, window):
        self.window = window
        self.window.geometry('976x700+300+0')

        self.create_frame()
        self.display_records()
    def create_frame(self):
        self.right_frame = Frame(self.window, bg="#2c2c2c", width=220)
        self.right_frame.pack(side="right", fill='y')

        # Register Button
        self.register_btn = Button(self.right_frame, text="Register", width=15, bg="#3c3c3c", fg="white", command=self.register_student)
        self.register_btn.pack(pady=5)

        # Display Button
        self.display_btn = Button(self.right_frame, text="Display", width=15, bg="#3c3c3c", fg="white", command=self.display_records)
        self.display_btn.pack(pady=5)

        # Update Button
        self.update_btn = Button(self.right_frame, text="Update", width=15, bg="#3c3c3c", fg="white")
        self.update_btn.pack(pady=5)

        # Delete Button
        self.delete_btn = Button(self.right_frame, text="Delete", width=15, bg="#3c3c3c", fg="white")
        self.delete_btn.pack(pady=5)

        # Search Button
        self.search_btn = Button(self.right_frame, text="Search", width=15, bg="#3c3c3c", fg="white")
        self.search_btn.pack(pady=5)

        # Reset Button

        self.reset_btn = Button(self.right_frame, text="Reset", width=15, bg="#3c3c3c", fg="white", command=self.clear)
        self.reset_btn.pack(pady=5)

        # Exit Button
        self.exit_btn = Button(self.right_frame, text="Exit", width=15, bg="#3c3c3c", fg="white", command=self.exit)
        self.exit_btn.pack(pady=5)


        self.form_frame = Frame(self.window, bg="#3c3c3c", height=400)
        self.form_frame.pack(side="top", fill='x', padx=20, pady=20)

        # ================== CREATING A VARIABLE =======================
        self.studentId = StringVar()
        self.firstName = StringVar()
        self.lastName = StringVar()
        self.email = StringVar()
        self.address = StringVar()

        # Labels
        Label(self.form_frame, text="Student ID", bg="#3c3c3c", fg="white").grid(row=0, column=0,padx=10, pady=5)

        self.student_id_entry = Entry(self.form_frame, textvariable=self.studentId)
        self.student_id_entry.grid(row=0, column=1,  pady=5)

        Label(self.form_frame, text="First Name", bg="#3c3c3c", fg="white").grid(row=1, column=0,padx=10, pady=5)
        self.first_name_entry = Entry(self.form_frame, textvariable=self.firstName)
        self.first_name_entry.grid(row=1, column=1,  pady=5)

        Label(self.form_frame, text="Last Name", bg="#3c3c3c", fg="white").grid(row=1, column=2, padx=10, pady=5)

        self.last_name_entry = Entry(self.form_frame, textvariable=self.lastName)
        self.last_name_entry.grid(row=1, column=3,  pady=5)

        Label(self.form_frame, text="Email", bg="#3c3c3c", fg="white").grid(row=2, column=0,padx=10, pady=5)

        self.email_entry = Entry(self.form_frame, textvariable=self.email)
        self.email_entry.grid(row=2, column=1, sticky="w", pady=5)

        Label(self.form_frame, text="Address", bg="#3c3c3c", fg="white").grid(row=2, column=2,  padx=10,pady=5)

        self.address_entry = Entry(self.form_frame, textvariable=self.address)
        self.address_entry.grid(row=2, column=3,  pady=5)

        self.table_frame = Frame(self.window, bg="#3c3c3c", height=500)
        self.table_frame.pack(side="bottom", fill='x')


#         for creating a table in the table frame
        scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.student_records_table = tkinter.ttk.Treeview(self.table_frame, height=15, column = ('stdid', 'firstname','lastname','email','address'), yscrollcommand=scroll_y.set)
        scroll_y.pack(side="right", fill="y")

        self.student_records_table.heading("stdid", text="StudentId")
        self.student_records_table.heading("firstname", text="First Name")
        self.student_records_table.heading("lastname", text="Last Name")
        self.student_records_table.heading("email", text="Email")
        self.student_records_table.heading("address", text="Address")

        self.student_records_table['show'] = "headings"

        self.student_records_table.column("stdid", width=70)
        self.student_records_table.column("firstname", width=100)
        self.student_records_table.column("lastname", width=100)
        self.student_records_table.column("email", width=100)
        self.student_records_table.column("address", width=100)

        self.student_records_table.pack(fill=BOTH, expand = 1)
        self.student_records_table.bind("<ButtonRelease-1>", self.student_info)
#         ====================== FUNCTION DECLARATIONS ===================
    def exit(self):
        exit = messagebox.askyesno("Exit Window", "Confirm if you want to exit !")
        if exit == 1:
            self.window.destroy()
            return

    def clear(self):
        self.student_id_entry.delete(0, END)
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

    def register_student(self):
        if not (self.studentId =="" or self.firstName == "" or self.email=="" or self.address==""):
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password ="",
                    database = "tkinter"
                )
                cursor = connection.cursor()
                cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s)", (
                self.studentId.get(), self.firstName.get(), self.lastName.get(), self.email.get(), self.address.get()))

                connection.commit()
                cursor.close()
                connection.close()
                messagebox.showinfo("Registration", "Registeration Success")
                self.clear()
            except Exception as e:
                messagebox.showerror("ERROR", f"Error during registration: {str(e)}")

        else:
             messagebox.showerror("ERROR", "Please Fill All The Details !")


    def display_records(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tkinter"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM student")

            result = cursor.fetchall()
            if result is not None:
                self.student_records_table.delete(*self.student_records_table.get_children())
                for row in result:
                    self.student_records_table.insert('', END, values=row)


            connection.commit()
            cursor.close()
            connection.close()

        except Exception as e:
            print(e)
            messagebox.showerror("ERROR", f"{e}")

    def student_info(self, event):
        view_info = self.student_records_table.focus()
        student_data = self.student_records_table.item(view_info)

        row = student_data['values']

        self.studentId.set(row[0])
        self.firstName.set(row[1])
        self.lastName.set(row[2])
        self.email.set(row[3])
        self.address.set(row[4])



if __name__ == '__main__':
    window = Tk()
    tableWindow = TableWindow(window)
    # tableWindow.create_frame()
    window.mainloop()
