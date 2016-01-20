import subprocess

class HydroControl(object):
	_instance = None    def __new__(cls):
    	if cls._instance is None:
    		cls._instance = object.__new__(cls)
    	return cls._instance
    	
    def startMain(self):
	    self.MAINPATH = '/home/pi/hydroponics/main.py'
        cmd = 'sudo -E python3 %s' % (self.MAINPATH)
        self.p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def stopMain(self):
        self.p.kill()
        self.p = None

    def showPID(self):
        print(self.p.pid)
