from turtle import width
import matplotlib.pyplot as plt
from math import sin,cos,pi,ceil,atan,tan,sqrt

def drawPath(position,timestep):
    
    plt.plot([i[0] for i in position],[i[1] for i in position])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    plt.plot([i*timestep for i in range(len(position))],[i[3] for i in position],label="XVelocity")
    plt.plot([i*timestep for i in range(len(position))],[i[4] for i in position],label="YVelocity")
    plt.plot([i*timestep for i in range(len(position))],[i[2] for i in position],label="ThetaVelocity")
    plt.xlabel("Time")
    plt.ylabel("Velocities")
    plt.legend()
    plt.show()

class Robot:
    def __init__(self, width, length, dt):
        self.x, self.y, self.t, self.width, self.length, self.dt = 0, 0, 0, width, length, dt
        self.commands = []
        self.position = []
    
    
class Skid(Robot):
    def __init__(self, width, length, dt):
        super().__init__(width, length, dt)
    def step(self,left,right,time):
        for i in range(round(time/self.dt)):
            dx = -(right+left)/2*self.dt*sin(self.t)
            dy = (right+left)/2*self.dt*cos(self.t)
            dtheta = (right-left)*self.dt/self.width
            self.x+=dx
            self.y+=dy
            self.t+=dtheta
            self.position.append((self.x, self.y, dtheta/self.dt, dx/self.dt, dy/self.dt))
        self.commands.append((left, right, time))

class Ackermann(Robot):
    def __init__(self, width, length, dt):
        super().__init__(width, length, dt)
    def step(self,alpha,velocity,time):
        for i in range(round(time/self.dt)):
            dx = -velocity*self.dt*sin(self.t)
            dy = velocity*self.dt*cos(self.t)
            dtheta = velocity/self.length*self.dt*tan(alpha)
            self.x+=dx
            self.y+=dy
            self.t+=dtheta
            self.position.append((self.x, self.y, dtheta/self.dt, dx/self.dt, dy/self.dt))
        self.commands.append((alpha, velocity, time))


def partA():
    # Constants / setup
    timestep = 0.1
    speed = 8
    width = .55
    length = .75
    v = Skid(width, length, timestep)

    # semi half diameter circle to get from the
    # middle to outside in correct orientation
    radius = 2.5/2
    time = (pi*radius/speed)

    # These new formulas compute using speed and radius
    left = speed-width*speed/(2*radius)
    right= 2*speed-left
    v.step(left, right, time)

    # Full size circle all the way around
    radius = 2.5
    time = (2*pi*radius/speed)

    # These new formulas compute using speed and radius
    left = speed-width*speed/(2*radius)
    right= 2*speed-left
    v.step(left, right, time)

    # plot the output
    drawPath(v.position,timestep)
    print(v.commands)

def partB():
    # Constants / setup
    velocity = 8
    width = .55
    length = .75
    timestep = .1
    v = Ackermann(width, length, timestep)

    # semi half diameter circle to get from the
    # middle to outside in correct orientation
    radius = 2.5 / 2
    alpha = atan(length / radius)
    v.step(alpha, velocity, pi*radius/velocity)

    # Full size circle all the way around
    radius = 2.5
    alpha = atan(length / radius)
    v.step(alpha, velocity, 2*pi*radius/velocity)

    # plot the output
    drawPath(v.position,timestep)
    print(v.commands)


partA()
partB()