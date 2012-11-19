#!/usr/bin/env python
# Point cloud test utility

import sys, optparse
from cgkit import pointcloud
from cgkit.cgtypes import *

def readPtc(fileName, libName):
    """Read a point cloud file and dump it to stdout.
    """
    print ('Reading file "%s"...'%fileName) 
    ptc = pointcloud.open(fileName, "r", libName)
    print ("variables: %s"%ptc.variables)
    print ("npoints: %s"%ptc.npoints)
    print ("datasize: %s"%ptc.datasize)
    print ("bbox: %s"%ptc.bbox)
    print ("format %sx%s, %s"%ptc.format)
    print ("world2eye %s"%ptc.world2eye)
    print ("world2ndc %s"%ptc.world2ndc)
    print ("")
    
    for i in range(ptc.npoints):
        pos,normal,radius,data = ptc.readDataPoint()
        print ("%s %s %s %s"%(pos,normal,radius,data))
    ptc.close()

def writePtc(fileName, libName):
    """Write a test point cloud file.
    """
    print ('Writing file "%s"...'%fileName) 
    vars = [("float", "spam"), ("vector", "dir")]
    ptc = pointcloud.open(fileName, "w", libName, vars=vars, world2eye=mat4(2), world2ndc=mat4(1), format=(320,240,1.333))
    ptc.writeDataPoint((0.5, 0.6, 0.7), (0,1,0), 0.2, {"spam":0.5})
    ptc.writeDataPoint((1, 2, 3), (1,0,0), 0.3, {"spam":0.2})
    ptc.writeDataPoint((-1, 2.5, 17), (0,1,0), 0.2, {"spam":0.5})
    ptc.close()

def main():
    parser = optparse.OptionParser(usage="%prog [options] PtcFile")
    parser.add_option("-w", "--write", default=False, action="store_true", help="Write a test ptc file")
    parser.add_option("-l", "--lib-name", default="aqsis_tex", help="The renderer library implementing the point cloud API")
    
    opts,args = parser.parse_args()
    
    if len(args)==0:
        parser.print_help()
        sys.exit(1)
    
    fileName = args[0]
    libName = opts.lib_name
    
    if opts.write:
        writePtc(fileName, libName)
    else:
        readPtc(fileName, libName)
    
main()

