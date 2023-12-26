class Payment:
    def __init__(self, payment_id=0, distance=0, total_amount=0, date=None, is_generated=False, payment_status=None, booking_id=0):
        self._payment_id = payment_id
        self._total_amount = total_amount
        self._date = date
        self._distance = distance
        self._is_generated = is_generated
        self._payment_status = payment_status
        self._booking_id = booking_id

    # Getter Methods
    def get_payment_id(self):
        return self._payment_id

    def get_total_amount(self):
        return self._total_amount

    def get_date(self):
        return self._date

    def get_distance(self):
        return self._distance

    def get_is_generated(self):
        return self._is_generated

    def get_payment_status(self):
        return self._payment_status

    def get_booking_id(self):
        return self._booking_id

    # Setter Methods
    def set_payment_id(self, payment_id):
        self._payment_id = payment_id

    def set_total_amount(self, total_amount):
        self._total_amount = total_amount

    def set_date(self, date):
        self._date = date

    def set_distance(self, distance):
        self._distance = distance

    def set_is_generated(self, is_generated):
        self._is_generated = is_generated

    def set_payment_status(self, payment_status):
        self._payment_status = payment_status

    def set_booking_id(self, booking_id):
        self._booking_id = booking_id
