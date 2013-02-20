'''
Created on Jul 13, 2012

@author: trungtle
'''
import random
import pygame
import numpy
import re

import  Diags.BLogger
from    Events.BEventManager import *
import  Utility.util         as ns_util

from GameSource import CONFIG


class Simulator(object):
    
    def __init__(self, modelManager):
        g_evManager.RegisterListener(self)
        self.modelManager   = modelManager
        self.circ_count = 0
        self.circleCenters = [(0,0)]

        self.circle_radius = 0


    def Init(self):
        #
        # Play background music
        #

        if CONFIG["music"]["on"]:
            pygame.mixer.music.play(-1)

    def isNewCircleOverlapValid(self, pos):
        # for center in self.circles:
        # if(self.radius > numpy.linalg) 
        print "Distance: "
        for cpos in self.circleCenters:
            a = numpy.array(pos)
            b = numpy.array(cpos)
            if(numpy.linalg.norm(a-b) < self.circle_radius):
                return False

        return True

    def addCircle(self, pos):
        
        if(self.isNewCircleOverlapValid(pos)):
            s = ns_util.GetModel("Circle","regular")
            s["json"]["pos"] = pos
            self.modelManager.Add(s,"circle" + str(self.circ_count))
            self.circ_count += 1
            self.circleCenters.append(pos)
            self.circle_radius = s["json"]["radius"]
            g_evManager.Post(evDrawCircle(pos))


    def Notify(self, event):
        if isinstance(event, evEnter):
            if self.ready:
                # Initialize
                self.Init()
                g_evManager.UnregisterListener(self)
        elif isinstance(event, evLMouseDown):
          self.addCircle(event.mouse_pos)


