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

    def Add(self, model, name):
        name = name
        
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

    def Get(self, name):
        for k in self.models.keys():
            if name == k:
                return self.models[k]

    def Size(self):
        return len(self.models.keys())

