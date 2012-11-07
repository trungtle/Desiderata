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

		# Reinitialize

		self.done = False
		self.curFrame = 0
		self.curLen = 0
		lineLen = self.m['line_len']

		# These are used for checking if text is new
		self.prevLen = len(self.m['text'])
		self.preCheckChar = self.m['text'][:]

		# Split string into multiple lines

		tokens = self.m["text"].split()
		self.lines = []
		for i in range(0, len(tokens), lineLen):
			self.lines.append(' '.join(tokens[i:i + lineLen]))

		# Make empty lines to prepare for drawing in view

		self.m['lines'] = ['']*len(self.lines)
		self.lineCount = 0


	def IsNewText(self):
		return (self.prevLen != len(self.m['text']) or
				self.preCheckChar != self.m['text'][:])


	def Notify(self, event):
		if isinstance(event, evRefresh):			

			#
			# Refresh if we have a new text
			#
			#if (self.IsNewText()) : self.Refresh()
			self.Refresh()

		elif isinstance(event, evTick):

			if not self.done: self.curFrame += 1
			
			#
			# Instant draw if there's no frames
			#

			if self.m['frames'] == 0:
				self.m['lines'] = self.lines
				if not self.done: g_evManager.Post(evUpdatedLabel())
				self.done = True

			#
			# Only update on mutiples of self.m['frames']
			#

			elif self.curFrame % self.m["frames"] == 0:

				# There is nothing to update
				if len(self.lines) == 0 or self.m['text'] == '':
					self.m['lines'] = []
					if not self.done: g_evManager.Post(evUpdatedLabel())
					self.done = True

				# Update character

				elif self.curLen < len(self.lines[self.lineCount]):
					self.curLen += 1
					self.m['lines'][self.lineCount] = \
								''.join(self.lines[self.lineCount][0:self.curLen])

				# Update lines

				elif (self.curLen == len(self.lines[self.lineCount])):
					if(self.lineCount < len(self.lines) - 1):
						self.lineCount += 1
						self.curLen = 0

					# Finished update

					else:
						if not self.done: g_evManager.Post(evUpdatedLabel())
						self.done = True
