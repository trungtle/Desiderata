'''
Created on Aug 21, 2012

@author: tle
'''
import importlib


import Views.LineMovingTargetView
import Views.CircleView
import Controllers.LineMovingTargetController
import Controllers.CircleController


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
        
        self.models[name] = model["json"]

        mStr = "Controllers." + \
                model["name"] + "Controller." + \
                model["name"] + "Controller(model['json'])"
        self.controllers[name] = eval(mStr)

        mStr = "Views." + \
                model["name"] + "View." + \
                model["name"] + "View(model['json'])"
        self.views[name] = eval(mStr)

        ModelManager.MODEL_ID += 1

    def Get(self, name):
        for k in self.models.keys():
            if name == k:
                return self.models[k]

    def Size(self):
        return len(self.models.keys())

