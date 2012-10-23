'''
Created on Jul 13, 2012

@author: trungtle
'''
import 	os
import 	sys
import 	logging

from EngineCore import CONFIG

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

class Logger(object):

    def __init__(self):
        self.DEBUG = CONFIG["diags"]["enable"]


    def Enable(self, isEnable):
        if isEnable:
            self.DEBUG = True
        else:
            self.DEBUG = False


    def IsEnable(self):
    	return self.DEBUG


    def Print(self, msg):
        if(self.DEBUG):
            logging.debug(msg)

# Global object
g_logger = Logger()
