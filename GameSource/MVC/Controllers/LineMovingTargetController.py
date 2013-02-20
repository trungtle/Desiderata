import pygame
from pygame.locals import *

from    Events.BEventManager import *
class LineMovingTargetController(object):
	def __init__(self, model):
		'''
		'''
		g_evManager.RegisterListener(self)
		self.m = model

	def update(self):

		for t in self.m.keys():
			endpoint1 = self.m[t]["endpoint1"]
			endpoint2 = self.m[t]["endpoint2"]
			pos = self.m[t]["pos"]
			bearing = self.m[t]["bearing"]
			if(pos[0] > endpoint2[0]):
				bearing *= -1	
				self.m[t]["bearing"] = bearing
			elif(pos[0] < endpoint1[0]):
				bearing *= -1
				self.m[t]["bearing"] = bearing
			
			pos[0] += bearing * 1
			self.m[t]["pos"] = pos



	def Notify(self, event):
		if isinstance(event, evTick):
			self.update()


