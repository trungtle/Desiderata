'''
Created on Aug 21, 2012

@author: tle
'''
import importlib

import Views.LabelView
import Controllers.LabelController

import Views.InputboxView
import Controllers.InputboxController


class ModelManager(object):
    '''
    '''
    MODEL_ID = 0

    def __init__(self):
        self.controllers = {}
        self.views = {}
        self.models = {}

    def Add(self, model):
        name = model["name"] + str(ModelManager.MODEL_ID)
        
        self.models[name] = model

        mStr = "Controllers." + \
                model["name"].capitalize() + "Controller." + \
                model["name"].capitalize() + "Controller(model)"
        self.controllers[name] = eval(mStr)

        mStr = "Views." + \
                model["name"].capitalize() + "View." + \
                model["name"].capitalize() + "View(model)"
        self.views[name] = eval(mStr)

        ModelManager.MODEL_ID += 1

    def Size(self):
        return len(self.models.keys())

    def Inputbox(self):
        for k in self.models.keys():
            if 'inputbox' in k:
                return self.models[k]

    def InputboxController(self):
        for k in self.models.keys():
            if 'inputbox' in k:
                return self.controllers[k]

    def StoryLabel(self):
        for k in self.models.keys():
            if 'label' in k:
                return self.models[k]
