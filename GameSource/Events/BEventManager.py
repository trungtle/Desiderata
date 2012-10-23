'''
Created on Aug 19, 2012

@author: tle
'''
import Diags.BLogger as ns_logger
from Events.BEvent   import *

logger = ns_logger.g_logger

class EventManager(object):
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()
               
    def RegisterListener(self, listener):
        self.listeners[listener] = 1
        
    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]
            
    def Post(self, event):
        if event.log:
                logger.Print(event.name)
                
        for listener in self.listeners.keys():
            listener.Notify(event)
            
# Global object            
g_evManager = EventManager()
        