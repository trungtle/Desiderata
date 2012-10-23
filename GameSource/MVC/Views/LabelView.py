import pygame

from    Events.BEventManager import *
from 	Graphics.BColors import *
from	Graphics.BDraw import *
from	GameSource import UBUNTU_FONT_DIR

class LabelView(object):
	def __init__(self, model):
		'''
		'''
		g_evManager.RegisterListener(self)

		self.m = model
		self.screen = pygame.display.get_surface()
		self.font = pygame.font.Font(UBUNTU_FONT_DIR + self.m["font"], self.m["font_size"])


	def Render(self):
		if len(self.m['lines'][0]) != 0:
			for i in range(len(self.m['lines'])):
				pos = [self.m["pos"][0], self.m['pos'][1] + i * 50]
				img = self.screen.blit( \
						self.font.render(self.m["lines"][i], True, self.m["font_color"]), \
						pos
						)


	def Notify(self, event):
		if isinstance(event, evScreenCleared):
			self.Render()
			g_evManager.Post(evModelDrawn())
