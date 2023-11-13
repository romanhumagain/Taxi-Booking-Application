from Controller.connection import mysql_connection
from Model.customer import Customer
from Model.user import User
from tkinter import  messagebox

def register_user(user):
    try:
        connection = mysql_connection()
        if connection is not None:
            # create a cursor object
            cursor = connection.cursor()

            # sql query to insert data into the table
            query = "INSERT INTO user(email, password, user_type) VALUES (%s, %s, %s)"
            values = (
                      user.get_email(),
                      user.get_password(),
                      user.get_user_type())

            # to execute the query
            cursor.execute(query, values)

            # to commit the changes
            connection.commit()

            # get the primary key of the currently inserted data's primary key
            user_id = cursor.lastrowid

            user.set_user_id(user_id)

            return True

    except Exception as error:
        print(f"ERROR {error}")
        return False

    finally:
        cursor.close()
        connection.close()

def register_customer(customer, user):
    try:
        connection = mysql_connection()
        if connection is not None:
            # create a cursor object
            cursor = connection.cursor()

            # sql query to insert data into the table
            query = "INSERT INTO customer( name, phone_no, payment, address, date_of_birth, gender, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (
                      customer.get_name(),
                      customer.get_phone_no(),
                      customer.get_payment(),
                      customer.get_address(),
                      customer.get_date_of_birth(),
                      customer.get_gender(),
                      user.get_user_id())

            # to execute the query
            cursor.execute(query, values)

            # to commit the changes
            connection.commit()
            return True

    except Exception as error:
        print(f"ERROR {error}")
        return False
    finally:
        cursor.close()
        connection.close()
