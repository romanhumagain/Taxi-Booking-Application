class AccountActivity:
    def __init__(self, activity_id=0, activity_related=None, description=None, date=None, time=None, user_id=0):
        self._activity_id = activity_id
        self._activity_related = activity_related
        self._description = description
        self._date = date
        self._time = time
        self._user_id = user_id

    def get_activity_id(self):
        return self._activity_id

    def set_activity_id(self, value):
        self._activity_id = value

    def get_activity_related(self):
        return self._activity_related

    def set_activity_related(self, value):
        self._activity_related = value

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    def get_date(self):
        return self._date

    def set_date(self, value):
        self._date = value

    def get_time(self):
        return self._time

    def set_time(self, value):
        self._time = value

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value):
        self._user_id = value
