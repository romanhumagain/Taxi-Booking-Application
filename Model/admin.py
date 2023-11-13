class Admin:
    def __init__(self, admin_id=0, name=None, phone_no=None, address=None, gender=None, user_id=0):
        self._admin_id = admin_id
        self._name = name
        self._phone_no = phone_no
        self._address = address
        self._gender = gender
        self._user_id = user_id

    # Getter Methods
    def get_admin_id(self):
        return self.admin_id

    def get_name(self):
        return self._name

    def get_phone_no(self):
        return self._phone_no

    def get_address(self):
        return self._address

    def get_gender(self):
        return self._gender

    def get_user_id(self):
        return self._user_id

    # Setter Methods
    def set_admin_id(self, admin_id):
        self._admin_id = admin_id

    def set_name(self, name):
        self._name = name

    def set_phone_no(self, phone_no):
        self._phone_no = phone_no

    def set_address(self, address):
        self._address = address

    def set_gender(self, gender):
        self._gender = gender

    def set_user_id(self, user_id):
        self._user_id = user_id

