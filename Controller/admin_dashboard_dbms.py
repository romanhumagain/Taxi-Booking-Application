from Controller.connection import mysql_connection
from Model.booking import Booking
def fetch_customer_booking():
      connection = mysql_connection()
      if connection is not None:
          cursor = None
          result = None
          try:
              cursor = connection.cursor()

              query = "SELECT booked_date, COUNT(*) FROM booking GROUP BY booked_date"

              cursor.execute(query)
              result = cursor.fetchall()

          except Exception as error:
              print(error)
          finally:
              cursor.close()
              connection.close()
              return result


def fetch_pending_booking_details():
    connection = mysql_connection()
    if connection is not None:
        cursor = None
        result = None
        try:
            cursor = connection.cursor()

            query = """ SELECT booking_id, customer.customer_id, name, pickup_address, pickup_date, pickup_time, dropoff_address, booking_status
                        FROM customer 
                        INNER JOIN booking 
                        ON customer.customer_id = booking.customer_id """

            cursor.execute(query)
            result = cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

def search_booking_details(booking):
    connection = mysql_connection()
    if connection is not None:
        cursor = None
        result = None
        try:
            cursor = connection.cursor()

            query = """ SELECT booking_id, customer.customer_id, name, pickup_address, pickup_date, pickup_time, dropoff_address, booking_status
                        FROM customer 
                        INNER JOIN booking 
                        ON customer.customer_id = booking.customer_id
                        WHERE booking_id = %s
                        """
            values =(booking.get_booking_id(),)

            cursor.execute(query, values)
            result = cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result
