import pygame

from    Events.BEventManager import *
from 	Graphics.BColors import *
from	Graphics.BDraw import *


class LineMovingTargetView(object):
	def __init__(self, model):
		'''
		'''
		g_evManager.RegisterListener(self)
		self.m = model
		self.screen = pygame.display.get_surface()

		

	def Render(self):
		for t in self.m.keys():
			pos = self.m[t]["pos"]
			pygame.draw.circle(self.screen, red, pos, 30)
		
		g_evManager.Post(evModelDrawn())


	def Notify(self, event):
		if isinstance(event, evScreenCleared):
			self.Render()
			
