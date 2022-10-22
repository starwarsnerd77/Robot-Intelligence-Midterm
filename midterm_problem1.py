from turtle import width
import matplotlib.pyplot as plt
from math import sin,cos,pi,ceil,atan,tan

def drawPath(position):
    
    plt.plot([i[0] for i in position],[i[1] for i in position])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
    plt.plot([i[3] for i in position],label="XVelocity")
    plt.plot([i[4] for i in position],label="YVelocity")
    plt.plot([i[2] for i in position],label="ThetaVelocity")
    plt.xlabel("Timesteps")
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
            self.position.append((self.x, self.y, dtheta/self.dt, dx, dy))
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
            self.position.append((self.x, self.y, dtheta/self.dt, dx, dy))
        self.commands.append((alpha, velocity, time))


def partA():
    timestep = 0.1
    speed = 8
    width = .55
    length = .75
    radius = 2.225/2
    time = (pi*radius/speed)*1.1

    theta = speed * timestep / radius
    new_y = radius * sin(theta)
    rminl = theta * width
    rplusl = new_y * 2 / cos(theta)

    v = Skid(width, length, timestep)
    
    left = ((rplusl - rminl) / 2) * 10
    right = (rminl * 10) + left
    v.step(left, right, time)

    radius = 2.225
    time = (2*pi*radius/speed)*1.1

    theta = speed * timestep / radius
    new_y = radius * sin(theta)
    rminl = theta * width
    rplusl = new_y * 2 / cos(theta)
    
    left = ((rplusl - rminl) / 2) * 10
    right = (rminl * 10) + left

    v.step(left,right,time)
    drawPath(v.position)
    print(v.commands)

partA()