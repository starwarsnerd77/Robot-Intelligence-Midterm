from math import sin,cos,pi
def angle(t,g,l,p,c,F):
    return (g*sin(t)+cos(t)*((-F)/(c+p)))/(l*(4/3-(p*cos(t)**2)/(c+p)))
for i in range(144600,144610):
    print(angle(i/1000000,9.81,1,.2,4,6),i/1000000)
print("8.285 degrees")