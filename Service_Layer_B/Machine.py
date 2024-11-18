from datetime import datetime, timedelta
from .User import User

class Machine:
    """
    A class representing a washer or dryer machine
    """
    def __init__(self, machine_type, machine_id):
        """
        Creates a new instance of a Machine

        Args:
            machine_type (str): either a washer or dryer

        Raises:
            ValueError: raises error if the machine type is not a washer or dryer
        """
        if machine_type.title() == 'Washer' or machine_type.title() == 'Dryer':
            self._machine_type = machine_type
        else:
            raise ValueError("Invalid machine type")

        self._current_state = 'Available'
        self.id = machine_id
        self._start_time = None
        self._end_time = None
        self._who_is_using = None

    @property
    def current_state(self):
        """Getter for the current state."""
        return self._current_state

    def update_state(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not isinstance(value[1], User):
            raise TypeError("Invalid state or user type")
        
        next_state = value[0]
        user = value[1]

        if next_state == "Out of Order" and user.is_admin == True:
            self._current_state = "Out of Order"
            return
        
        if next_state == "Out of Order" and user.is_admin == False:
            raise ValueError("Only admins can set the machine to 'Out of Order'")

        if self._current_state == 'Available' and next_state == 'In Use':
            # Starting cycle
            self._start_time = datetime.now()
            self._current_state = 'In Use'
            self._who_is_using = user.user_name
            time_change = timedelta(minutes=1 if self._machine_type == 'Washer' else 1)
            self._end_time = self._start_time + time_change
        elif self._current_state == 'In Use' and next_state == 'Available':
            # Ending cycle
            self._current_state = 'Available'
            self._who_is_using = None  
            self._end_time = None
            self._start_time = None
        else:
            raise ValueError("Invalid state transition")

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time=None):
        self._start_time = start_time if start_time else datetime.now()

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time

    @property
    def machine_type(self):
        return self._machine_type

    @machine_type.setter
    def machine_type(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not isinstance(value[1], User):
            raise TypeError("Invalid machine type or user type")
        
        machine_type = value[0]
        user = value[1]

        if not isinstance(user, User):
            raise TypeError("User must be an instance of User")

        if user.is_admin == False:
            raise PermissionError("User does not have permission to change machine type")

        if machine_type.title() == 'Washer' or machine_type.title() == 'Dryer':
            self._machine_type = machine_type
        else:
            raise ValueError("Invalid machine type")

    @property
    def who_is_using(self):
        return self._who_is_using
    
    @who_is_using.setter
    def who_is_using(self, user_name):
        self._who_is_using = user_name

    def to_dict(self):
        """Convert the machine instance to a dictionary."""
        return {
            "machine_type": self._machine_type,
            "id": self.id,
            "current_state": self._current_state,
            "start_time": self._start_time.isoformat() if self._start_time else None,
            "end_time": self._end_time.isoformat() if self._end_time else None,
            "who_is_using": self._who_is_using
        }
