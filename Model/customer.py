class Customer:
    def __init__(self, customer_id=0, name=None, phone_no=None, payment=None, address=None, date_of_birth=None, gender=None, user_id=0):
        self._customer_id = customer_id
        self._name = name
        self._phone_no = phone_no
        self._payment = payment
        self._address = address
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._user_id = user_id

    # Getter Methods
    def get_customer_id(self):
        return self._customer_id

    def get_name(self):
        return self._name

    def get_phone_no(self):
        return self._phone_no

    def get_payment(self):
        return self._payment

    def get_date_of_birth(self):
        return self._date_of_birth

    def get_address(self):
        return self._address

    def get_gender(self):
        return self._gender

    def get_user_id(self):
        return self._user_id

    # Setter Methods
    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_name(self, name):
        self._name = name

    def set_phone_no(self, phone_no):
        self._phone_no = phone_no

    def set_payment(self, payment):
        self._payment = payment

    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def set_address(self, address):
        self._address = address

    def set_gender(self, gender):
        self._gender = gender

    def set_user_id(self, user_id):
        self._user_id = user_id
