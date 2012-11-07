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

varMatch = '(\${3})'

class Simulator(object):
    
    def __init__(self, modelManager):

        g_evManager.RegisterListener(self)
        self.modelManager   = modelManager
        self.ready = False
        self.labelDoneCount = 0

    def Init(self):

        #
        # Play background music
        #

        if CONFIG["music"]["on"]:
            pygame.mixer.music.play(-1)

        #
        # Choose randomly a path to begin
        #

        self.pathChoice     = random.randint(0, 0)
        self.BeginPath(self.pathChoice)


    def BeginPath(self, choice):
        if choice == 0:
            self.choice = KnowledgePath(self.modelManager)


    def Notify(self, event):
        if isinstance(event, evEnter):
            if self.ready:
                # Initialize
                self.Init()
                g_evManager.UnregisterListener(self)
        
        elif isinstance(event, evUpdatedLabel):
            self.labelDoneCount += 1
            if self.labelDoneCount == 1:
                self.ready = True


class KnowledgePath(Simulator):
    def __init__(self, modelManager):

        g_evManager.RegisterListener(self)
        self.modelManager   = modelManager

        # Set up initial start in storyline
        self.story = ns_util.GetModel("Story", "knowledge")
        self.path = ns_util.GetModel("Path", "knowledge") 
        
        self.curPath = self.GetNode(self.path, ('intro1',))
        self.curStory = {}
        for k in ('p', 'b', 'h'):
            self.curStory[k] = self.GetNode(self.story, ('intro1', k))

        # Retrieve inputbox
        self.inputbox = self.modelManager.Get('ib')

        # Retrieve labels
        self.lb = {}
        for k in ('p', 'b', 'h'):
            self.lb[k] = self.modelManager.Get(k)

        self.ans = ['']
        self.vars = ['']

        self.Refresh()


    def Refresh(self):

        # Re-init

        self.labelDoneCount = 0
        self.ready = False

        # Set max possible len for ans

        self.inputbox['max_word'] = self.curPath['ans_len']

        # Update the text with current node in path

        for k in self.lb:
            if self.curStory[k] is not None:
                if k == 'b':
                    self.lb[k]['text'] = "Beast: '" + self.curStory[k] + "'"
                elif k == 'h':
                    self.lb[k]['text'] = "'" + self.curStory[k] + "'"
                else:
                    self.lb[k]['text'] = self.curStory[k]
            else:
                self.lb[k]['text'] = ""

        g_evManager.Post(evRefresh())


    def ReplaceText(self, text, vars):
        '''
        '''
        
        #
        # Break text into characters
        #

        tempStr = list(text)

        #
        # Search for special placeholders
        #

        varI = 0
        i = text.find('$$$')
        while i != -1:
            tempStr[i:i+len('$$$')] = [vars[varI]]
            text = ''.join(tempStr)
            i = text.find('$$$')
            varI += 1

        return text


    def GetNode(self, root, nodeId):
        '''
        Recursively traverse the path tree to find the node

        @params: nodeId is a tuple that defines that path to that node
        '''
        if len(nodeId) == 1:
            if nodeId[0] in root:
                return root[nodeId[0]]
        elif nodeId[0] in root:
            return self.GetNode(root[nodeId[0]], nodeId[1:])    


    def GetAnswer(self):
        '''
        @return: True for valid answer and False for invalid answer
        '''
        if self.curPath['ans_len'] == 0:
            g_evManager.Post(evAdvance())
            return

        self.ans = self.inputbox['text']
        
        # Check for valid answer
        
        for i, a in enumerate(self.curPath['valid_ans']):
            if self.ans.lower() == a.lower():

                #
                # Match next with answer
                #
                self.curPath['next'] = self.curPath['p_next'][i]

                #
                # Signal to advance
                #

                g_evManager.Post(evAdvance())   


    def AdvancePath(self):
        '''
        '''
        if self.curPath['next'] is None:
            g_evManager.Post(evEnd())
            return

        next = tuple(self.curPath['next'])
        self.curPath = self.GetNode(self.path, next)

        for k in self.curStory.keys():
            self.curStory[k] = self.GetNode(self.story, next + (k,))


    def Notify(self, event):
        if isinstance(event, evEnter):
            if self.ready:
                self.GetAnswer()

        elif isinstance(event, evUpdatedLabel):

            #
            # Set ready when all labels are done
            #

            self.labelDoneCount += 1
            
            if self.labelDoneCount == len(self.curStory):
                self.ready = True
        
        elif isinstance(event, evAdvance):
            self.AdvancePath()
            self.Refresh()

        elif isinstance(event, evEnd):
            g_evManager.Post(evQuit())

