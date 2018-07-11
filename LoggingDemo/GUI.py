from LoggingDemo.CustomLogger import *

class MyFancyGui(object):
	def __init__(self):
		self.logger = logging.getLogger(__name__)
		self.logger.info("Initializing MyFancyGui class!")

	def doSomething(self):
		self.logger.debug("I'm doing something!")

		self.logger.critical("Oh no not anymore!")
