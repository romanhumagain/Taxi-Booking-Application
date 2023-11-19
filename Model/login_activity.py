class LoginActivity:
    def __init__(self, activity_id=0, device_type=None, os=None, processor=None, node_device_name=None,
                 login_date=None, login_time=None, user_id=0):
        self._activity_id = activity_id
        self._device_type = device_type
        self._os = os
        self._processor = processor
        self._node_device_name = node_device_name
        self._login_date = login_date
        self._login_time = login_time
        self._user_id = user_id

    # Getter methods
    def get_activity_id(self):
        return self._activity_id

    def get_device_type(self):
        return self._device_type

    def get_os(self):
        return self._os

    def get_processor(self):
        return self._processor

    def get_node_device_name(self):
        return self._node_device_name

    def get_login_date(self):
        return self._login_date

    def get_login_time(self):
        return self._login_time

    def get_user_id(self):
        return self._user_id

    # Setter methods
    def set_activity_id(self, activity_id):
        self._activity_id = activity_id

    def set_device_type(self, device_type):
        self._device_type = device_type

    def set_os(self, os):
        self._os = os

    def set_processor(self, processor):
        self._processor = processor

    def set_node_device_name(self, node_device_name):
        self._node_device_name = node_device_name

    def set_login_date(self, login_date):
        self._login_date = login_date

    def set_login_time(self, login_time):
        self._login_time = login_time

    def set_user_id(self, user_id):
        self._user_id = user_id

