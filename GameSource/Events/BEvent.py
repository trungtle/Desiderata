'''
Created on Aug 24, 2012

@author: tle
'''

class Event(object):
    def __init__(self):
        self.name = "Default Event"
        self.log = False
       
        
# ------------------------------------------------------------------------------
# Game State Events
# ------------------------------------------------------------------------------
class evTick(Event):
    def __init__(self):
        self.name = "Tick Event"
        self.log = False

class evEnd(Event):
    def __init__(self):
        self.name = "End Game Event"
        self.log = False

class evQuit(Event):
    def __init__(self):
        self.name = "Quit Event"
        self.log = False 

# ------------------------------------------------------------------------------
# Display Events
# ------------------------------------------------------------------------------
class evFlipScreen(Event):
    def __init__(self):
        self.name = "Flip Screen Event"
        self.log = False

class evScreenCleared(Event):
    def __init__(self):
        self.name = "Screen Cleared Event"
        self.log = False

class evModelDrawn(Event):
    def __init__(self):
        self.name = "Model Drawn Event"
        self.log = False

# ------------------------------------------------------------------------------
# Input Events
# ------------------------------------------------------------------------------
class evKeyDown(Event):
    def __init__(self, key, unic):
        self.name = "Key Down"
        self.key = key
        self.unicode = unic
        self.log = False

class evKeyUp(Event):
    def __init__(self, key):
        self.name = "Key Up"
        self.key = key
        self.log = False

class evEnter(Event):
    def __init__(self):
        self.name = "Enter Event"
        self.log = False

class evMouseMove(Event):
    def __init__(self, mouse_pos):
        self.name = "Mouse Move Event"
        self.log = False
        self.mouse_pos = mouse_pos
                
class evLMouseDown(Event):
    def __init__(self, mouse_pos):
        self.name = "Left Mouse Down Event"
        self.log = False

class evRMouseDown(Event):
    def __init__(self, mouse_pos):
        self.name = "Right Mouse Down Event"
        self.log = False
              
# ------------------------------------------------------------------------------
# In-game Events
# ------------------------------------------------------------------------------
class evAdvance(Event):
    def __init__(self):
        self.name = "Advance Event"
        self.log = False

