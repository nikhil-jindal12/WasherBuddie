from datetime import datetime

class Machine:
    def __init__(self, current_state='', start_time=None, end_time=None, functionality_state=0):
        self._current_state = current_state
        self._start_time = start_time if start_time else datetime.now()
        self._end_time = end_time
        self._functionality_state = functionality_state
        self._machine_type = machine_type

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        self._current_state = current_state

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time

    @property
    def functionality_state(self):
        return self._functionality_state

    @functionality_state.setter
    def functionality_state(self, functionality_state):
        self._functionality_state = functionality_state

    @property
    def machine_type(self):
        return self._machine_type
    
    @machine_type.setter
    def machine_type(self, machine_type):
        self._machine_type = machine_type