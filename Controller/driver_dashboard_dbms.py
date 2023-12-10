from Controller.connection import mysql_connection
from Model.driver import Driver

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
                        WHERE driver.driver_id = %s
                    """
            values = (driver.get_driver_id(),)
            cursor.execute(query, values)
            result = cursor.fetchall()
        except Exception as error:
            print(f"ERROR: {error}")
        finally:
            cursor.close()
            connection.close()
            return result
