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

def dumbSearch(dx,dy,dz,od1,od2,od3,oa1,oa4,oa5,d6):
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
    giveup =0
    while bestdist>.00000001:
        giveup+=1
        if giveup>100:
            return None
        candidates=10
        x,y,z=getPos(a1,a4,a5,d1,d2,d3,d6)
        bestdist=(x-dx)**2+(y-dy)**2+(z-dz)**2
        s=sqrt(bestdist)
        for i in range(candidates):
            ca1=a1+(random.random()-.5)*s
            ca4=a4+(random.random()-.5)*s
            ca5=a5+(random.random()-.5)*s
            cd1=abs(d1+(random.random()-.5)*s)
            cd2=abs(d2+(random.random()-.5)*s)
            cd3=abs(d3+(random.random()-.5)*s)
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
    return (a1,a4,a5,d1,d2,d3)
# Take into account distances
def cost(oa1,oa4,oa5,od1,od2,od3,ca1,ca4,ca5,cd1,cd2,cd3,wa1,wa4,wa5,wd1,wd2,wd3):
    return abs(oa1-ca1)*wa1 + abs(oa4-ca4)*wa4 + abs(oa5-ca5)*wa5 + abs(od1-cd1)*wd1 + abs(od2-cd2)*wd2 + abs(od3-cd3)*wd3
def smarterSearch(dx,dy,dz,od1,od2,od3,oa1,oa4,oa5,d6,wa1,wa4,wa5,wd1,wd2,wd3):
    # Current Values
    a1=oa1
    a4=oa4
    a5=oa5
    d1=od1
    d2=od2
    d3=od3

    # speed
    bestcost=999999999999
    for j in range(10000):
        x,y,z=getPos(a1,a4,a5,d1,d2,d3,d6)
        out = dumbSearch(dx,dy,dz,0,random.random()*2,random.random()*2,random.random()*pi*2,random.random()*pi*2,random.random()*pi*2,d6)
        if out:
            (ca1,ca4,ca5,cd1,cd2,cd3) = out
            c=cost(oa1,oa4,oa5,od1,od2,od3,ca1,ca4,ca5,cd1,cd2,cd3,wa1,wa4,wa5,wd1,wd2,wd3)
            if c<bestcost:
                bestcost=c
                a1=ca1
                a4=ca4
                a5=ca5
                d1=cd1
                d2=cd2
                d3=cd3
    print("Cost:",cost(oa1,oa4,oa5,od1,od2,od3,a1,a4,a5,d1,d2,d3,wa1,wa4,wa5,wd1,wd2,wd3))
    return (a1,a4,a5,d1,d2,d3)

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
    out=dumbSearch(dx,dy,dz,od1,od2,od3,oa1,oa4,oa5,d6)
    print("Part A")
    print("a1: {0}, a4: {1}, a5: {2}, d1: {3}, d2: {4}, d3: {5}".format(*out))

def partB():
    # Destination
    dx=1.2
    dy=.8
    dz=.5

    # Adjustable
    od1=0
    od2=.2
    od3=.3
    oa1=0
    oa4=-90*pi/180
    oa5=90*pi/180
    oa6=40*pi/180 # This one doesn't matter for position

    # Constants
    d6=.2
    print("Part B")
    out=smarterSearch(dx,dy,dz,od1,od2,od3,oa1,oa4,oa5,d6,1,1,1,0,1,1)
    print("a1: {0}, a4: {1}, a5: {2}, d1: {3}, d2: {4}, d3: {5}".format(*out))

def partC():
    # Destination
    dx=1.2
    dy=.8
    dz=.5

    # Adjustable
    od1=0
    od2=.2
    od3=.3
    oa1=0
    oa4=-90*pi/180
    oa5=90*pi/180
    oa6=40*pi/180 # This one doesn't matter for position

    # Constants
    d6=.2
    print("Part C")
    out=smarterSearch(dx,dy,dz,od1,od2,od3,oa1,oa4,oa5,d6,3,1,1,0,2,2)
    print("a1: {0}, a4: {1}, a5: {2}, d1: {3}, d2: {4}, d3: {5}".format(*out))

partA()
partB()
partC()
