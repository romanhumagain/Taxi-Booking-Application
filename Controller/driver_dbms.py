from Controller.connection import mysql_connection
from Model.driver import Driver
from Model.user import User
from tkinter import messagebox

# ========== TO INSERT DATA TO THE DRIVER TABLE FROM THE ADMIN DASHBOARD ============
def register_driver(driver, user):
    connection = mysql_connection()
    result = False
    cursor = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO driver(name, phone_no, address, license, gender, driver_status, user_id) VALUES (%s, %s, %s ,%s, %s, %s, %s)"
            values = (driver.get_name(),driver.get_phone_no(), driver.get_address(), driver.get_license(), driver.get_gender(), driver.get_driver_status(), user.get_user_id())
            cursor.execute(query, values)
            connection.commit()
            result  = True
        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

# =========== TO DISPLAY ALL THE DRIVER DETAILS ==================
def get_all_driver():
    connection = mysql_connection()
    cursor = None
    result = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT driver_id, name, phone_no, address , license,gender, driver_status FROM driver ORDER BY driver_id DESC"
            cursor.execute(query)
            result = cursor.fetchall()

        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result


# =========== TO FETCH SPECIFIC DRIVER DETAILS ==================
def search_driver(driver):
    connection = mysql_connection()
    cursor = None
    result = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT driver_id, name, phone_no, address , license,gender, driver_status FROM driver WHERE driver_id = %s ORDER BY driver_id DESC"
            values = (driver.get_driver_id(),)
            cursor.execute(query, values)
            result = cursor.fetchone()

        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result