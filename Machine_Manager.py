import Machine
import User

class Machine_Manager:
	"""
	Class that manages the machines and their status
	"""
 
	def create_session(self, machine, user):
		"""
		Sets the status for a machine to 'In Use' and associates the user with the machine

		Args:
			machine (Machine): machine the user is using
			user (User): specific user using the machine

		Raises:
			TypeError: if the parameters are not of type Machine or User

		Returns:
			None: if the machine is successfully set to 'In Use'
		"""
		if type(machine) != Machine or type(user) != User:
			raise TypeError()
		
		return machine.set_current_state('In Use', user)
		
	def end_session(self, machine, user):
		"""
		Sets the status for a machine to 'Available' and removes the user from the machine

		Args:
			machine (Machine): machine the user is using
			user (User): user using the machine

		Raises:
			TypeError: if the parameters are not of type Machine or User

		Returns:
			None: if the machine is successfully set to 'Available'
		"""
		if type(machine) != Machine or type(user) != User:
			raise TypeError()

		return machine.set_current_state('Available', user)
		
	def set_out_of_order(self, machine, status, user):
		"""
		Sets the status of the machine to/from out of order

		Args:
			machine (Machine): machine to have its status changed
			status (str): new status of the machine
			user (User): user setting the status of the machine
   
		Raises:
			TypeError: if the parameters are not of type Machine or User
			ValueError: if the user is not an admin
		"""
		if type(machine) != Machine or type(user) != User:
			raise TypeError()

		if not user.get_is_admin():
			raise ValueError()

		return machine.set_current_state(status, user)

	def getStatus(self, machine):
		"""
		Returns the current status of the machine

		Args:
			machine (Machine): machine to get the status of

		Returns:
			str: the current status of the machine

		Raises:
			TypeError: if the parameter is not of type Machine
		"""
		if type(machine) != Machine:
			raise TypeError()

		return machine.get_current_state()
	
	def notifyUser(self, machine, user):
		"""
		Notifies the user of the machine's completion

		Args:
			machine (Machine): machine to notify the user of
			user (User): user to notify

		Raises:
			TypeError: if the parameters are not of type Machine or User
		"""
		if type(machine) != Machine or type(user) != User:
			raise TypeError()

		# utilize notification manager to notify the user with their preferred method of communication
		return True
		
	def logEvent(self, machine, user):
		"""
		Logs the user's interaction with the machine

		Args:
			machine (Machine): machine to log the event of
			user (User): user to log

		Raises:
			TypeError: if the parameters are not of type Machine or User
		"""
		if type(machine) != Machine or type(user) != User:
			raise TypeError()

		# utilize logging service to log the event
		return True