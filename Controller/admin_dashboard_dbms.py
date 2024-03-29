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
                        ON customer.customer_id = booking.customer_id WHERE booking_status = %s ORDER BY booking_id DESC """

            cursor.execute(query, ("pending",))
            result = cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

def fetch_total_booking():
    connection = mysql_connection()
    if connection is not None:
        cursor = None
        result = None
        try:
            cursor = connection.cursor()

            query = """ SELECT * FROM booking """

            cursor.execute(query)
            result = cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

def fetch_total_driver():
    connection = mysql_connection()
    if connection is not None:
        cursor = None
        result = None
        try:
            cursor = connection.cursor()

            query = """ SELECT * FROM user WHERE user_type = %s """

            cursor.execute(query, ("driver",))
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


def fetch_active_booking():
    connection = mysql_connection()
    if connection is not None:
        cursor = None
        result = None
        try:
            cursor = connection.cursor()

            query = """ SELECT booking.booking_id, booking.customer_id, pickup_address, pickup_date, pickup_time, dropoff_address, booking.driver_id, driver.name
                        FROM booking 
                        INNER JOIN customer ON booking.customer_id = customer.customer_id  
                        INNER JOIN driver ON booking.driver_id = driver.driver_id 
                        WHERE booking.booking_status = %s;
                    """

            cursor.execute(query, ("approved",))
            result = cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

def fetch_booking_history():
    connection = mysql_connection()
    if connection is not None:
        cursor = None
        result = None
        try:
            cursor = connection.cursor()

            query = """ SELECT booking.booking_id, booking.customer_id, pickup_address, pickup_date, pickup_time, dropoff_address, booking.driver_id, driver.name,booking_status
                        FROM booking 
                        INNER JOIN customer ON booking.customer_id = customer.customer_id  
                        INNER JOIN driver ON booking.driver_id = driver.driver_id 
                        WHERE booking.booking_status = %s OR booking.booking_status = %s;
                    """

            cursor.execute(query, ("approved","completed"))
            result = cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

def fetch_completed_booking():
    connection = mysql_connection()
    if connection is not None:
        cursor = None
        result = None
        try:
            cursor = connection.cursor()

            query = """ SELECT booking.booking_id, booking.customer_id, pickup_address, pickup_date, pickup_time, dropoff_address, booking.driver_id, driver.name, booking.trip_status
                        FROM booking 
                        INNER JOIN customer ON booking.customer_id = customer.customer_id  
                        INNER JOIN driver ON booking.driver_id = driver.driver_id 
                        WHERE booking.trip_status = %s;
                    """

            cursor.execute(query, ("Completed",))
            result = cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result

def search_booking_history(booking):
    connection = mysql_connection()
    if connection is not None:
        cursor = None
        result = None
        try:
            cursor = connection.cursor()
            query = """     SELECT booking_id, booking.customer_id, pickup_address, pickup_date, pickup_time, dropoff_address,booking.driver_id, driver.name, booking_status
                            FROM booking 
                            JOIN customer 
                            ON booking.customer_id = customer.customer_id
                            JOIN driver 
                            ON booking.driver_id = driver.driver_id
                            WHERE booking_id = %s
                    """
            values = (booking.get_booking_id(),)

            cursor.execute(query, values)
            result = cursor.fetchall()

        except Exception as error:
            print(error)
        finally:
            cursor.close()
            connection.close()
            return result


