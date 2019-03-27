import random
import cmath
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
n = int(input("Enter n value: "))
x1 = []
x2 = []
for i in range(0,n):
    x1.append(random.uniform(-3,3))
    x2.append(random.uniform(-3,3))
sum1 = 0
sum2 = 0
for i in range(0,n):
    sum1 = sum1 + x1[i]
    sum2 = sum2 + x2[i]

mean1 = sum1/(n)
mean2 = sum2/n

var1=0
var2=0
for i in range(0,n):
    var1 = var1 + ((x1[i]-mean1) * (x1[i]-mean1))
    var2 = var2 + ((x2[i] - mean2) * (x2[i] - mean2))
var1 = var1/(n-1)
var2 = var2/ (n-1)

cove = 0
for i in range(0,n):
    cove = cove + ((x1[i] - mean1)*(x2[i] - mean2))
cove = cove/n-1

mat = np.array([[var1,cove],[cove,var2]])
#print(mat)
#print( np.transpose(mat))
dete = np.linalg.det(mat)
#print(dete)
ans1 = 1/ ((cmath.pi*2)*cmath.sqrt(np.linalg.det(mat)))
ans = []
for i in range(0,n):
    temp1 = np.array([x1[i]-mean1,x2[i]-mean2])
    temp1t = np.transpose(temp1)
    inverse = np.linalg.inv(mat)
    firstm = np.dot(temp1t,inverse)
    secondm = np.dot(firstm,temp1)
    #print(secondm)
    power = ((-0.5) * secondm)
    ans2 = cmath.e ** power
    anst = ans1 * ans2
    ans.append(anst)
    print(anst)
#plt()
#print(temp1t)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1, x2, ans)
plt.show()