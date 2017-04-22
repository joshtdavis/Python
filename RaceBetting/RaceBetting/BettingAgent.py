import Athletes
import random
class BettingAgent(object):
	"""description of class"""
	__id = -1
	__name = ""
	__betValue = 0
	__betRacer = -1

	def __init__(self):
		return None
	def __init__(self,id,name):
		self.__id = id
		self.__name = name

	def set_name(self,name):
		self.__name = name
	def get_name(self):
		return self.__name

	def set_betValue(self,betVal):
		self.__betValue = betVal
	def get_betValue(self):
		return self.__betValue

	def set_betRacer(self,betRacer):
		self.__betRacer = betRacer
	def get_betRacer(self):
		return self.__betRacer

	def determineBet(self,racers): # betting agents don't know the speed of the athlete
		heuristics = []
		largestHeuristic = 0;
		preferedRacer = racers[0]
		for racer in racers:
			heuristic = 0
			heuristic += round(float(racer.get_winPercent()) * .1)
			if(racer.get_lane()<6 and racer.get_lane() >2):
				heuristic += 2
			heuristic += random.randint(0,7) # personal bias
			#print(self.get_name() + " has heuristic of "+ str(heuristic) + " for " + racer.get_name() + " : "+ racers[0].get_name())
			heuristics.append(heuristic)
			#print(str(largestHeuristic) + " " + str(heuristic))
			if(largestHeuristic<heuristic):
				largestHeuristic = heuristic
				preferedRacer = racer
		heuristics.sort();
		self.set_betRacer(preferedRacer.get_id())
		self.set_betValue(random.randint(20,500) * (heuristics[len(heuristics)-1] - heuristics[len(heuristics)-2] +1))
		print(self.get_name() + " has made a bet on " + preferedRacer.get_name() + " of value "+ str(self.get_betValue()))