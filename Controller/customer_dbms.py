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
            query = """ SELECT customer_id, name, email, phone_no, payment, address, date_of_birth, gender
                        FROM user
                        INNER JOIN customer
                        ON user.user_id = customer.user_id
                        ORDER BY customer_id DESC """
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
            query = """SELECT customer_id, name, email, phone_no, payment, address, date_of_birth, gender
                        FROM user
                        INNER JOIN customer
                        ON user.user_id = customer.user_id
                        WHERE customer_id = %s """
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

def delete_customer(customer):
    connection = mysql_connection()
    cursor = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            driver_delete_query = "DELETE from customer WHERE customer_id = %s "
            values = (customer.get_customer_id(),)
            cursor.execute(driver_delete_query, values)

            user_delete_query = "DELETE FROM user WHERE user_id = %s"
            values = (customer.get_user_id(),)
            cursor.execute(user_delete_query, values)

            connection.commit()
            return True

        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(error)
            return False
        finally:
            cursor.close()
            connection.close()