import logging
import logging.config
import os

logging.config.fileConfig(os.sep.join([os.path.dirname(__file__),"LoggingConfig","LoggingConfig.ini"]),defaults={'logfilename':os.sep.join([os.path.dirname(__file__),"Logs","LoggingDemo.log"])})