# Poisson Distribution
import cmath
import random
import math
import matplotlib.pyplot as plt
n = int(input("Enter n value: "))
lam = float(input("Enter the lamda value: "))
y =[]
ans = []
for i in range(0,n):
    x = random.randint(0,100)
    y.append(x)
y.sort()
for i in range(0,n):
    ans1 = ((lam** y[i]) * (cmath.e**(-1*lam)))/ math.factorial(int(y[i]))
    ans.append(ans1)
plt.plot(y,ans)
plt.show()