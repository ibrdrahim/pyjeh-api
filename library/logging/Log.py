import logging
import logging.handlers

def logger(msg,log_type = ''):
	LOG_FILE = 'log/sysLogging.log'

	#create logger
	logger = logging.getLogger('ServiceApi')
	logger.setLevel(logging.DEBUG)

	# create file handler which logs even debug messages
	fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=10*1024*1024, backupCount=5)
	fh.setLevel(logging.DEBUG)

	# create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.ERROR)

	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
	ch.setFormatter(formatter)
	fh.setFormatter(formatter)

	# add the handlers to logger
	logger.addHandler(ch)
	logger.addHandler(fh)	

	if log_type == "DEBUG":
		logger.debug(msg)
	else:
		logger.error(msg)

# Logger("tes fuad","DbFunction")