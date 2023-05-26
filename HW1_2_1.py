import matplotlib.pyplot as plt
import numpy as np
from numpy import random
###################
np.random.seed(4)
x1 = random.normal(loc=2, scale=1, size=(100,1))
y1 = random.normal(loc=1, scale=0.1, size=(100,1))
xy1 = np.concatenate((x1, y1),axis=1)
###################
np.random.seed(4)
x2 = random.normal(loc=-1, scale=0.4, size=(20,1))
y2 = random.normal(loc=2, scale=0.4, size=(20,1))
xy2 = np.concatenate((x2, y2),axis=1)
###################
###################
dataset = np.concatenate((xy1,xy2), axis=0)
###################
w1 = 0
w2 = 0
b = 0
a = 0.0022
##################
error = []
l = 0
while (True):
    error_list = []
    error_sum = 0
    for i in range(120):
        if i < 100:
            t = -1
        else:
            t = 1
        x11 = dataset[i, 0]
        y11 = dataset[i, 1]
        net = (x11*w1)+(y11*w2)+b
        cost_function = 0.5*((t-net)**2)
        error_list.append(cost_function)
        error_sum = error_sum + cost_function
        w1 = w1 + (a * (t - net) * x11)
        w2 = w2 + (a * (t - net) * y11)
        b = b + (a * (t - net))
    l = l+1
    error.append(error_sum)
    print(max(error_list))
    if (max(error_list))<0.5:
        break
print(l)
##############
xpoint1 = -1
ypoint1 = (((-1) * w1 * xpoint1) -(b))/w2
xpoint2 = 3
ypoint2 = (((-1) * w1 * xpoint2) -(b))/w2
xpoints = np.array([xpoint1,xpoint2])
ypoints = np.array([ypoint1,ypoint2])
plt.plot(xpoints , ypoints)
plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.plot(error)
plt.show()
