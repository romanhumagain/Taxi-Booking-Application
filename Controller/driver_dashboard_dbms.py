from tkinter import messagebox

from Controller.connection import mysql_connection
from Model.driver import Driver
from Model.user import User


# ============= TO FETCH THE ASSIGNED BOOKING TO THE SPECIFIC DRIVER ===================
def fetch_assigned_booking(driver):
    connection = None
    cursor = None
    result = None

    connection = mysql_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = """
                        SELECT booking.booking_id, booking.customer_id, customer.name, pickup_address, pickup_date, pickup_time, dropoff_address,booking.booking_status
                        FROM booking 
                        JOIN customer 
                        ON booking.customer_id = customer.customer_id
                        JOIN driver
                        ON booking.driver_id = driver.driver_id
                        WHERE driver.driver_id = %s and booking.trip_status = %s
                    """
            values = (driver.get_driver_id(),"Incomplete")
            cursor.execute(query, values)
            result = cursor.fetchall()
        except Exception as error:
            print(f"ERROR: {error}")
        finally:
            cursor.close()
            connection.close()
            return result


# ============ TO GET THE DATA FOR THE TRIP HISTORY ================
def fetch_complete_trip_history(driver):
    connection = mysql_connection()
    cursor = None
    result = None

    if connection is not None:
        try:
            cursor = connection.cursor()
            query = """
                        SELECT booking.booking_id, booking.customer_id, pickup_address, pickup_date, pickup_time, dropoff_address
                        FROM booking 
                        JOIN customer 
                        ON booking.customer_id = customer.customer_id
                        JOIN driver
                        ON booking.driver_id = driver.driver_id
                        WHERE driver.driver_id = %s and booking.trip_status = %s
                    """
            values = (driver.get_driver_id(),"Completed")
            cursor.execute(query, values)
            result = cursor.fetchall()
        except Exception as error:
            print(f"ERROR: {error}")
        finally:
            cursor.close()
            connection.close()
            return result

def fetch_incomplete_booking(driver):
    connection = None
    cursor = None
    result = None

    connection = mysql_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = """
                        SELECT booking.booking_id, booking.customer_id, pickup_address, pickup_date, pickup_time, dropoff_address
                        FROM booking 
                        JOIN customer 
                        ON booking.customer_id = customer.customer_id
                        JOIN driver
                        ON booking.driver_id = driver.driver_id
                        WHERE driver.driver_id = %s and booking.trip_status = %s
                    """
            values = (driver.get_driver_id(),"Incomplete")
            cursor.execute(query, values)
            result = cursor.fetchall()
        except Exception as error:
            print(f"ERROR: {error}")
        finally:
            cursor.close()
            connection.close()
            return result

def fetch_customer_details(customer):
    connection = None
    cursor = None
    result = None

    connection = mysql_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = """SELECT customer_id, name, phone_no, address, gender, date_of_birth FROM customer WHERE customer_id = %s
                        """
            values = (customer.get_customer_id(),)
            cursor.execute(query, values)
            result = cursor.fetchall()
        except Exception as error:
            print(f"ERROR: {error}")
        finally:
            cursor.close()
            connection.close()
            return result

# ============== TO COMPLETE THE ASSIGNED TRIP ==============
def complete_assigned_trip(booking):
    connection = None
    cursor = None
    connection = mysql_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = """UPDATE booking SET trip_status = %s WHERE booking_id = %s"""
            values = ("Completed",booking.get_booking_id())
            cursor.execute(query, values)

            query = """ UPDATE driver SET driver_status = %s WHERE driver_id = %s"""
            values = ("available", booking.get_driver_id())
            cursor.execute(query, values)

            query = """ UPDATE payment SET payment_status = %s WHERE booking_id = %s"""
            values = ("Paid", booking.get_booking_id())
            cursor.execute(query, values)

            connection.commit()
            return True
        except Exception as error:
            print(f"ERROR: {error}")
            return False
        finally:
            cursor.close()
            connection.close()

def update_driver_profile(driver, user):
    connection = mysql_connection()
    result = False
    cursor = None
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "UPDATE driver SET name= %s, phone_no = %s, address = %s, gender = %s, license = %s WHERE driver_id = %s"
            values = ( driver.get_name(), driver.get_phone_no(), driver.get_address(), driver.get_gender(), driver.get_license(),driver.get_driver_id())
            cursor.execute(query, values)

            user_update_query = "UPDATE user SET email = %s WHERE user_id = %s"
            data = (user.get_email(), user.get_user_id())
            cursor.execute(user_update_query, data)

            connection.commit()
            result = True
        except Exception as error:
            messagebox.showerror("ERROR", f"{error}")
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

# =========== TO FETCH THE DRIVER PROFILE DETAILS ====================
def get_profile_details(driver, user):
    connection = None
    cursor = None
    driver_details = None
    user_details = None

    connection = mysql_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = """SELECT * FROM driver WHERE driver_id = %s """
            values = (driver.get_driver_id(),)
            cursor.execute(query, values)
            driver_details = cursor.fetchone()

            user_query = """ SELECT * FROM user WHERE user_id = %s """
            value = (user.get_user_id(),)
            cursor.execute(user_query,value)
            user_details = cursor.fetchone()

        except Exception as error:
            print(f"ERROR: {error}")
        finally:
            cursor.close()
            connection.close()
            return driver_details, user_details

def check_active_status(driver):
    connection = None
    cursor = None
    driver_active_status = None

    connection = mysql_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = """SELECT driver_status FROM driver WHERE driver_id = %s """
            values = (driver.get_driver_id(),)
            cursor.execute(query, values)
            driver_details = cursor.fetchone()
            driver_active_status = driver_details[0]

        except Exception as error:
            print(f"ERROR: {error}")
        finally:
            cursor.close()
            connection.close()
            return driver_active_status