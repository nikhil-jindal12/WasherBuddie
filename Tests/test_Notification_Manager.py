import unittest
from unittest.mock import MagicMock, patch
from Notification_Manager import Notification_Manager
from User import User
from Machine import Machine
import Notification_Sender

class TestNotificationManager(unittest.TestCase):

    def setUp(self):
        self.manager = Notification_Manager()
        self.admin_user = User()
        self.non_admin_user = User()
        self.user1 = User()
        self.user2 = User()
        self.machine = Machine()

        # Mock admin user
        self.admin_user.get_is_admin = MagicMock(return_value=True)
        self.admin_user.get_notification_preference = MagicMock(return_value='Email')

        # Mock non-admin user
        self.non_admin_user.get_is_admin = MagicMock(return_value=False)
        self.non_admin_user.get_notification_preference = MagicMock(return_value='Text')

        # Mock users
        self.user1.get_notification_preference = MagicMock(return_value='Text')
        self.user2.get_notification_preference = MagicMock(return_value='Email')

    def test_send_notification_success(self):
        users = [self.user1, self.user2]
        message = "Your laundry is ready!"

        with patch('Notification_Sender.send_custom_message') as mock_send:
            self.manager.send_notification(users, self.admin_user, message)
            mock_send.assert_any_call(self.admin_user, self.user1, message)
            mock_send.assert_any_call(self.admin_user, self.user2, message)

    def test_send_notification_type_error_sender(self):
        with self.assertRaises(TypeError):
            self.manager.send_notification([self.user1], "NotAUser", "Message")

    def test_send_notification_type_error_message(self):
        with self.assertRaises(TypeError):
            self.manager.send_notification([self.user1], self.admin_user, 123)

    def test_send_notification_permission_error(self):
        with self.assertRaises(PermissionError):
            self.manager.send_notification([self.user1], self.non_admin_user, "Message")

    def test_send_user_notification_success_text(self):
        self.user1.get_notification_preference = MagicMock(return_value='Text')

        with patch('Notification_Sender.send_text_notification') as mock_send:
            self.manager.send_user_notification(self.user1, self.machine)
            mock_send.assert_called_once_with(self.user1, self.machine)

    def test_send_user_notification_success_email(self):
        self.user1.get_notification_preference = MagicMock(return_value='Email')

        with patch('Notification_Sender.send_email_notification') as mock_send:
            self.manager.send_user_notification(self.user1, self.machine)
            mock_send.assert_called_once_with(self.user1, self.machine)

    def test_send_user_notification_type_error_user(self):
        with self.assertRaises(TypeError):
            self.manager.send_user_notification("NotAUser", self.machine)

    def test_send_user_notification_type_error_machine(self):
        with self.assertRaises(TypeError):
            self.manager.send_user_notification(self.user1, "NotAMachine")

    def test_send_follow_up_notification_success_text(self):
        self.user1.get_notification_preference = MagicMock(return_value='Text')

        with patch('Notification_Sender.send_follow_up_text_notification') as mock_send:
            self.manager.send_follow_up_notification(self.user1, self.machine)
            mock_send.assert_called_once_with(self.user1, self.machine)

    def test_send_follow_up_notification_success_email(self):
        self.user1.get_notification_preference = MagicMock(return_value='Email')

        with patch('Notification_Sender.send_follow_up_email_notification') as mock_send:
            self.manager.send_follow_up_notification(self.user1, self.machine)
            mock_send.assert_called_once_with(self.user1, self.machine)

    def test_send_follow_up_notification_type_error_user(self):
        with self.assertRaises(TypeError):
            self.manager.send_follow_up_notification("NotAUser", self.machine)

    def test_send_follow_up_notification_type_error_machine(self):
        with self.assertRaises(TypeError):
            self.manager.send_follow_up_notification(self.user1, "NotAMachine")

    def test_send_ping_success(self):
        message = "Hello!"

        with patch('Notification_Sender.send_custom_message') as mock_send:
            self.manager.send_ping(self.admin_user, self.user1, message)
            mock_send.assert_called_once_with(self.admin_user, self.user1, message)

    def test_send_ping_type_error_sending_user(self):
        with self.assertRaises(TypeError):
            self.manager.send_ping("NotAUser", self.user1, "Message")

    def test_send_ping_type_error_receiving_user(self):
        with self.assertRaises(TypeError):
            self.manager.send_ping(self.admin_user, "NotAUser", "Message")

    def test_send_ping_type_error_message(self):
        with self.assertRaises(TypeError):
            self.manager.send_ping(self.admin_user, self.user1, 123)

if __name__ == '__main__':
    unittest.main()
