import Machine
import User

class Interaction_Manager:
    def add_washer(self, machine_type='Washer'):
        try:
            Machine(machine_type)
            return True
        except:
            return False

    def add_dryer(self, machine_type='Dryer'):
        try:
            Machine(machine_type)
            return True
        except:
            return False

    def send_notification(self):
        return False

    def add_user(self, user_name, notification_preference, user_phone_number, user_email, is_admin=False):
        try:
            User(user_name, notification_preference, user_phone_number, user_email, is_admin)
            # put an addition request into CRUD
            # will add line in DB with user
            return True
        except:
            return False

    def remove_user(self, user_name):
        try:
            # put a delete request into CRUD
            # will search up in DB and delete that line
            return True
        except:
            return False

    def authenticate_log_in(self):
        return False

    def get_white_list(self):
        return False

    def log_event(self):
        return False
