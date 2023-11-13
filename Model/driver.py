class Driver:
    def __init__(self, driver_id=0, name=None, phone_no=None, address=None, gender=None, license=None, user_id=0):
        self._driver_id = driver_id
        self._name = name
        self._phone_no = phone_no
        self._address = address
        self._gender = gender
        self._license = license
        self._user_id = user_id

    # Getter Methods
    def get_driver_id(self):
        return self._driver_id

    def get_name(self):
        return self._name

    def get_phone_no(self):
        return self._phone_no

    def get_license(self):
        return self._license

    def get_address(self):
        return self._address

    def get_gender(self):
        return self._gender

    def get_user_id(self):
        return self._user_id

    # Setter Methods
    def set_driver_id(self, driver_id):
        self._driver_id = driver_id

    def set_name(self, name):
        self._name = name

    def set_phone_no(self, phone_no):
        self._phone_no = phone_no

    def set_license(self, license):
        self._license = license

    def set_address(self, address):
        self._address = address

    def set_gender(self, gender):
        self._gender = gender

    def set_user_id(self, user_id):
        self._user_id = user_id
