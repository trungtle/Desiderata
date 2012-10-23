'''
Created on Jul 13, 2012

@author: trungtle
'''

import pygame

from    Events.BEventManager import *
from    Graphics.BColors     import *
import  Graphics.BDraw       as ns_draw

from EngineCore import CONFIG


class BView(object):
    '''
    MVC View
    '''
    def __init__(self, modelManager):
        
        g_evManager.RegisterListener(self)

        self.modelManager       = modelManager
        
        # Window
        self.screenSize = CONFIG["view"]["size"]
        if CONFIG["view"]["fullscreen"]:
            self.screen = pygame.display.set_mode(self.screenSize, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.screenSize)

        self.screenRect = self.screen.get_rect()
        pygame.display.set_caption(CONFIG["view"]["caption"])
        
        pygame.init()
        
                
    def Notify(self, event):
        if isinstance(event, evTick):
            self.models_to_draw     = self.modelManager.Size()
            ns_draw.Draw(self.screen)
            g_evManager.Post(evScreenCleared())

        elif isinstance(event, evModelDrawn):
            self.models_to_draw -= 1
            if(self.models_to_draw == 0):
                g_evManager.Post(evFlipScreen())

        elif isinstance(event, evFlipScreen):
            pygame.display.flip()            

        elif isinstance(event, evQuit):
            pass
    