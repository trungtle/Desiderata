import numpy


# ------------------------------------------ #
# @return: distance squared
# ------------------------------------------ #
def CalculateDisSqr(pos1, pos2):
    x1 = pos1[0]
    x2 = pos2[0]
    y1 = pos1[1]
    y2 = pos2[1]
    
    dSqr = (x1-x2)**2 + (y1-y2)**2
    return dSqr

# ------------------------------------------ #
# @return: numpy array of facing normalized
# ------------------------------------------ #
def CalculateFacingNormalized(fromPos,toPos):
    direction = (fromPos[0]-toPos[0],fromPos[1]-toPos[1])
    m = numpy.sqrt((direction[0])**2 + (direction[1])**2)    
    if(m == 0):
        m = 1
    return numpy.array([float(direction[0])/m,float(direction[1])/m])


# ------------------------------------------ #
# @return: numpy array of facing
# ------------------------------------------ #
def CalculateFacing(fromPos,toPos):
    return numpy.array([fromPos[0]-toPos[0],fromPos[1]-toPos[1]])


# ------------------------------------------ #
# @return: closest pos (in numpy array format) from source in a list of positions
# ------------------------------------------ #
def ClosestPos(src, targetListPos):
    '''
    @param : src is (x,y) 
    @param : targetListPos is of the format [(x,y), (x,y), (x,y)]
    
    @return : the closest point to src
    
    '''
    minDis = float("+inf")
    closestPos = None
    for p in targetListPos:
        dSqr = CalculateDisSqr(src, p)
        if(dSqr < minDis):
            minDis = dSqr
            closestPos = p
            
    return numpy.array(closestPos)
