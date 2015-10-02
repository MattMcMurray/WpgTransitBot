from time_adjust import get_wpg_time
import os
import shutil

def printlog(msg):
	print msg
	time, extratime= get_wpg_time()
	out = '[{0}] : {1}\n'.format(time, msg)

	filepath = getlogdir()
	filepath += 'print.log'
	file = open(filepath, 'a')

	file.write(out)

	file.close()

def getlogdir():
	dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	dirname+='/logs/'

	if not os.path.exists(dirname):
		os.makedirs(dirname)

	return dirname

def clearlogs():
	shutil.rmtree(getlogdir())