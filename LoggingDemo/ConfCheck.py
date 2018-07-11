from LoggingDemo.CustomLogger import *

class Checker(object):
	def __init__(self):
		self.logger = logging.getLogger(__name__)
		self.logger.debug("Initializing Checker class!")

	def doSomething(self):
		self.logger.debug("I'm doing something!")

		self.logger.error("Oh no not anymore!")
