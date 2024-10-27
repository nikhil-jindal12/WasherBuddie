from datetime import datetime
from datetime import timedelta
import User

class Machine:
    """
    A class representing a washer or dryer machine
    """

    _machine_type = None
    _current_state = None
    _start_time = None
    _end_time = None
    _who_is_using = None
    
    def __init__(self, machine_type):
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
            raise ValueError()

        self._current_state = 'Available'
        self._start_time = None
        self._end_time = None
        self._who_is_using = None
       
    @property
    def get_current_state(self):
        """
        Returns the current state of the machine

        Returns:
            boolean: Available, In Use, or Out of Order
        """
        return self._current_state

    @get_current_state.setter
    def set_current_state(self, current_state, user):
        """
        Sets the current state of the washer and the start and end times

        Args:
            current_state (str): new state of the washer
            
        Raises:
            TypeError: raises error if state is not recognized
        """
        if type(user) != User:
            raise TypeError()
        
        if Machine.get_current_state() == 'Available' and current_state == 'In Use':
            # starting cycle
            self._start_time = datetime.now()
            if Machine.get_machine_type == 'Washer':
                self._current_state = 'In Use'
                Machine.set_who_is_using(user.get_user_name())
                time_change = timedelta(minutes=50)
                Machine.set_end_time(Machine.get_start_time() + time_change)
            elif Machine.get_machine_type == 'Dryer':
                self._current_state = 'In Use'
                Machine.set_who_is_using(user.get_user_name())
                time_change = timedelta(minutes=60)
                Machine.set_end_time(Machine.get_start_time() + time_change)
        elif Machine.get_current_state() == 'In Use' and current_state == 'Available':
            # ending cycle
            self._current_state = 'Available'
            Machine.set_who_is_using(None)
            self._end_time = None
            self._start_time = None
        elif user.get_is_admin() and ((Machine.get_current_state() == 'Out of Order' and current_state == 'Available') or current_state == 'Out of Order'):
            # only admins can set machines to be out of order
            self._current_state = 'Available'
            Machine.set_who_is_using(None)
            self._end_time = None
            self._start_time = None
        else:
            raise ValueError()

    @property
    def get_start_time(self):
        """
        Returns the time the machine cycle was started

        Returns:
            DateTime: date and time the machine cycle was started
        """
        return self._start_time

    @get_current_state.setter
    def set_start_time(self, start_time=datetime.now()):
        """
        Sets the time the machine cycle was started

        Args:
            start_time (DateTime, optional): Specific time. Defaults to datetime.now().
        """        
        self._start_time = start_time

    @property
    def get_end_time(self):
        """
        Returns the time the machine cycle will end

        Returns:
            DateTime: date and time the machine cycle will end 
        """
        return self._end_time

    @get_end_time.setter
    def set_end_time(self, end_time):
        """
        Sets the time the machine cycle will end

        Args:
            end_time (DateTime): date and time the machine cycle will end
        """
        self._end_time = end_time

    @property
    def get_machine_type(self):
        """
        Returns the type of machine

        Returns:
            str: 'Washer' or 'Dryer'
        """
        return self._machine_type
    
    @get_machine_type.setter
    def set_machine_type(self, machine_type, user):
        """
        Sets the type of machine

        Args:
            machine_type (str): 'Washer' or 'Dryer
            
        Raises:
            ValueError: Raises error if the machine type is not a washer or dryer
            TypeError: Raises error if the user is not of type User
            PermissionError: Raises error if the user is not an admin
        """
        if type(user) != User:
            raise TypeError()
        
        if not user.get_is_admin():
            raise PermissionError()
        
        if machine_type.title() == 'Washer' or machine_type.title() == 'Dryer':
            self._machine_type = machine_type
        else:
            raise ValueError()
                
    @property
    def get_who_is_using(self):
        """
        Returns the user who is currently using the machine

        Returns:
            str: current machine user's name
        """
        return self._who_is_using
    
    @get_who_is_using.setter
    def set_who_is_using(self, user_name):
        """
        Sets the user who is currently using the machine

        Args:
            user_name (str): current machine user's name
        """
        self._who_is_using = user_name