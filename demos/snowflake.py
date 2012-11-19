# Render a Koch snowflake as procedurals.
# This is the example from the manual (chapter "cri").
# To render the snowflake, run this script directly
# (without using the render tool).

import cgkit.cri
from cgkit.cgtypes import *

def bound(A, E):
    """Compute the bounding box of one segment."""
    eps = 0.03
    dv = E-A
    n = vec3(-dv.y, dv.x, 0)
    C = 0.5*(A+E) + 0.2887*n
    xx = [A.x, C.x, E.x]
    yy = [A.y, C.y, E.y]
    bound = [min(xx)-eps, max(xx)+eps, min(yy)-eps, max(yy)+eps, -0.001, 0.001]
    return bound

def subdiv(data, detail):
    """Subdivide function."""
    A,E = data
    dv = E-A
    if dv.length()<0.005:
        RiCurves(RI_LINEAR, [2], RI_NONPERIODIC, P=[A,E], constantwidth=0.003)
    else:
        t = 1.0/3
        B = (1.0-t)*A + t*E
        D = (1.0-t)*E + t*A
        n = vec3(-dv.y, dv.x, 0)
        C = 0.5*(A+E) + 0.2887*n
        RiProcedural((A,B), bound(A,B), subdiv)
        RiProcedural((B,C), bound(B,C), subdiv)
        RiProcedural((C,D), bound(C,D), subdiv)
        RiProcedural((D,E), bound(D,E), subdiv)

# Load the RenderMan API.
# Replace the library name with whatever renderer you want to use.
ri = cgkit.cri.loadRI("/Library/Pixie/lib/libri.dylib")
cgkit.cri.importRINames(ri, globals())

RiBegin(RI_NULL)
RiFormat(1024,768,1)
#RiDisplay("koch.tif", RI_FRAMEBUFFER, RI_RGB)
RiDisplay("koch.tif", RI_FILE, RI_RGB)
RiPixelSamples(3,3)
RiProjection(RI_ORTHOGRAPHIC)
RiScale(vec3(0.8))
RiTranslate(0,0.55,5)
RiWorldBegin()
RiSurface("constant")
RiColor((1,1,1))
RiPatch(RI_BILINEAR, P=[-2,2,1, 2,2,1, -2,-2,1, 2,-2,1])
RiColor((0,0,0))
RiProcedural((vec3(-1,0,0),vec3(1,0,0)), [-2,2, -2,2, -0.01,0.01], subdiv)
RiProcedural((vec3(0,-1.732,0),vec3(-1,0,0)), [-2,2, -2,2, -0.01,0.01], subdiv)
RiProcedural((vec3(1,0,0), vec3(0,-1.732,0)), [-2,2, -2,2, -0.01,0.01], subdiv)
RiWorldEnd()
RiEnd()
