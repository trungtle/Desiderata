'''
Created on Jul 13, 2012

@author: trungtle
'''
import sys
import pygame
import numpy
import Diags.BLogger

# ------------------------------------------ #
# Check if pos is outside of the view rect.
#@return: collidedSides is where in the screen the collision happened.
# ------------------------------------------ #
def CheckScreenBoundary(viewRect, pos, size):
    collidedSides = {'top': False, 'bottom': False, 'left': False, 'right': False}
    
    if pos[0] <= viewRect.left:
        collidedSides['left'] = True
        
    if pos[0] + size[0] >= viewRect.right:
        collidedSides['right'] = True
        
        
    if pos[1] <= viewRect.top:
        collidedSides['top'] = True
        
    if pos[1] + size[1] > viewRect.bottom:
        collidedSides['bottom'] = True        

    return collidedSides


# ------------------------------------------ #
# Check if 2 objects are collided. Return the collidedSides of obj1 when it collided with obj2
# ------------------------------------------ #
def CheckCollide(m1, m2):
    xAxis_result, yAxis_result = __ProjectionTestRR(pygame.Rect(m1['pos'], m1['size']), \
                                                    pygame.Rect(m2['pos'], m2['size']), \
                                                    m1['vel'])
    
    # If either axis is none, that means no overlap and we can stop there
    if(xAxis_result is None or yAxis_result is None):
        return {'top': False, 'bottom': False, 'left': False, 'right': False}
    
    # Otherwise, update model1's position to avoid collision
    if numpy.abs(xAxis_result[1]) < numpy.abs(yAxis_result[1]):
        m1['pos'][0] += xAxis_result[1]
        #m1['vel'][0] = -m1['vel'][0]*.5    # Object bounces on the side
    else:
        m1['pos'][1] += yAxis_result[1]
        m1['vel'][1] *= .9  # Reduce speed of object so if they're hanging by gravity, it's not building up
        
        
    # Determine which side of obj1 that collided with obj2
    collidedSides = {'top': False, 'bottom': False, 'left': False, 'right': False}
    if xAxis_result[1] < 0:
        collidedSides['right'] = True
    else:
        collidedSides['left'] = True
    
    if yAxis_result[1] <= 0:
        collidedSides['bottom'] = True
    else:
        collidedSides['top'] = True
        
    return collidedSides

     
       


# ------------------------------------------ #
# Projection test Rect on Rect
# @param s1 has a velocity of vel1
# @return: ((isOverlapped axis1, disToMove), (isOverlapped axis2, disToMove))
# ------------------------------------------ #
def __ProjectionTestRR(s1,s2,vel1 = [0,0]):
    s1 = [s1.topleft,s1.topright,s1.bottomright,s1.bottomleft]
    s2 = [s2.topleft,s2.topright,s2.bottomright,s2.bottomleft]
    xAxis = numpy.array([1,0])
    yAxis = numpy.array([0,1])
    return (__TestAxis(s1,s2,vel1,xAxis),__TestAxis(s1,s2,vel1,yAxis))
    
    
# ------------------------------------------ #
# Test if projections of 2 rects over a given axis overlap
# @return: (True for overlapping without velocity/False for overlapping with velocity, 
#            dist to move away from and resolve overlap)
# ------------------------------------------ #
def __TestAxis(s1,s2,vel1,axis):
    returnValue = None
    
    # -- Find the projection over the given axis
    projS1 = __FindOrthoProj(s1,axis)
    projS2 = __FindOrthoProj(s2,axis)
    
    # -- Find distance between the projections
    dist = __ProjectionDist(projS1,projS2)
    
    # Distance is less than 0, that means overlap at this frame
    if(dist < 0):
        s1_topleft = s1[0]
        s2_topleft = s2[0]
        
        # Determine move distance by examining location of the topleft
        if(s1_topleft[0]*axis[0] > s2_topleft[0]*axis[0] or s1_topleft[1]*axis[1] > s2_topleft[1]*axis[1]):
            dist = -dist
            
            
        returnValue = (True,dist)
    # Not overlapped yet, but now we check for the case of potential overlapping from moving 
    else:
        dotVel = vel1[0]*axis[0]+vel1[1]*axis[1]
        # Vel going negative, add to current projection of s1
        if(dotVel < 0):
            projS1[0] += dotVel
        else:
            projS1[1] += dotVel
            
        # -- Find distance between the new potential projections created by moving
        veldist = __ProjectionDist(projS1,projS2)
        
        # Next frame with overlap
        if(veldist < 0):
            s1_topleft = s1[0]
            s2_topleft = s2[0]
            if(s1_topleft[0] > s2_topleft[0]):
                dist = -dist
            returnValue = (False,dist)
    
    return returnValue

# ------------------------------------------ #
# Find the distance between projection a and b
# @param a, b: a[start/min, end/max], b[start/min, end/max]
# ------------------------------------------ #
def __ProjectionDist(a,b):
    if(a[0] < b[0]):
        return b[0] - a[1]
    return a[0] - b[1]


# ------------------------------------------ #
# Return projection of given points on a given axis
# ------------------------------------------ #
def __FindOrthoProj(points,axis):
    dpMax = -sys.maxint
    dpMin = sys.maxint
    for point in points:
        # Dotproduct
        dp = point[0]*axis[0]+point[1]*axis[1]
        if(dp > dpMax):
            dpMax = dp
        if(dp < dpMin):
            dpMin = dp
    return [dpMin,dpMax]

