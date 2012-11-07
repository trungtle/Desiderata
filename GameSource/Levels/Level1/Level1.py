'''
Created on Jul 13, 2012

@author: trungtle
'''
import json
import pygame
from   pygame.locals import *
import numpy

import Diags.BLogger        as ns_logger
import Graphics.BDraw       as ns_draw
import Simulators.BSimulator as ns_sim
import Utility.util         as ns_util


import MVC.BController      as ns_controller
import MVC.BView            as ns_view
import MVC.BModelManager    as ns_model_manager

from   GameSource import SOUND_DIR
from   GameSource import CONFIG

class Level(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.levelup = 0

        
    def Initialize(self):
    
        self.spinner            = ns_controller.LevelSpinnerController()
        self.modelManager       = ns_model_manager.ModelManager()
        self.keyboardController = ns_controller.KeyboardController()
        self.view               = ns_view.BView(self.modelManager)
        self.sim                = ns_sim.Simulator(self.modelManager)

        # Allow mutiple key down events
        pygame.key.set_repeat(500, 10)

    
    def LoadModels(self):
        s = ns_util.GetModel("label", "p")
        self.modelManager.Add(s, "p")

        s = ns_util.GetModel("label", "b")
        self.modelManager.Add(s, "b")

        s = ns_util.GetModel("label", "h")
        self.modelManager.Add(s, "h")

        inputbox = ns_util.GetModel("inputbox", "level1")
        self.modelManager.Add(inputbox, "ib")
    

    def LoadResources(self):
        pygame.mixer.music.load(SOUND_DIR + CONFIG["music"]["background"])
    

    def LevelUp(self):
        '''
        Return the number of next level. If self.levelup is 0, there is no next
        level and the game goes to evEnd.
        '''
        return self.levelup                        