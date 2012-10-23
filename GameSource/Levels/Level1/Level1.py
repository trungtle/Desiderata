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
        s = ns_util.GetModel("label", "s")
        self.modelManager.Add(s)

        inputbox = ns_util.GetModel("inputbox", "level1")
        self.modelManager.Add(inputbox)
    

    def LoadResources(self):
        pass
    

    def LevelUp(self):
        '''
        Return the number of next level. If self.levelup is 0, there is no next
        level and the game goes to evEnd.
        '''
        return self.levelup                        