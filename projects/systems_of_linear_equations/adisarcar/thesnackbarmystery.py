import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2,3],[3,2]])

B = np.array([37,38])
print(np.linalg.solve(A,B))

x_1 = np.linspace(0,10,100)
y_1 = 37/3 - 2*(x_1)/3 #equation converted so that y is expressed in terms of x
plt.plot(x_1,y_1,color='green')

x_2 = np.linspace(0,10,100)
y_2 = -1.5*x_2+19
plt.plot(x_2,y_2,color='red')

plt.plot(8,7,marker='o',markersize = 20, color='blue')