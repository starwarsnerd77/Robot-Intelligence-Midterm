from turtle import width
import matplotlib.pyplot as plt
from math import sin,cos,pi,ceil,atan,tan
# 1. (20 points) Moving in a car
# I would like you to use a skid steer model of a robot that is 75cm long and 55cm wide and
# run a few simple experiments with it. Please upload your resulting figures and python
# (or other) code:
# (a) (5 points) Make a list of commands (at t=0.1) that will allow this robot to traverse
# along the edge of a 5m diameter circle. The robot starts off in the center of the
# circle (0,0), and you cannot leave the circle’s border. Plot both the resulting path
# (x, y) and trajectory (x, y, and angular velocities). Assume a constant velocity of
# 8m/s
# (b) (5 points) Do the same as the above for a traditional car (Ackermann steering).
# (c) (10 points) Your Ackermann vehicle (with the same dimensions as described for the
# skid steer), is driving on a circle of radius 2.5m. Assume that you begin on the edge
# of the circle. Calculate the positional error with our computational approximation
# using the forward Euler method, as referred to in the course notes and illustrated
# in Reading 2, eq. 1.6. Graph the errors and computing time for three different
# time-steps (∆t = 1, 0.1, 0.01), error is defined as the absolute distance between the
# expected (from equations) to real x, y position (defined analytically) over time.
# Brief notes on what this problem is about: Imagine that you are moving a semi-truck
# and you have GPS positions (somewhat accurate) and an internal prediction model.
# We want the internal models to be updated based on ”ground truth” information
# to build better estimates of the vehicle motion over time.
# (d) (10 points) Graduate Student Question Compute part c again where road frictions are much lower (due to rain or ice). Slip causes your tires to respond very
# differently. Assume that your theta is θactual = θ(1 − 0.08) and velocity is vactual =
# v(1 − 0.04)
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 5])
# plt.ylabel('some numbers')
# plt.show()
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
    v = Skid(.55, .75, .1)
    radius = -2.5
    right = 1
    rs = .05
    left = -(v.width*right-2*radius*right)/(v.width+2*radius)
    v.step(1,1,2.5)
    v.step(rs,-rs,pi/2*v.width/(2*rs))
    v.step(left,right,100)
    drawPath(v.position)
    print(v.commands)

def partB():
    radius, width, length = .55, .75, 2.5
    alpha = atan(length/radius)
    v=Ackermann(width,length,.1)
    v.step(0,1,2.5)
    v.step(alpha,1,100)
    drawPath(v.position)
    print(v.commands)

partA()
partB()


        
# def partA():
#     v = Skid(.3,.1)
#     v.step(1,1.5,5)
#     v.step(-1,-1.5,3)
#     v.step(.8,-2,8)
#     v.step(2,2,10)
#     drawPath(v.position)

# def partB():
#     v = Skid(w:=.3,.1)
#     rs = .05
#     for i in range(ceil(5/w/2)):
#         v.step(1,1,5)
#         v.step(rs,-rs,pi/2*w/(2*rs))
#         v.step(1,1,w)
#         v.step(rs,-rs,pi/2*w/(2*rs))
#         v.step(1,1,5)
#         v.step(-rs,rs,pi/2*w/(2*rs))
#         v.step(1,1,w)
#         v.step(-rs,rs,pi/2*w/(2*rs))
#     [print(f"{i} ") for i in v.commands]
#     drawPath(v.position)
    

# def partC():
#     v = SwedishFish(.1)
#     w = .3
#     for i in range(ceil(5/w/2)):
#         v.step(0 , 5)
#         v.step(3*pi/2, w*10,.1)
#         v.step(pi, 5)
#         v.step(3*pi/2, w*10,.1)
#     [print(f"{i} ") for i in v.commands]
#     drawPath(v.position)