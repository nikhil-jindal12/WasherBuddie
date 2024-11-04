import smtplib
from email.mime.text import MIMEText
import User
import Notification
import Machine

class Notification_Sender:
	
	_mobile_carriers = 	{'AT&T': '@mms.att.net',
	 					'Verizon': '@vzwpix.com', 
						'Boost Mobile': '@myboostmobile.com', 
					 	'Cricket': '@mms.mycricket.com', 
					  	'MetroPCS': '@mymetropcs.com',
					   	'Sprint': '@pm.sprint.com',
						'T-Mobile': '@tmomail.net',
						'U.S. Cellular': '@mms.uscc.net',
						}
	
	@property
	def get_mobile_carriers(self):
		"""
		Returns a list of mobile carriers and their gateway addresses

		Returns:
			dict: list of mobile carriers and their gateway addresses
		"""
		return self._mobile_carriers


	def	send_text_notification(self, user, machine):
		"""
		Sends a text notification to the user's phone number

		Args:
			user (User): user using the machine
			machine (Machine): machine being used

		Raises:
			TypeError: if the parameters are not the correct types
		"""	
		if type(user) != User or type(machine) != Machine:
			raise TypeError()

		msg = MIMEText(Notification.get_text_notification(user, machine.get_machine_type()))
		msg['Subject'] = 'WasherBuddie - Your Laundry Cycle Has Finished'
		msg['From'] = 'WasherBuddie'
		msg['To'] = user.get_phone_number() + self.get_mobile_carriers()[user.get_phone_carrier()]

		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.starttls()
			smtp.login("washerbuddie@gmail.com", "zqsp ieqt qils etkr")
			smtp.send_message(msg)
			smtp.quit()
   
	def send_email_notification(self, user, machine):
		"""
		Sends an email notification to the user's email address

		Args:
			user (User): user using the machine
			machine (Machine): machine being used

		Raises:
			TypeError: if the parameters are not the correct types
		"""	
		if type(user) != User or type(machine) != Machine:
			raise TypeError()

		msg = MIMEText(Notification.get_email_notification(user.get_user_name(), machine.get_machine_type()))
		msg['Subject'] = 'WasherBuddie - Your Laundry Cycle Has Finished'
		msg['From'] = 'WasherBuddie'
		msg['To'] = user.get_user_email()

		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.starttls()
			smtp.login("washerbuddie@gmail.com", "zqsp ieqt qils etkr")
			smtp.send_message(msg)
			smtp.quit()
  
	def send_follow_up_text_notification(self, user, machine):
		"""
		Sends a follow-up text notification to the user's phone number

		Args:
			user (User): user using machine
			machine (Machine): machine being used

		Raises:
			TypeError: if the parameters are not the correct types
		"""	
		if type(user) != User or type(machine) != Machine:
			raise TypeError()

		msg = MIMEText(Notification.get_follow_up_text_notification(machine.get_machine_type()))
		msg['Subject'] = 'WasherBuddie - Your Laundry Cycle Has Been Stagnant'
		msg['From'] = 'WasherBuddie'
		msg['To'] = user.get_phone_number() + self.get_mobile_carriers()[user.get_phone_carrier()]
  
		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.starttls()
			smtp.login("washerbuddie@gmail.com", "zqsp ieqt qils etkr")
			smtp.send_message(msg)
			smtp.quit()
   
	def send_follow_up_email_notification(self, user, machine):
		"""
		Sends a follow-up email notification to the user's email address

		Args:
			user (User): user using machine
			machine (Machine): machine being used

		Raises:
			TypeError: if the parameters are not the correct types
		"""
		if type(user) != User or type(machine) != Machine:
			raise TypeError()

		msg = MIMEText(Notification.get_follow_up_email_notification(user.get_user_name(), machine.get_machine_type()))
		msg['Subject'] = 'WasherBuddie - Your Laundry Cycle Has Been Stagnant'
		msg['From'] = 'WasherBuddie'
		msg['To'] = user.get_user_email()

		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.starttls()
			smtp.login("washerbuddie@gmail.com", "zqsp ieqt qils etkr")
			smtp.send_message(msg)
			smtp.quit()
   
	@property
	def send_custom_message(self, sending_user, receiving_user, message):
		"""
		Sends a custom message to the receiving user using their preferred method of communication from another user

		Args:
			sending_user (User): user sending a message
			receiving_user (User): user using machine and receiving the message
			message (str): message contents

		Raises:
			TypeError: if the parameters are not the correct types
		"""
		if type(sending_user) != User or type(receiving_user) != User:
			raise TypeError()

		if receiving_user.get_notification_preference() == 'Text':
			message = MIMEText(message)
			message['Subject'] = 'WasherBuddie - Message from ' + sending_user.get_user_name()
			message['From'] = sending_user.get_user_name()
			message['To'] = receiving_user.get_phone_number() + self.get_mobile_carriers()[receiving_user.get_phone_carrier()]
		elif receiving_user.get_notification_preference() == 'Email':
			msg = MIMEText(message)
			msg['Subject'] = 'WasherBuddie - Message from ' + sending_user.get_user_name()
			msg['From'] = sending_user.get_user_name()
			msg['To'] = receiving_user.get_user_email()

		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.starttls()
			smtp.login("washerbuddie@gmail.com", "zqsp ieqt qils etkr")
			smtp.send_message(msg)
			smtp.quit()
		