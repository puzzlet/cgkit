# pyODE example 3: Collision detection
# Rewritten for cgkit/ODEDynamics by Alex Dumitrache
# Original code by Matthias Baas.

import random

objects = []
counter = 0
state = 0

# Create a ground plane
p = Plane(lx = 5, ly = 5)

# Set contact properties and initialize ODEDynamics
defaultContactProps = ODEContactProperties(bounce = 0.2, mu = 5000)
odeSim = ODEDynamics(gravity=9.81, substeps=2, cfm=1e-5, erp=0.8, defaultcontactproperties = defaultContactProps, use_quick_step = False, auto_add = True)

# Add a little damping to prevent ODE from crashing
odeSim.world.setLinearDamping(1e-5)
odeSim.world.setAngularDamping(1e-5)
odeSim.world.setMaxAngularSpeed(100)

def rz(ang):
    """Elementary rotation around Z"""
    return mat3(1).rotate(ang, (0,0,1))

def drop_object():
    """Drop an object into the scene."""

    pos = (random.gauss(0,0.1), random.gauss(0,0.1), 3)
    rot = rz(random.uniform(0, 2*pi))
    b = Box(lx=1, ly=0.2, lz=0.2, pos=pos, rot=rot, mass=1000*1*0.2*0.2)
    
    odeSim.add(b)
    objects.append(b)

def explosion():
    """Simulate an explosion.

    Every object is pushed away from the origin.
    The force is dependent on the objects distance from the origin.
    """
    for b in objects:
        l = b.pos
        d = abs(l)
        l = max(0, 20000*(1.0-0.2*d*d)) * vec3(l[0] / 4, l[1] / 4, l[2]).normalize()
        b.manip.addForce(l)

def pull():
    """Pull the objects back to the origin.

    Every object will be pulled back to the origin.
    Every couple of frames there'll be a thrust upwards so that
    the objects won't stick to the ground all the time.
    """
    for b in objects:
        b.manip.addForce(-500 * b.pos.normalize())
        if counter % 60 == 0:
            b.manip.addForce((0,0,5000))

def onStepFrame():
    global counter, state
    counter += 1

    # State 1: Drop objects
    if state==0:
        if counter==20:
            drop_object()
            counter = 0
        if len(objects) == 30:
            state=1
            counter=0
    # State 1: Explosion and pulling back the objects
    elif state==1:
        if counter==100:
            explosion()
        if counter>300:
            pull()
        if counter==500:
            counter=20
            
eventmanager.connect(STEP_FRAME, onStepFrame)
