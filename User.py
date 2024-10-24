class User:
    def __init__(self, user_name, notification_preference, user_phone_number, user_email, is_admin=False):
        if len(user_name) > 0:
            self._user_name = user_name
        else:
            raise ValueError()
        
        if len(user_phone_number) == 10:
            self._user_number = user_phone_number
        else:
            raise ValueError()
        
        self._user_email = user_email
        
        if notification_preference is 'Email' or 'Text':
            self._notification_preference = notification_preference
        else:
            raise ValueError()
        
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
