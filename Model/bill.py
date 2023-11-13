class Bill:
    def __init__(self, bill_id=0, total_amount=0, date=None, distance=0, unit=0, customer_id=0, booking_id=0):
        self._bill_id = bill_id
        self._total_amount = total_amount
        self._date = date
        self._distance = distance
        self._unit = unit
        self._customer_id = customer_id
        self._booking_id = booking_id

    # Getter Methods
    def get_bill_id(self):
        return self._bill_id

    def get_total_amount(self):
        return self._total_amount

    def get_date(self):
        return self._date

    def get_distance(self):
        return self._distance

    def get_unit(self):
        return self._unit

    def get_customer_id(self):
        return self._customer_id

    def get_booking_id(self):
        return self._booking_id

    # Setter Methods
    def set_bill_id(self, bill_id):
        self._bill_id = bill_id

    def set_total_amount(self, total_amount):
        self._total_amount = total_amount

    def set_date(self, date):
        self._date = date

    def set_distance(self, distance):
        self._distance = distance

    def set_unit(self, unit):
        self._unit = unit

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_booking_id(self, booking_id):
        self._booking_id = booking_id
