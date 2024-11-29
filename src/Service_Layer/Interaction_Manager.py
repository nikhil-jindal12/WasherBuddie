from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import threading
import datetime
import time
import traceback

if TYPE_CHECKING:
    from mongoDB.CRUD_api import Database_Manager
    from src.Service_Layer.Machine import Machine
    from src.Service_Layer.User import User
    from src.Service_Layer.Notification_Manager import Notification_Manager

class Interaction_Manager:
    machine_count = 0
    def add_washer(self, machine_id: int) -> bool:
        """
        Adds a new washing machine
        
        Args:
            machine_id (int): machine id of the new washer

        Returns:
            boolean: whether or not the washer was added successfully
        """
        try:
            washer = Machine('Washer', self.machine_count)
            machine_count+=1
            return Database_Manager().insert_washer(washer)
        except:
            return False

    def add_dryer(self, machine_id: int) -> bool:
        """
        Adds a new drying machine
        
        Args:
            machine_id (int): machine id of the new dryer

        Returns:
            boolean: whether or not the dryer was added successfully
        """
        try:
            dryer = Machine('Dryer', self.machine_count)
            machine_count+=1
            return Database_Manager().insert_dryer(dryer)
        except:
            return False

    def send_notification(self, sending_user: User, receiving_user: User, message: str):
        """
        Sends a notification to another user from the current user

        Args:
            sending_user (User): user sending a message
            receiving_user (User): user receiving the message
            message (str): message being sent
        """
        Notification_Manager.send_ping(sending_user, receiving_user, message)

    def add_user(self, user_name: str, notification_preference: str, user_phone_number: int, user_email: str, phone_carrier: str, is_admin:Optional[bool]=False, password:Optional[str]='defaultpassword123') -> bool:
        """
        Adds a user to the database

        Args:
            user_name (str): user's name
            notification_preference (str): user's notification preferences
            user_phone_number (int): user's 10-digit phone number
            user_email (str): user's valid email
            phone_carrier (str): user's phone carrier
            is_admin (bool, optional): whether the user is an admin of the program. Defaults to False.
            password (str, optional): user's password. Defaults to 'defaultpassword123'.

        Returns:
            _type_: _description_
        """
        try:
            #need to check if the user already exists first
            return Database_Manager().insert_single_user(User(user_name, user_email, phone_carrier, notification_preference, user_phone_number, is_admin, password))
        except:
            return False

    def remove_user(self, user_name: str) -> bool:
        """
        Removes a user from the database

        Args:
            user_name (str): user's namee to be deleted from whitelist

        Returns:
            boolean: True if the user was removed successfully, False otherwise
        """
        try:
            return Database_Manager().delete_single_user(user_name)
        except:
            return False

    def authenticate_log_in(self, email_address: str, password: str) -> bool:
        """
        Authenticates a user's log in using their email and password

        Args:
            email_address (str): user's email address
            password (str): user's password input

        Returns:
            boolean: True if the user is authenticated, False otherwise
        """
        try:
            return Database_Manager().validate_user(email_address, password)
        except:
            return False

    def get_white_list(self):
        """
        Returns a list of all valid users

        Returns:
            list: list of all valid users as Users, False otherwise
        """
        try:
            return Database_Manager().get_valid_users()
        except:
            return False
        
#below needs to be integrated into the class, may keep local vars, my go into the db, then get rid of machine manager      
    
    def create_session(self, machine: Machine, user: User, hours, minutes) -> bool:
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
            machine.end_time = machine.start_time + datetime.timedelta(hours=hours, minutes=minutes)

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


            
    def end_session(self, machine: Machine, user: User) -> bool:
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


        def set_out_of_order(self, machine_id, user):
            """
            Sets the status of the machine to/from out of order
            """
            machine = self.Machines[machine_id]
            if type(machine) != Machine or type(user) != User:
                raise TypeError()

            if not user.is_admin:
                raise PermissionError()

            machine.update_state(value=("Out of Order", user))
            return True

        def get_status(self, machine_id):
            """
            Returns the current status of the machine
            """
            machine = self.Machines[machine_id]
            if type(machine) != Machine:
                raise TypeError()

            return machine._current_state
        
        def notify_user(self, machine, user):
            """
            Notifies the user of the machine's completion
            """
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
        