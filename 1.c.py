# Exponential Distribution
import random
import cmath
import matplotlib.pyplot as plt
n = int( input("Enter n value "))
lam = int(input("Enter lamda"))
y = []
ans =[]
for i in range(0,n):
    x = random.uniform(-3,3)
    y.append(x)
y.sort()
for i in range(0,n):
    temp =  lam * (cmath.e**(-1*(lam*y[i])))
    ans.append(temp)
plt.plot(y,ans)
plt.show()
