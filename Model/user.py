class User:
    def __init__(self, user_id = 0, email = None, password = None, user_type = None):
        self._user_id = user_id
        self._email = email
        self._password = password
        self._user_type = user_type

    # Getter Method
    def get_user_id(self):
        return self._user_id

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_user_type(self):
        return self._user_type

    # Setter Method
    def set_user_id(self, user_id):
        self._user_id = user_id

    def set_email(self, email):
        self._email = email

    def set_password(self, password):
        self._password = password

    def set_user_type(self, user_type):
        self._user_type = user_type