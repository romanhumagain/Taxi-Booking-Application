from Controller.connection import mysql_connection
from Model.booking import Booking

# ================== TO INSERT RECORD TO THE BOOKING TABLE ====================
def booking_taxi(booking):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()

            # query for insert
            query = """INSERT INTO booking(pickup_address, pickup_date, pickup_time, dropoff_address,booking_status, booked_date, customer_id) VALUES (%s, %s, %s, %s,%s, %s, %s)"""
            values = (
                booking.get_pickup_address(),
                booking.get_pickup_date(),
                booking.get_pickup_time(),
                booking.get_dropoff_address(),
                booking.get_booking_status(),
                booking.get_booked_date(),
                booking.get_customer_id()
            )
            cursor.execute(query, values)
            connection.commit()

            return True
    except Exception as e:
        print(f"ERROR {e}")
        return False
    finally:
        cursor.close()
        connection.close()

# ================= TO SELECT ALL BOOKING OF A SPECIFIC CUSTOMER ===============
def select_all_booking(booking):
    result = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query  = "SELECT * FROM booking WHERE customer_id = %s ORDER BY booking_id DESC"
            values =(booking.get_customer_id(),)

            cursor.execute(query, values)
            result = cursor.fetchall()

    except Exception as error:
        print(f"ERROR:- {error}")

    finally:
        cursor.close()
        connection.close()
        return result




# ================== TO SELECT THE PENDING BOOKING =====================
def select_pending_booking(booking):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query  = "SELECT * FROM booking WHERE customer_id = %s and booking_status = %s ORDER BY booking_id DESC"
            values =(booking.get_customer_id(), "Pending")

            cursor.execute(query, values)
            result = cursor.fetchall()

            return result

    except Exception as error:
        print(f"ERROR:- {error}")

    finally:
        cursor.close()
        connection.close()


# ================== TO SELECT THE APPROVED BOOKING =====================
def select_approved_booking(booking):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query  = "SELECT * FROM booking WHERE customer_id = %s and booking_status = %s ORDER BY booking_id DESC"
            values =(booking.get_customer_id(), "Approved")

            cursor.execute(query, values)
            result = cursor.fetchall()

            return result

    except Exception as error:
        print(f"ERROR:- {error}")

    finally:
        cursor.close()
        connection.close()


# ================== TO UPDATE THE BOOKING =========================
def update_booking(booking):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()

            # Query to update the booking
            query = """ UPDATE booking SET pickup_address = %s, pickup_date = %s , pickup_time = %s, dropoff_address = %s WHERE booking_id = %s """
            values = (
                booking.get_pickup_address(),
                booking.get_pickup_date(),
                booking.get_pickup_time(),
                booking.get_dropoff_address(),
                booking.get_booking_id()
            )

            # To execute the query
            cursor.execute(query, values)

            connection.commit()
            return True

    except Exception as error:
        print(f"ERROR:- {error}")
        return False
    finally:
        cursor.close()
        connection.close()


# =================== TO CANCEL THE BOOKING =========================
def cancel_booking(booking):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()

            # Query to update the booking
            query = " DELETE FROM booking WHERE booking_id = %s "
            values = (
                booking.get_booking_id(),
            )

            # To execute the query
            cursor.execute(query, values)

            connection.commit()
            return True

    except Exception as error:
        print(f"ERROR:- {error}")
        return False
    finally:
        cursor.close()
        connection.close()
