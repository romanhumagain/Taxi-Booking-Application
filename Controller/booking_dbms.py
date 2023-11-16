from Controller.connection import mysql_connection
from Model.booking import Booking

def booking_taxi(booking):
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()

            # query for insert
            query = """INSERT INTO booking(pickup_address, pickup_date, pickup_time, dropoff_address,booking_status) VALUES (%s, %s, %s, %s, %s)"""
            values = (
                booking.get_pickup_address(),
                booking.get_pickup_date(),
                booking.get_pickup_time(),
                booking.get_dropoff_address(),
                booking.get_booking_status()
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

def select_pending_booking():
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query  = "SELECT * FROM booking WHERE customer_id = %s and booking_status = %s"
            values =(97, "Pending")

            cursor.execute(query, values)

            result = cursor.fetchall()
            if result is not None:
                return result
            return result

    except Exception as error:
        print(f"ERROR:- {error}")

    finally:
        cursor.close()
        connection.close()
