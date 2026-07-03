import numpy as np
import matplotlib.pyplot as plt

def shear(k): 
    return np.array([[1, k],
                     [0, 1]])
    print("Determinant:" + str(np.linalg.det(np.array([[1, k],
                     [0, 1]]))))

stemF = np.array([np.zeros(100),np.linspace(0,2,100)])
topFLine = np.array([np.linspace(0,1.3,100),np.full(100,2)])
bottomFLine = np.array([np.linspace(0,1,100),np.full(100,1)])
plt.plot(stemF[0],stemF[1],color='green')
plt.plot(topFLine[0],topFLine[1],color='green')
plt.plot(bottomFLine[0],bottomFLine[1],color='green')
n = 0.5
shearedStemF = shear(n) @ stemF
shearedTopFLine = shear(n) @ topFLine
shearedBottomFLine = shear(n) @ bottomFLine
plt.plot(shearedStemF[0],shearedStemF[1],color='red')
plt.plot(shearedTopFLine[0],shearedTopFLine[1],color='red')
plt.plot(shearedBottomFLine[0],shearedBottomFLine[1],color='red')
plt.gca().set_aspect('equal')
plt.show()