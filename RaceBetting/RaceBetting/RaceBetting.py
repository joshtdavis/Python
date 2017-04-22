import random
from Athletes import Athletes
from BettingAgent import BettingAgent
racers = []
agents = []
finalResults = -1
def __laneTaken(laneNum,Lanes):
	for lane in Lanes:
		if(laneNum == lane):
			return True
	return False
def __initialize():
	names = ["Dimitri","Ludwig","Harrison","Bolt","John","Tyson","Eren","Levi"]
	percentSum = 0
	lanes = []
	for i in range(8):
		if(percentSum<100):
			winPercent = random.randint(0,75)
			percentSum += winPercent
			if(percentSum>=100):
				winPercent = winPercent - (percentSum - 100)
		laneNum = random.randint(0,8)
		while(__laneTaken(laneNum,lanes)):
			laneNum = random.randint(0,8)
		lanes.append(laneNum)
		racers.append(Athletes(i,names[i],winPercent,laneNum,random.randint(3,10)))

def __placeBets():
	# each loop simulates one minute where a bet might be placed
	names = ["Jack","Alex","Adam","Clark","John","Chris","Jessica","Sydney","Linda","Jordan","Matt","Thomas","Luke","Joe"]
	for i in range(60): 
		if(random.randint(0,4)==2): # 25% chance a bet will be place each minute
			agent = BettingAgent(i,names[random.randint(0,len(names)-1)])
			agent.determineBet(racers);
			agents.append(agent)
def __runRace():
	runners = []
	for racer in racers:
		#print(racer.toString())
		runners.append( [racer,0] )
	for i in range(40): # each loop simulates 10 seconds
		places = []
		for runner in runners:
			if(1==random.randint(0,200)): # 5% chance for injury to every athlete
				print(runner[0].get_name() + " has been injured and removed from the race.")
				runners.remove(runner)
			runner[1] = int(runner[0].get_winPercent() *.1)
			variableSpeed = random.randint(0,2)
			if(variableSpeed==0):
				runner[1] += (runner[0].get_speed()-.5 * 10)
			elif(variableSpeed==1):
				runner[1] += (runner[0].get_speed()+.5 * 10)
			else:
				runner[1] += (runner[0].get_speed() * 10)
			places.append(runner)
		places = sorted(places,key=lambda place: place[1])
	return places
def __afterMath(finalResults):
	print("The results are in ")
	place = 1
	moneyLost = 0
	moneyWon = 0
	for result in finalResults:
		print(str(place) + " " + result[0].get_name())
		place+=1
	for agent in agents:
			if(agent.get_betRacer() == finalResults[0][0].get_id()):
				#print(str(agent.get_betRacer()) + " " + str(finalResults[0][0].get_id()) +" $" + str(agent.get_betValue()))
				moneyLost += agent.get_betValue()
			else:
				moneyWon += agent.get_betValue()
	for agent in agents:
		for racer in racers:
			if(agent.get_betRacer() == racer.get_id()):
				Athelete = racer
	print("The race org lost " + str(moneyLost) + " dollars and made " + str(moneyWon) + " for a net value of " + str(moneyWon-moneyLost))
def Main():
	# code goes here for main program
	__initialize()
	__placeBets()
	finalResults = __runRace()
	__afterMath(finalResults)
if(__name__ == "__main__"):
	Main()