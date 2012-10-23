import pygame

from    Events.BEventManager import *
from 	Graphics.BColors import *
from	GameSource import UBUNTU_FONT_DIR

class InputboxView(object):
	def __init__(self, model):
		'''
		'''
		g_evManager.RegisterListener(self)

		self.m = model
		self.screen = pygame.display.get_surface()
		self.font = pygame.font.Font(UBUNTU_FONT_DIR + self.m["font"], self.m["font_size"])


	def Render(self):
		if (self.m['cursor']):
			self.RenderCursor()

		if len(self.m["text"]) != 0:
			self.screen.blit( \
					self.font.render(self.m["text"], True, black), \
					self.m["pos"]
					)

	def RenderCursor(self):
		cursorPos = [self.m['pos'][0] + self.m['size'][0] + 2, self.m['pos'][1]]
		cursorSize = [3, self.m['size'][1]]
		
		pygame.draw.rect(self.screen, \
						(200, 200, 200), \
						pygame.Rect(cursorPos,cursorSize), \
						3)


	def Notify(self, event):
		if isinstance(event, evScreenCleared):
			self.Render()
			g_evManager.Post(evModelDrawn())
