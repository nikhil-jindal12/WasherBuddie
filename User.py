class User:
    def __init__(self, user_name='', user_number=0, user_email='', notification_preference=False, is_admin=False):
        self._user_name = user_name
        self._user_number = user_number
        self._user_email = user_email
        self._notification_preference = notification_preference
        self._is_admin = is_admin

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    @property
    def user_number(self):
        return self._user_number

    @user_number.setter
    def user_number(self, user_number):
        self._user_number = user_number

    @property
    def user_email(self):
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        self._user_email = user_email

    @property
    def notification_preference(self):
        return self._notification_preference

    @notification_preference.setter
    def notification_preference(self, notification_preference):
        self._notification_preference = notification_preference

    @property
    def is_admin(self):
        return self._is_admin
