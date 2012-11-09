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
            self.choice = Path1(self.modelManager)


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


class Path1(Simulator):
    def __init__(self, modelManager):

        g_evManager.RegisterListener(self)
        self.modelManager   = modelManager

        # Set up initial start in storyline
        self.story = ns_util.GetModel("Story", "layer1")
        self.path = ns_util.GetModel("Path", "layer1") 
        
        self.curPath = GetNode(self.path, (CONFIG["initial"]["checkPoint"],))
        self.curStory = {}
        for k in ('p', 'b', 'h'):
            self.curStory[k] = GetNode(self.story, (CONFIG["initial"]["checkPoint"], k))

        # Retrieve inputbox
        self.inputbox = self.modelManager.Get('ib')

        # Retrieve labels
        self.lb = {}
        for k in ('p', 'b', 'h'):
            self.lb[k] = self.modelManager.Get(k)

        self.ans = ['']
        self.vars = ['']
        self.next = ('',)
        self.isThinker = CONFIG["initial"]["isThinker"]
        self.a1 = CONFIG["initial"]["a1"]
        self.a2 = CONFIG["initial"]["a2"]
        self.a3 = CONFIG["initial"]["a3"]
        self.hasName = CONFIG["initial"]["hasName"]

        self.Refresh()


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

        self.next = tuple(self.curPath['next']) 
        self.ParseLogic()       
        self.curPath = GetNode(self.path, self.next)

        for k in self.curStory.keys():
            self.curStory[k] = GetNode(self.story, self.next + (k,))

        self.Refresh()

    def ParseLogic(self):
        #
        # Build up replacement
        #

        if self.next[0] == "believer":
            self.vars = ['Faith']
            self.isThinker = False

        elif self.next[0] == "thinker":
            self.vars = ['Knowledge']
            self.isThinker = True

        elif self.next[0] == "h_no_name1":
            self.hasName = False

        elif self.next[0] == "h_name1":
            self.hasName = True

        elif self.next[0] == "a1" or self.next[0] == 'a2' or self.next[0] == 'a3':
            #
            # Trim out quote
            #

            trimmedAns = self.ans[1:-1]
            self.vars = [trimmedAns]

            if self.next[0] == 'a1':
                self.a1 = trimmedAns
            elif self.next[0] == 'a2':
                self.a2 = trimmedAns
            elif self.next[0] == 'a3':
                self.a3 = trimmedAns

        elif self.next[0] == "ending":

            if self.a1 == 'random' and \
                (self.a2 == 'tails' or self.a2 == 'always tail') and \
                self.a3 == 'choose the slice':

                if (self.isThinker and self.hasName) or (not self.isThinker and not self.hasName):
                    self.vars = ["The beast looked at you sleeping. The forest stired quietly like a child. The rain stopped. As the beast smiled, he knew you have passed the first test..."]

                else:
                    if self.isThinker and not self.hasName:
                        self.vars = ["The beast looked at you sleeping. He was in disapproval, as for a thinker like you to willingly give up your name without hesitance. You needed to be more careful. Without a sound, the beast silently walked away. The chill overwhelming took over the forest. The road to the Gate is closed..."]
                    if not self.isThinker and self.hasName:
                        self.vars = ["The beast looked at you sleeping. He was in disapproval, as for a believer like you to not be trusting him enough to share your real name. The Gate does not give answers to those without Faith. Without a sound, the beast silently walked away. The chill overwhelming took over the forest. The road to the Gate is closed..."]
            else:
                self.vars = ["The beast looked at you sleeping, then without a sound, he silently walked away. He knew you didn't have the answers. The chill overwhelming took over the forest. The road to the Gate is closed..."]


    def Refresh(self):

        # Re-init

        self.labelDoneCount = 0
        self.ready = False

        # Set max possible len for ans

        self.inputbox['max_word'] = self.curPath['ans_len']

        # Update the text with current node in path

        for k in self.lb:
            if self.curStory[k] is not None:
                text = self.ParseText(self.curStory[k])
                if k == 'b':
                    self.lb[k]['text'] = "Beast: '" + text + "'"
                elif k == 'h':
                    self.lb[k]['text'] = "'" + text + "'"
                else:
                    self.lb[k]['text'] = text
            else:
                self.lb[k]['text'] = ""

        g_evManager.Post(evRefresh())


    def ParseText(self, text):
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
            tempStr[i:i+len('$$$')] = [self.vars[varI]]
            text = ''.join(tempStr)
            i = text.find('$$$')
            varI += 1

        return text


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

        elif isinstance(event, evEnd):
            g_evManager.Post(evQuit())

    
def GetNode(root, nodeId):
    '''
    Recursively traverse the path tree to find the node

    @params: nodeId is a tuple that defines that path to that node
    '''
    if len(nodeId) == 1:
        if nodeId[0] in root:
            return root[nodeId[0]]
    elif nodeId[0] in root:
        return GetNode(root[nodeId[0]], nodeId[1:])                

