import pygame
from pygame.locals import *

from    Events.BEventManager import *
from	GameSource import UBUNTU_FONT_DIR

class LabelController(object):
	def __init__(self, model):
		'''
		'''
		g_evManager.RegisterListener(self)

		self.m = model
		self.Refresh()

	def Refresh(self):
		self.curFrame = 0
		self.curLen = 0
		lineLen = self.m['line_len']

		# Split string into
		self.len = len(self.m['text'])
		self.checkChar = self.m['text'][-1:0]

		tokens = self.m["text"].split()
		self.lines = []
		for i in range(0, len(tokens), lineLen):
			self.lines.append(' '.join(tokens[i:i + lineLen]))

		# Make empty lines to prepare for drawing
		self.m['lines'] = ['']*len(self.lines)
		self.lineCount = 0

	def IsNewText(self):
		return (self.len != len(self.m['text']) or
				self.checkChar != self.m['text'][-1:0])

	def Notify(self, event):
		if isinstance(event, evTick):

			# Refresh if we have a new text
			if (self.IsNewText()):
				self.Refresh()

			# Count up to self.m["frames"] to update the next character
			# to label
			self.curFrame += 1
			self.curFrame %= self.m["frames"]
			if self.curFrame == 0:

				# Do not update more if we have displayed all

				# Update character
				if self.curLen < len(self.lines[self.lineCount]):
					self.curLen += 1
					self.m['lines'][self.lineCount] = \
								''.join(self.lines[self.lineCount][0:self.curLen])

				# Update lines
				else:
					if (self.lineCount < len(self.lines) - 1):
						self.lineCount += 1
						self.curLen = 0
				
