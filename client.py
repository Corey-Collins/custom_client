from threading import Thread
import time

class Listener(object):

	performer = None

	def __init__(self, performer_instance):
		performer = performer_instance
		self.checkInput()		

	def checkInput(self):
		while True:
			user_input = raw_input("Enter Something: ")
			if(user_input == 'exit'):
				break
			else:
				performer.addAction(user_input)


class Performer(object):

	actions = ['']

	def addAction(self, action):
		self.actions.append(action)

	def listActions(self):
		for i in self.actions:
			print i


#runs on thread
def startListener(performer_instance):
	Listener(performer_instance)

#runs on main
performer = Performer()
thread = Thread(target=startListener, args=(performer,))
thread.start()
thread.join()
performer.listActions()