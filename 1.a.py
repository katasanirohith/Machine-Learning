# Normal Distribution
import random
import cmath
import matplotlib.pyplot as plt
n = int(input("Enter n value"))
sum = 0
x = []
for i in range(0,n):
    x.append( random.uniform(-3 , 3))
    sum += int(x[i])
x.sort()
mean = sum/n
print("mean=", mean)
arr = []
var = []
var = 0
for i in range (0, n):
    var += (x[i] - mean) * (x[i] - mean)
var = var/(n-1)
print("var = ", var)
ans1 = 1 /(cmath.sqrt(2*cmath.pi)*cmath.sqrt(var))
answ=[]
for i in range(0,n):
     ans2 = cmath.e ** (-1*(((x[i]-mean) * (x[i] - mean))/(2*(var))))
     ans = ans1*ans2
     print(ans)
     answ.append(ans)
plt.plot(x,answ)
plt.show()

