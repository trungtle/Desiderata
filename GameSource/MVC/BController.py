'''
Created on Jul 19, 2012

@author: tle
'''

import pygame

from Events.BEventManager import *


class LevelSpinnerController(object):
    '''
    @description:

        Controller that generate tick events for other classes to use. 
        There are 2 types of states: 'run' and 'pause'.

        'run': True ticks the level, False breaks the main control loop.
        'pause'; True stops ticking events, but does not break the main control loop.
    '''


    def __init__(self):
        g_evManager.RegisterListener(self)

        self.states = { \
            'run'   : False,
            'pause' : False
        }

        # Clock to manage how fast the screen updates
        self.clock = pygame.time.Clock()


    def Run(self):
        self.states['run']  = True

        while self.states['run']:

            if not self.states['pause']:
                self.clock.tick(60)
                g_evManager.Post(evTick())


    def Notify(self, event):
        if isinstance(event, evQuit):
            self.states['run'] = False


class KeyboardController():


    def __init__(self):
        g_evManager.RegisterListener(self)


    def Notify(self, event):
        if isinstance(event, evTick):

            # Always send in mouse pos event
            mouse_pos = pygame.mouse.get_pos()
            g_evManager.Post(evMouseMove(mouse_pos))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    g_evManager.Post(evQuit())
                    continue

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        g_evManager.Post(evQuit())
                        continue

                    g_evManager.Post(evKeyDown(event.key, event.unicode))

                if event.type == pygame.KEYUP:
                    g_evManager.Post(evKeyUp(event.key))
                    continue

                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Left click
                    if(pygame.mouse.get_pressed()[0]):
                        g_evManager.Post(evLMouseDown(mouse_pos))
                        continue

                    # Right click
                    if(pygame.mouse.get_pressed()[2]):
                        g_evManager.Post(evRMouseDown(mouse_pos))
                        continue
