from Controller.connection import mysql_connection
from Model.payment import Payment
from Model.customer import Customer

def create_payment_table(payment):
    connection = None
    cursor = None

    try:
        connection = mysql_connection()
        if connection is not None:
            # create a cursor object
            cursor = connection.cursor()

            # sql query to insert data into the table
            query = "INSERT INTO payment(is_generated, payment_status, booking_id) VALUES (%s,%s,%s)"
            values = (False,"Pending",payment.get_booking_id(),)

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

# ====== TO GENERATE THE PAYMENT OF THE SPECIFIC BOOKING ============
def generate_payment(payment):
    connection = None
    cursor = None
    try:
        connection = mysql_connection()
        if connection is not None:
            # create a cursor object
            cursor = connection.cursor()

            # sql query to insert data into the table
            query = "UPDATE payment SET distance = %s, total_amount = %s, is_generated = %s, date = %s  WHERE booking_id = %s"
            values = (payment.get_distance(), payment.get_total_amount(), payment.get_is_generated(), payment.get_date(), payment.get_booking_id())

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


# ==== TO VIEW THE UNGENERATED PAYMENT =========
def fetch_pending_payment():
    connection = None
    cursor = None
    result = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """
                SELECT payment.booking_id, customer.customer_id, pickup_address, dropoff_address, booking.pickup_date
                FROM booking 
                INNER JOIN payment ON booking.booking_id = payment.booking_id
                INNER JOIN customer ON booking.customer_id = customer.customer_id 
                WHERE payment.is_generated = %s AND NOT booking.booking_status = %s
            """
            values = (False, "Pending")

            cursor.execute(query, values)
            result = cursor.fetchall()
    except Exception as error:
        print(f"ERROR {error}")
    finally:
        cursor.close()
        connection.close()
        return result

def fetch_pending_payment_details():
    connection = None
    cursor = None
    result = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """
                    SELECT payment.booking_id,customer.customer_id, name, pickup_address, dropoff_address, booking.pickup_date, payment_status
                    FROM booking 
                    INNER JOIN payment
                    ON booking.booking_id = payment.booking_id
                    INNER JOIN customer
                    ON booking.customer_id = customer.customer_id 
                    WHERE payment.is_generated = %s AND NOT booking.booking_status = %s
                    """
            values = (False,"Pending")
            cursor.execute(query, values)
            result = cursor.fetchall()
    except Exception as error:
        print(f"ERROR {error}")
    finally:
        cursor.close()
        connection.close()
        return result

def fetch_completed_payment():
    connection = None
    cursor = None
    result = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """
                    SELECT payment_id, payment.booking_id, pickup_address, dropoff_address, payment.date, distance, total_amount
                    FROM booking 
                    INNER JOIN payment
                    ON booking.booking_id = payment.booking_id
                    INNER JOIN customer
                    ON booking.customer_id = customer.customer_id 
                    WHERE payment.is_generated = %s
                    """
            values = (True,)
            cursor.execute(query, values)
            result = cursor.fetchall()

    except Exception as error:
        print(f"ERROR {error}")

    finally:
        cursor.close()
        connection.close()
        return result

# =========== TO FETCH THE COMPLETED PAYMENT DETAILS FOR THE SPECIFIC CUSTOMER
def fetch_customer_completed_payment(customer):
    connection = None
    cursor = None
    result = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """
                    SELECT payment_id, payment.booking_id, pickup_address, dropoff_address, payment.date, distance, total_amount
                    FROM booking 
                    INNER JOIN payment
                    ON booking.booking_id = payment.booking_id
                    INNER JOIN customer
                    ON booking.customer_id = customer.customer_id 
                    WHERE payment.payment_status = %s and customer.customer_id = %s 
                    ORDER BY payment_id DESC
                    """
            values = ("Paid",customer.get_customer_id())
            cursor.execute(query, values)
            result = cursor.fetchall()

    except Exception as error:
        print(f"ERROR {error}")

    finally:
        cursor.close()
        connection.close()
        return result

# =========== TO SEARCH CUSTOMER COMPLETED PAYMENT DETAILS ============
def search_customer_completed_payment(customer, payment):
    connection = None
    cursor = None
    result = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """
                    SELECT payment_id, payment.booking_id, pickup_address, dropoff_address, payment.date, distance, total_amount
                    FROM booking 
                    INNER JOIN payment
                    ON booking.booking_id = payment.booking_id
                    INNER JOIN customer
                    ON booking.customer_id = customer.customer_id 
                    WHERE payment.payment_status = %s and customer.customer_id = %s and payment_id = %s 
                    """
            values = ("Success",customer.get_customer_id(), payment.get_payment_id())
            cursor.execute(query, values)
            result = cursor.fetchall()

    except Exception as error:
        print(f"ERROR {error}")

    finally:
        cursor.close()
        connection.close()
        return result


