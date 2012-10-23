'''
Created on Jul 13, 2012

@author: trungtle
'''
import numpy
import Diags.BLogger

# ------------------------------------------ #
# ------------------------------------------ #
def UpdateMotion(pos, vel, accl, t):
    # Convert to array if not already there
    if not isinstance(pos, numpy.ndarray):
        pos = numpy.asarray(pos, numpy.float32)
    if not isinstance(vel, numpy.ndarray):
        vel = numpy.asfarray(vel, numpy.float32)
    if not isinstance(accl, numpy.ndarray):
        accl = numpy.asarray(accl, numpy.float32)


    __UpdateVelocity(vel, accl, t)    
    __UpdatePosition(pos, vel, t)
    
    return pos, vel, accl
    
# ------------------------------------------ #
# ------------------------------------------ #
def __UpdatePosition(pos, vel, t):
    #update pos
    pos += vel*t


# ------------------------------------------ #
# ------------------------------------------ #
def __UpdateVelocity(vel, accl, t):
    # Update vel
    vel += accl*t    


def AddGravity(gravity, vel, t):
    # Convert to array if not already there
    if not isinstance(vel, numpy.ndarray):
        vel = numpy.asfarray(vel, numpy.float32)

    # Update vel
    vel += gravity*t

# ------------------------------------------ #
# Combine force together to find the acceleration
# @return: acceleration
# ------------------------------------------ #
def ComputeAccl(mass, force ):
    if mass != 0:
        # Convert to array if not already there
        if not isinstance(force, numpy.ndarray):
            force = numpy.asfarray(force,numpy.float32)
        accl = force/mass
        return accl
    else:
        return 0


