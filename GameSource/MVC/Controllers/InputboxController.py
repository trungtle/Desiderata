import pygame
from pygame.locals import *

from    Events.BEventManager import *
from	GameSource import UBUNTU_FONT_DIR

class InputboxController(object):
	def __init__(self, model):
		'''
		'''
		g_evManager.RegisterListener(self)

		self.m = model
		self.font = pygame.font.Font(UBUNTU_FONT_DIR + self.m["font"], self.m["font_size"])
		self.text = list(self.m["text"])


	def Refresh(self):
		self.m["size"] = list(self.font.size(self.m["text"]))
		if self.m['max_word'] == 0:
			self.ClearText()
			self.m['cursor'] = False
		else:
			self.m['cursor'] = True

	def ClearText(self):
		self.text = []
		self.m['text'] = ''

	def Notify(self, event):
		if isinstance(event, evTick):
			# Assume refresh rate is faster than key down event
			self.Refresh()

		elif isinstance(event, evKeyDown):
			if event.key == K_BACKSPACE or event.key == K_DELETE:
				self.text = self.text[0:-1]
			
			elif event.key == K_RETURN:
				g_evManager.Post(evEnter())

			elif event.key <= 127:

				# Cap the size of input box
				if len(self.text) != self.m['max_word']:
					char = str(event.unicode)
					self.text.append(char)

			self.m["text"] = "".join(self.text)
