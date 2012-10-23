'''
Created on Jul 13, 2012

@author: trungtle
'''
import json
import pygame
from   pygame.locals import *

import Diags.BLogger        as ns_logger
import Graphics.BDraw       as ns_draw

import MVC.BController      as ns_controller
import MVC.BView            as ns_view
import MVC.BModelManager    as ns_model_manager

import Simulators.BSimulator as ns_sim


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
    
        self.spinner = ns_controller.LevelSpinnerController()
        self.keyboardController = ns_controller.KeyboardController()
        self.modelManager = ns_model_manager.ModelManager()
        self.view = ns_view.BView()

        # Allow mutiple key down events
        pygame.key.set_repeat(1, 10)

    
    def LoadResources(self):
        pass
    
        
    def LoadModels(self):
        pass        
    

    def LevelUp(self):
        '''
        Return the number of next level. If self.levelup is 0, there is no next
        level and the game goes to evEnd.
        '''
        return self.levelup
    
    
    def Run(self):
        pass
    
                        