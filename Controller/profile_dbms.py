from Controller.connection import *
# from Model.customer import Customer
from Model import Global

# ======================= TO GET THE CUSTOMER PROFILE INFO ============================
def profile_details(customer):
    customer_profile_details = None
    user = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()

            query = "SELECT * FROM customer WHERE customer_id =%s "
            values = (customer.get_customer_id(),)

            cursor.execute(query, values)

            customer_profile_details = cursor.fetchone()
            if customer_profile_details is not None:
                cursor.execute("SELECT * FROM user WHERE user_id = %s ", (Global.current_user[0],))
                user = cursor.fetchone()

    except Exception as error:
        print(f"ERROR :- {error}")

    finally:
        cursor.close()
        connection.close()
        return customer_profile_details, user


# ====================== TO UPDATE THE CUSTOMER PROFILE DETAILS =========================
def update_customer_profile(customer, user):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            customer_update_query = "UPDATE customer SET name = %s, phone_no = %s, address = %s, payment = %s, date_of_birth = %s, gender = %s WHERE customer_id = %s"

            values = (customer.get_name(),
                      customer.get_phone_no(),
                      customer.get_address(),
                      customer.get_payment(),
                      customer.get_date_of_birth(),
                      customer.get_gender(),
                      customer.get_customer_id())

            cursor.execute(customer_update_query, values)

            user_update_query = "UPDATE user SET email = %s WHERE user_id = %s"
            values = (user.get_email(),user.get_user_id())
            cursor.execute(user_update_query, values)

            connection.commit()
            return True

    except Exception as error:
        print(f"ERROR:- {error}")
        return False
    finally:
        cursor.close()
        connection.close()



