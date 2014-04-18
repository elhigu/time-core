## -*- coding: utf-8 -*-

# TODO: packaging to namespace

class AvailabilityBase(object):
	def __init__(self, negative=False):
		"""Base Availability

		@param negative If True then time declaration will 
		    explicitly not be available.
		"""
		self.negative = negative

	def isAvailable(self, dt):
		assert("Not implemented")
		return None;

class Availability(AvailabilityBase):
	"""List of availabilities and exceptions.
	"""
	pass

class Always(AvailabilityBase):
	def isAvailable(self, dt):
		return True;

class OnDatetime(AvailabilityBase):
	def isAvailable(self, dt):
		return 

class Weekly(AvailabilityBase):
	pass

class Monthly(AvailabilityBase):
	pass
