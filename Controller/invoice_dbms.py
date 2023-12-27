from Controller.connection import mysql_connection
from Model.payment import Payment

# ===== TO FETCH THE PAYMENT DETAILS OF THE SPECIFIC INVOICE NO. ===============
def fetch_payment_details(payment):
    connection = None
    cursor = None
    result = None
    try:
        connection = mysql_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = """
                    SELECT payment_id, payment.booking_id,customer.name, pickup_address, dropoff_address, payment.date, distance, total_amount
                    FROM booking 
                    INNER JOIN payment
                    ON booking.booking_id = payment.booking_id
                    INNER JOIN customer
                    ON booking.customer_id = customer.customer_id 
                    WHERE payment.payment_status = %s and payment.payment_id = %s
                    """
            values = ("Success",payment.get_payment_id())
            cursor.execute(query, values)
            result = cursor.fetchone()

    except Exception as error:
        print(f"ERROR {error}")

    finally:
        cursor.close()
        connection.close()
        return result
