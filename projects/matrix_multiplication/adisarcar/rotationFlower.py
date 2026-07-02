import numpy as np
import math
import matplotlib.pyplot as plt
phi = input("Enter the angle of rotation in degrees: ")
phi = np.radians(float(phi))
point = np.array([1,0]) 
def rot(phi): 
    return np.array([[np.cos(phi), -np.sin(phi)],
                     [np.sin(phi), np.cos(phi)]])
# writing the flower petals
theta = np.linspace(0,np.pi,200)
r = np.sin(2*theta)

x = r*np.cos(theta)
y= r*np.sin(theta)

petal = np.array([x,y])
plt.plot(petal[0],petal[1],color='green')
for i in range 8:
    rotatedPetal = rot(np.radians(i*45)) @ petal
    plt.plot(rotatedPetal[0],rotatedPetal[1],color='red')
plt.gca().set_aspect('equal')
plt.show()  
