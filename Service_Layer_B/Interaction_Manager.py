from .Machine import Machine
from .User import User
import traceback
from .Notification_Manager import Notification_Manager
import datetime
import time
import threading


class Interaction_Manager:
    machine_count = 0
    Machines = {}
    Users = {}
    white_list = []

    def add_washer(self):
        """ Adds a new washing machine """
        try:
            washer = Machine('Washer', self.machine_count)
            self.Machines[self.machine_count] = washer
            self.machine_count += 1
            return True
        except Exception as e:
            print(f"Error adding washer: {e}")
            return False

    def add_dryer(self):
        """ Adds a new drying machine """
        try:
            dryer = Machine('Dryer', self.machine_count)
            self.Machines[self.machine_count] = dryer
            self.machine_count += 1
            return True  
        except Exception as e:
            print(f"Error adding dryer: {e}")
            return False

    def send_notification(self, sending_user, receiving_user, message):
        """ Sends a notification to another user from the current user """
        Notification_Manager.send_ping(sending_user, receiving_user, message)

    def add_user(self, user_name, notification_preference, user_phone_number, user_email, phone_carrier, is_admin=False):
        """ Adds a new user to the system """
        try:
            if user_name in self.Users:
                print(f"User with username {user_name} already exists.")
                return False

            user = User(user_name, user_email, phone_carrier, notification_preference, user_phone_number, is_admin)
            self.Users[user_name] = user 
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            print(traceback.format_exc())  # Print the stack trace for debugging
            return False

    def remove_user(self, user_name):
        """ Removes a user from the system """
        try:
            if user_name in self.Users:
                del self.Users[user_name]
                return True
            else:
                return False
        except Exception as e:
            print(f"Error removing user: {e}")
            return False

    def authenticate_log_in(self):
        """ Authenticates user logins (stub for future implementation) """
        return False

    def get_white_list(self):
        """ Returns the white list """
        try:
            return self.white_list
        except Exception as e:
            print(f"Error getting white list: {e}")
            return False
    
    def add_white_list(self, email):
        """ Returns the white list """
        if (len(email) > 0 and '@' in email and '.' in email) is not True:
            print("Not a valid email address")
            return False
        try:
            self.white_list.append(email)
            return True
        except Exception as e:
            print(f"Error getting white list: {e}")
            return False

    def create_session(self, machine, user, hours):
        """
        Sets the status for a machine to 'In Use' and associates the user with the machine.
        Defaults to a one-hour session if no end time is specified.
        """
        if not isinstance(machine, Machine) or not isinstance(user, User):
            raise TypeError("Invalid machine or user type")

        if machine.current_state != 'Available':
            raise ValueError(f"Machine {machine.machine_type} is not available")

        # Update machine state to 'In Use'
        machine.update_state(value=("In Use", user))

        # Calculate session duration, defaulting to 1 hour if no end_time is set
        if not machine.end_time:
            machine.end_time = machine.start_time + datetime.timedelta(hours=hours)

        # Start a background thread to monitor the session
        def monitor_session():
            now = datetime.datetime.now()
            time_to_wait = (machine.end_time - now).total_seconds()
            if time_to_wait > 0:
                time.sleep(time_to_wait)

            # End the session and notify the user
            self.end_session(machine, user)
            self.notify_user(machine, user)

        thread = threading.Thread(target=monitor_session, daemon=True)
        thread.start()

        return True


        
    def end_session(self, machine, user):
        """
        Ends the session for a machine, sets it back to 'Available', and clears user association.
        """
        if not isinstance(machine, Machine) or not isinstance(user, User):
            raise TypeError("Invalid machine or user type")

        if machine.current_state != 'In Use':
            raise ValueError(f"Machine {machine.machine_type} is not currently in use")

        if machine.who_is_using != user.user_name:
            raise PermissionError(f"User {user.user_name} is not authorized to end this session")

        # Update machine state to 'Available'
        machine.update_state(value=('Available', user))
        return True


    def set_out_of_order(self, machine_id, status, user):
        """
        Sets the status of the machine to/from out of order
        """
        machine = self.Machines[machine_id]
        if type(machine) != Machine or type(user) != User:
            raise TypeError()

        if not user.is_admin:
            raise PermissionError()

        machine.update_state(value=(status, user))
        return True

    def get_status(self, machine_id):
        """
        Returns the current status of the machine
        """
        machine = self.Machines[machine_id]
        if type(machine) != Machine:
            raise TypeError()

        return machine._current_state
    
    def notify_user(self, machine_id, user):
        """
        Notifies the user of the machine's completion
        """
        machine = self.Machines[machine_id]
        if type(machine) != Machine or type(user) != User:
            raise TypeError()

        Notification_Manager.send_user_notification(Notification_Manager(), user, machine)
        return True
        
    # def log_event(self, machine, user):
    #     """
    #     Logs the user's interaction with the machine
    #     """
    #     if type(machine) != Machine or type(user) != User:
    #         raise TypeError()
    #     return True
