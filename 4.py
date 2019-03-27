import numpy as np
import cmath
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
n = int(input("Enter n value"))
count = 0
def fucn(x1, x2, x3, x4):
    list1 = []
    list2 = []
    output = []
    count = 0
    a = np.array([[x1, x2], [x3, x4]])
    at = np.transpose(a)
    ad = np.linalg.det(a)
    ai = np.linalg.inv(a)
    ans1 = 1/((cmath.pi*2)*(cmath.sqrt(ad)))
    while count<n:
        f = random.uniform(-3, 3)
        s = random.uniform(-3, 3)
        mat = np.array([f, s])
        matt = np.transpose(mat)
        ans2 = cmath.e ** ((-0.5) * ( np.dot(np.dot(matt,ai),mat)))
        ans = ans1 * ans2
        if ans.real > cons:
            list1.append(f)
            list2.append(s)
            output.append(ans.real)
            #print(ans)
            #print(count)
            count+=1
    plt.plot(list1, list2)
    plt.show()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(list1, list2, output)
    plt.show()
cons = 0.08
fucn(1, 0, 0, 1)
cons = 0.01
fucn(0.2, 0, 0, 0.2)
cons =0.08
fucn(0.2, 0, 0, 2)
fucn(2, 0, 0, 0.2)
fucn(1,0.5,0.5,1)
fucn(0.3,0.5,0.5,2)
fucn(0.3,-0.5,-0.5,2)
cons = 0.01
fucn(2, 0, 0, 2)
