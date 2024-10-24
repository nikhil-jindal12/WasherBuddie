class User:
    def __init__(self, user_name, user_email, phone_carrier, notification_preference, user_phone_number='', is_admin=False):
        """
        Creates a new instance of a User

        Args:
            user_name (str): The first and last name of the user
            user_email (str): The user's preferred email address to receive notifications
            phone_carrier (str): User's mobile phone carrier to receive text messages through our system
                                    Should be part of a list that is to be specified...            notification_preference (_type_): _description_
            user_phone_number (int): The user's 10 digit phone number. Defaults to ''.
            is_admin (bool, optional): Whether or not the user has administrative functions. Defaults to False.

        Raises:
            ValueError: Raises error if the user did not input their first and last name
            ValueError: Raises error if the user did not input a valid email address or phone number
            ValueError: Raises error if the user did not correctly indicate how they would like to be notified
        """
        
        # checks if the user input their first and last name
        if len(user_name.split()) == 2:
            self._user_name = user_name
        else:
            raise ValueError()
        
        if len(user_phone_number) == 10:
            # check if the user input a 10 digit phone number
            self._user_phone_number = user_phone_number
            self._phone_carrier = phone_carrier
            self._user_email = user_email
        elif len(user_phone_number) == '' and len(user_email) > 0 and '@' in user_email and '.' in user_email:
            # if the user did not input a phone number, they must input a valid email address
            self._user_phone_number = None
            self._phone_carrier = None
            self._user_email = user_email
        else:
            raise ValueError()
        
        # users can only be notified via text or email
        if notification_preference is 'Email' or 'Text':
            self._notification_preference = notification_preference
        else:
            raise ValueError()
        
        self._is_admin = is_admin

    @property
    def get_user_name(self):
        """
        Returns the user's name

        Returns:
            str: user's name
        """
        return self._user_name

    @get_user_name.setter
    def set_user_name(self, user_name):
        """
        Sets the user's name

        Args:
            user_name (str): user's updated name
        """
        self._user_name = user_name

    @property
    def get_user_phone_number(self):
        """
        Returns the user's 

        Returns:
            _type_: _description_
        """
        return self._user_phone_number

    @get_user_phone_number.setter
    def set_user_phone_number(self, user_phone_number):
        """
        Sets the user's phone number

        Args:
            user_phone_number (int): user's new phone number

        Raises:
            ValueError: Raises error if user tries to input a non 10-digit phone number
        """        
        if len(user_phone_number) == 10 or len(user_phone_number) == 0:
            self._user_phone_number = user_phone_number
        else:
            raise ValueError()

    @property
    def get_user_email(self):
        """
        Returns the user's email

        Returns:
            str: user's email
        """
        return self._user_email

    @get_user_email.setter
    def set_user_email(self, user_email):
        """
        Sets the user's email

        Args:
            user_email (str): user's new email

        Raises:
            ValueError: Raises error if the email address does not have an @ and . in it
        """
        if '@' in user_email and '.' in user_email:
            self._user_email = user_email
        else:
            raise ValueError()

    @property
    def get_notification_preference(self):
        """
        Returns the user's notification preference

        Returns:
            str: user's notification preference
        """
        return self._notification_preference

    @get_notification_preference.setter
    def set_notification_preference(self, notification_preference):
        """
        Sets the user's notification preference

        Args:
            notification_preference (str): user's new notification preference

        Raises:
            ValueError: Raises error if the user inputs anything besides Text or Email as their notification preference
        """        
        if notification_preference.title() == 'Text' or notification_preference.title() == 'Email':
            self._notification_preference = notification_preference
        else:
            raise ValueError()
        
    @property
    def get_phone_carrier(self):
        """
        Returns the user's phone carrier

        Returns:
            str: valid phone carrier within the United States
        """        
        return self._phone_carrier
    
    @get_phone_carrier.setter
    def set_phone_carrier(self, phone_carrier):
        """
        Sets the user's phone carrier

        Args:
            phone_carrier (str): user's new phone carrier
        """
        self._phone_carrier = phone_carrier

    @property
    def get_is_admin(self):
        """
        Returns whether or not a user is an administrator

        Returns:
            boolean: True or False
        """
        return self._is_admin
