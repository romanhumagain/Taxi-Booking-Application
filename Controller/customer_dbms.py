from Controller.connection import  mysql_connection
from tkinter import messagebox
from Model.customer import Customer

# ==================== TO FETCH ALL THE CUSTOMER DETAILS FOR THE ADMIN DASHBOARD ======================
def fetch_all_customer():
    connection = mysql_connection()
    cursor = None
    result = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM customer ORDER BY customer_id DESC"
            cursor.execute(query)
            result = cursor.fetchall()

        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(f"ERROR: {error}")
        finally:
            cursor.close()
            connection.close()
            return result

# ==================== TO FETCH SPECIFIC CUSTOMER DETAILS FOR THE ADMIN DASHBOARD ======================
def search_customer(customer):
    connection = mysql_connection()
    cursor = None
    result = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM customer WHERE customer_id = %s "
            values = (customer.get_customer_id(),)
            cursor.execute(query, values)
            result = cursor.fetchall()

        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(f"ERROR: {error}")
        finally:
            cursor.close()
            connection.close()
            return result