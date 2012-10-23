import numpy
import pygame

from BColors import *

# ------------------------------------------ #
# Main draw function
# ------------------------------------------ #
def Draw(screen):
    ClearBgTo(screen)
    


# ------------------------------------------ #
# Function to clear background
# ------------------------------------------ #
def ClearBgTo(screen, background = None, pos = (0,0), area = None):

    screen.fill(white)
    if(background is not None):
        screen.blit(background, pos, area)


# ------------------------------------------ #
# ------------------------------------------ #
def Fade(srcImage, frames, destImage = None, reverse = False):
    '''
    fade image to black or reverse
    @param frames: fade for how many frames?
    @param image, dest: surface
    @param reverse: true -> fade to black, false -> black to image
    @return faded surface 
    '''
    
    screen = pygame.display.get_surface()
    rect = screen.get_rect()
    
    # Get the pixel array
    imageBuf = pygame.surfarray.array3d(srcImage)
    
    # Destination array. If none specified, use black
    if(destImage is None):
        destBuf = numpy.zeros(imageBuf.shape)
    else:
        destBuf = pygame.surfarray.array2d(destImage)
         
    for i in range(frames):
        diff = (destBuf - imageBuf)/(frames - i) 
        xfade = imageBuf + diff.astype(numpy.int)
        pygame.surfarray.blit_array(screen, xfade)
        pygame.display.flip()
        imageBuf = numpy.array(xfade)
    
    return True

# ------------------------------------------ #
# ------------------------------------------ #
def CrazyEffect(image, frames):
    '''
    CRAZY EFFECT BY MISTAKE!
    @param frames: fade for how many frames?
    @param image: surface
    @param reverse: true -> fade to black, false -> black to image
    @return faded surface 
    '''
    
    screen = pygame.display.get_surface()
    rect = screen.get_rect()
    imageBuf = pygame.surfarray.array3d(image)
    
    imageBufArray = numpy.array(imageBuf)
    dest = numpy.array(imageBuf.shape)
    dest[:] = (0, 0, 0)
    diff = (dest - imageBufArray)/(frames)
    
    for i in range(frames):
        xfade = imageBufArray + diff.astype(numpy.int)
        pygame.surfarray.blit_array(screen, xfade)
        pygame.display.flip()
        imageBufArray = numpy.array(xfade)
    
    return True
    