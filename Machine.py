from datetime import datetime

class Machine:
    def __init__(self, machine_type, current_state='', start_time=None, end_time=None, functionality_state=0):
        self._current_state = current_state
        self._start_time = start_time if start_time else datetime.now()
        self._end_time = end_time
        self._functionality_state = functionality_state
        self._machine_type = machine_type

    @property
    def get_current_state(self):
        return self._current_state

    @get_current_state.setter
    def set_current_state(self, current_state):
        self._current_state = current_state

    @property
    def get_start_time(self):
        return self._start_time

    @get_current_state.setter
    def set_start_time(self, start_time):
        self._start_time = start_time

    @property
    def get_end_time(self):
        return self._end_time

    @get_end_time.setter
    def set_end_time(self, end_time):
        self._end_time = end_time

    @property
    def get_functionality_state(self):
        return self._functionality_state

    @get_functionality_state.setter
    def set_functionality_state(self, functionality_state):
        self._functionality_state = functionality_state

    @property
    def get_machine_type(self):
        return self._machine_type
    
    @get_machine_type.setter
    def set_machine_type(self, machine_type):
        self._machine_type = machine_type