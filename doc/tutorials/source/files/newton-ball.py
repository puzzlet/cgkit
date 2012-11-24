# A simplified version of Newton's cradle

defaultContactProps = ODEContactProperties(bounce = 1, mu = 1, soft_erp=0.5, soft_cfm=1E-10)
odeSim = ODEDynamics(gravity=9.81, substeps=50, defaultcontactproperties = defaultContactProps, use_quick_step = False)

matRed = GLMaterial(name="Red", diffuse=(1,0,0))
matGreen = GLMaterial(name="Green", diffuse=(0,1,0))

p = Plane(lx=2.5, ly=1)
s  = Sphere(radius = 0.1, pos = ( -1, 0, 0.1), mass = 1, material = matRed)
s1 = Sphere(radius = 0.1, pos = (  0, 0, 0.1), mass = 1, material = matGreen)
s2 = Sphere(radius = 0.1, pos = (0.2, 0, 0.1), mass = 1, material = matGreen)
s3 = Sphere(radius = 0.1, pos = (0.4, 0, 0.1), mass = 1, material = matGreen)
odeSim.add(list(worldroot.iterChilds()))

def onKeyPress(K):  
    if K.key.lower() == 'h':
        s.manip.addForce((100,0,0))
    if K.key.lower() == 'r':
        eventmanager.event(RESET)

eventmanager.connect(KEY_PRESS, onKeyPress)

print """
Press H to hit the balls
Press R to restart the simulation
"""
#execfile("console.py") 
