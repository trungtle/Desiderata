'''
Created on Jul 13, 2012

@author: trungtle
'''
import random
import pygame
import re

import  Diags.BLogger
from    Events.BEventManager import *
import  Utility.util         as ns_util

from GameSource import CONFIG


class Simulator(object):
    
    def __init__(self, modelManager):
        g_evManager.RegisterListener(self)
        self.modelManager   = modelManager

    def Init(self):
        #
        # Play background music
        #

        if CONFIG["music"]["on"]:
            pygame.mixer.music.play(-1)



    def Notify(self, event):
        if isinstance(event, evEnter):
            if self.ready:
                # Initialize
                self.Init()
                g_evManager.UnregisterListener(self)


