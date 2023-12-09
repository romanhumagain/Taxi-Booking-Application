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


# =========== TO DISPLAY THE AVAILABLE DRIVER DETAILS ===========
def get_available_driver():
    connection = mysql_connection()
    cursor = None
    result = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT driver_id, name, phone_no, address , license,gender, driver_status FROM driver WHERE driver_status = %s ORDER BY driver_id DESC"
            values = ("available",)
            cursor.execute(query,values)
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
    table_result = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT driver_id, name, phone_no, address , license,gender, driver_status, user_id FROM driver WHERE driver_id = %s ORDER BY driver_id DESC"
            values = (driver.get_driver_id(),)
            cursor.execute(query, values)
            result = cursor.fetchone()

            cursor.execute(query, values)
            table_result = cursor.fetchall()

        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result, table_result


#  ============ TO UPDATE THE DRIVER DETAILS ==============
def update_driver_details(driver):
    connection = mysql_connection()
    result = False
    cursor = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "UPDATE driver SET name= %s, phone_no = %s, address = %s, gender = %s, license = %s WHERE driver_id = %s"
            values = ( driver.get_name(), driver.get_phone_no(), driver.get_address(), driver.get_gender(), driver.get_license(),driver.get_driver_id())
            cursor.execute(query, values)
            connection.commit()
            result = True
        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result


# =============== TO DELETE THE SPECIFIC DRIVER DETAILS ================
def delete_driver(driver):
    connection = mysql_connection()
    cursor = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            driver_delete_query = "DELETE from driver WHERE driver_id = %s "
            values = (driver.get_driver_id(),)
            cursor.execute(driver_delete_query, values)

            user_delete_query ="DELETE FROM user WHERE user_id = %s"
            values =(driver.get_user_id(),)
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

# ====== GETTING THE AVAILABLE DRIVER WHILE ASSIGNING THE DRIVER TO THE BOOKING ======================
def fetch_available_driver():
    connection = mysql_connection()
    cursor = None
    result = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT driver_id, name, phone_no, license FROM driver WHERE driver_status = %s"
            values = ("available",)
            cursor.execute(query, values)
            result = cursor.fetchall()

        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

def fetch_reserved_driver():
    connection = mysql_connection()
    cursor = None
    result = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = (""" SELECT booking.driver_id,booking.booking_id, driver.name, phone_no, address, license, gender 
                         FROM booking
                         INNER JOIN driver 
                         ON booking.driver_id = driver.driver_id 
                         WHERE driver_status = %s 
                     """
                     )
            values = ("assigned",)
            cursor.execute(query, values)
            result = cursor.fetchall()

        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

