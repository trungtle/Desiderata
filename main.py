'''
Created on July 13, 2012

@author: trungtuanle
'''
import importlib
import sys
import pygame

sys.path.append("EngineCore")
sys.path.append("GameSource")

import EngineCore
import GameSource

if __name__ == '__main__':

    # initialize level to 1
    nextLevel = 1
    
    # ------------ Main Game Loop --------------- #
    # Level = 0 is the end of game
    while nextLevel != 0:
    
        # Import the next level
        lvlStr = ".Level" + str(nextLevel) + ".Level" + str(nextLevel)
        levelModule = importlib.import_module(lvlStr, 'Levels')

        level = levelModule.Level()

        # Init phase
        level.Initialize()
        level.LoadModels()
        level.LoadResources()
    
        
        # ------------ Main Level Loop --------------- #
        level.spinner.Run()            

        nextLevel = level.LevelUp()
    
    pygame.quit()