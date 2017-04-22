class Athletes(object):
	"""description of class"""
	__name = ""
	__winPercent = 0
	__lane = -1
	__speed = 0 # meters per second
	__id = -1
	def __init__(self):
		return None
	def __init__(self,id,name,winPercent,laneNum,speed):
		self.__name = name
		self.__id = id
		self.__winPercent = winPercent
		self.__lane = laneNum
		self.__speed = speed

	def set_name(self,name):
		self.__name = name
	def get_name(self):
		return self.__name

	def set_winPercent(self,winPercent):
		self.__winPercent = winPercent
	def get_winPercent(self):
		return self.__winPercent

	def set_lane(self,lane):
		self.__lane = lane
	def get_lane(self):
		return self.__lane

	def set_id(self,id):
		self.__id = id
	def get_id(self):
		return self.__id

	def set_speed(self,speed):
		self.__speed = speed
	def get_speed(self):
		return self.__speed
	def toString(self):
		return (self.get_name() + " has lane " + str(self.get_lane()) + " and a win chance of " + str(self.get_winPercent()) )