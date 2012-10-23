'''
Created on Jul 13, 2012

@author: trungtle
'''
import random
import pygame

import  Diags.BLogger
from    Events.BEventManager import *
import  Utility.util         as ns_util


#TIMER = pygame.time.Clock()

class Simulator(object):
    
    def __init__(self, modelManager):

        g_evManager.RegisterListener(self)

        self.modelManager   = modelManager
        self.inputbox       = None
        self.begin          = False

    def Init(self):
        self.pathChoice     = random.randint(0, 0)
        self.BeginPath(self.pathChoice)

    def BeginPath(self, choice):
        if choice == 0:
            self.path = KnowledgePath(self.modelManager)

    def Notify(self, event):
        if isinstance(event, evEnter):                   
            # Initialize
            self.Init()
            g_evManager.UnregisterListener(self)


class KnowledgePath(Simulator):
    def __init__(self, modelManager):
        super(KnowledgePath, self).__init__(modelManager)
        
        # Set up initial start in storyline
        self.story = ns_util.GetModel("Story", "knowledge")
        self.root = ns_util.GetModel("Path", "knowledge") 
        self.cur = self.root["past"]["intro"]
        self.ans = []

        # Retrieve inputbox
        self.inputbox = self.modelManager.Inputbox()

        # Retrieve label
        self.label = self.modelManager.StoryLabel()

        self.Refresh()

    def Refresh(self):
        # Set max ans len. 
        self.inputbox['max_word'] = self.cur['max_word']
        self.SetLabel(self.cur['id'])

    def AdvancePath(self, next):
        '''
        @param next: 2d array path to advance to
        '''
        if next is None:
            g_evManager.Post(evEnd())
            return

        self.cur = self.root[next[0]][next[1]]

    def SetLabel(self, id):
        '''
        @params id: 2d array path to the next point in the story
        '''
        self.label['text'] = self.story[id[0]][id[1]]        

    
    def GetAnswer(self):
        # If non-zero, retrieve answer
        if self.inputbox['max_word'] != 0:
            self.ans = self.inputbox['text']

    def Notify(self, event):
        if isinstance(event, evEnter):
            # Retrieve path
            self.AdvancePath(self.cur["next"])
            self.Refresh()

        elif isinstance(event,evKeyDown):
            self.GetAnswer()

        elif isinstance(event, evEnd):
            g_evManager.Post(evQuit())



    # index = 0
    # diff_t = TIMER.tick() * 1.0 / world['timeScale']
    
    # for rule in RULES:
    #     rule.Execute()


    # return True

