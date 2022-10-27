from math import cos, radians, sin,pi,sqrt
import random

def getPos(a1,a4,a5,d1,d2,d3,d6):
    c1=cos(a1)
    c4=cos(a4)
    c5=cos(a5)
    s1=sin(a1)
    s4=sin(a4)
    s5=sin(a5)
    dx=c1*c4*s5*d6-s1*c5*d6-s1*d3
    dy=s1*c4*s5*d6+c1*c5*d6+c1*d3
    dz=-s4*s5*d6+d1+d2
    return (dx,dy,dz)

def partA():
    # Destination
    dx=1.2
    dy=.8
    dz=.5

    # Adjustable
    od1=0
    od2=.5
    od3=1
    oa1=-90*pi/180
    oa4=-90*pi/180
    oa5=90*pi/180
    oa6=40*pi/180 # This one doesn't matter for position

    # Constants
    d6=.2

    # Current Values
    a1=oa1
    a4=oa4
    a5=oa5
    d1=od1
    d2=od2
    d3=od3

    # speed
    s=.1
    bestdist=999999999999
    while bestdist>.0000000001:
        candidates=10
        x,y,z=getPos(a1,a4,a5,d1,d2,d3,d6)
        bestdist=(x-dx)**2+(y-dy)**2+(z-dz)**2
        s=sqrt(bestdist)/100
        for i in range(candidates):
            ca1=a1+(random.random()-.5)*s
            ca4=a4+(random.random()-.5)*s
            ca5=a5+(random.random()-.5)*s
            cd1=d1+(random.random()-.5)*s
            cd2=d2+(random.random()-.5)*s
            cd3=d3+(random.random()-.5)*s
            x,y,z=getPos(ca1,ca4,ca5,cd1,cd2,cd3,d6)
            dist=(x-dx)**2+(y-dy)**2+(z-dz)**2
            if dist<bestdist:
                bestdist=dist
                a1=ca1
                a4=ca4
                a5=ca5
                d1=cd1
                d2=cd2
                d3=cd3
    print(a1,a4,a5,d1,d2,d3)

partA()