import pygame
from pygame.locals import *

from    Events.BEventManager import *
import Utility.util         as ns_util

class CircleController(object):
	def __init__(self, model):
		'''
		'''
		g_evManager.RegisterListener(self)
		self.m = model


	def update(self):
		pass
	

	def AddCircle(self, pos):
		print pos


	def Notify(self, event):
		pass
		



