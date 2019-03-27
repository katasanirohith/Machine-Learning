import numpy as np
import cmath
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
n = int(input("Enter n value"))

count = 0

list1 = []
list2 = []
output = []
def fucn(p1,p2):
    count = 0
    a = np.array([[0.1, -0.08], [-0.08,0.2]])
    b = np.array([[0.1, 0], [0, 0.1]])
    at = np.transpose(a)
    ad = np.linalg.det(a)
    ai = np.linalg.inv(a)

    bt = np.transpose(b)
    bd = np.linalg.det(b)
    bi = np.linalg.inv(b)

    ans1 = 1/((cmath.pi*2)*(cmath.sqrt(ad)))
    ansb1 = 1/((cmath.pi*2)*(cmath.sqrt(bd)))
    while count<n:
        f = random.uniform(-3, 3)
        s = random.uniform(-3, 3)
        mat = np.array([f-1, s-1])
        mat2 = np.array([f-3, s-3])
        matt = np.transpose(mat)
        matt2 = np.transpose(mat2)
        ans2 = cmath.e ** ((-0.5) * ( np.dot(np.dot(matt, ai), mat)))
        ans2b = cmath.e ** ((-0.5) * (np.dot(np.dot(matt2, bi), mat2)))
        ansa = ans1 * ans2
        annsb = ansb1 * ans2b
        ans = (p1*ansa) + (p2*annsb)
        if ans.real > 0.00008 :
            list1.append(f)
            list2.append(s)
            output.append(ans.real)
            count+=1
   # plt.plot(list1, list2)
    #plt.show()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(list1, list2, output)
    plt.show()
fucn(0.5,0.5)
fucn(0.85,0.15)




