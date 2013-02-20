import pygame

from    Events.BEventManager import *
from 	Graphics.BColors import *
from	Graphics.BDraw import *


class CircleView(object):
	def __init__(self, model):
		'''
		'''
		g_evManager.RegisterListener(self)
		self.m = model
		self.screen = pygame.display.get_surface()
		
		

	def Render(self):
		pygame.draw.circle(self.screen, green, self.m["pos"], self.m["radius"],2)	
		g_evManager.Post(evModelDrawn())


	def Notify(self, event):
		if isinstance(event, evScreenCleared):
			self.Render()
		