from math import cos, radians, sin,pi,sqrt
import random

def getPos(a1,a2,a3,a4,a5,a6,d1,d2,d3,d6):
    c1=cos(a1)
    c2=cos(a2)
    c3=cos(a3)
    c4=cos(a4)
    c5=cos(a5)
    c6=cos(a6)
    s1=sin(a1)
    s2=sin(a2)
    s3=sin(a3)
    s4=sin(a4)
    s5=sin(a5)
    s6=sin(a6)
    dx=c1*c4*s5*d6-s1*c5*d6-s1*d3
    dy=s1*c4*s5*d6+c1*c5*d6+c1*d3
    dz=-s4*s5*d6+d1+d2
    return (dx,dy,dz)

def partA():
    dx=1.2
    dy=.8
    dz=.5
    d2=.5
    d3=1
    oa1=-90*pi/180
    oa2=0
    oa3=0
    oa4=-90*pi/180
    oa5=90*pi/180
    oa6=40*pi/180
    d6=.2
    a1=oa1
    a2=oa2
    a3=oa3
    a4=oa4
    a5=oa5
    a6=oa6
    s=.1
    bestdist=999999999999
    while bestdist>.0001:
        candidates=10
        x,y,z=getPos(a1,a2,a3,a4,a5,a6,0,d2,d3,d6)
        bestdist=(x-dx)**2+(y-dy)**2+(z-dz)**2
        s=sqrt(bestdist)/100
        for i in range(candidates):
            ca1=a1+(random.random()-.5)*s
            ca2=a2+(random.random()-.5)*s
            ca3=a3+(random.random()-.5)*s
            ca4=a4+(random.random()-.5)*s
            ca5=a5+(random.random()-.5)*s
            ca6=a6+(random.random()-.5)*s
            x,y,z=getPos(ca1,ca2,ca3,ca4,ca5,ca6,0,d2,d3,d6)
            dist=(x-dx)**2+(y-dy)**2+(z-dz)**2
            if dist<bestdist:
                bestdist=dist
                a1=ca1
                a2=ca2
                a3=ca3
                a4=ca4
                a5=ca5
                a6=ca6
    print(a1,a2,a3,a4,a5,a6)

partA()