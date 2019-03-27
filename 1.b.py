# Uniform Distribution
import random
import matplotlib.pyplot as plt
n = int(input("Number of samples: "))
a = int(input("Enter a number between -3 and 6 a: "))
b = int(input("Enter a number between -3 and 6 b: "))
y = []
ans=[]
orgn = n
i=0
while(i<n):
    x = random.uniform(-3,6)
    #print(x)
    y.append(x)
    i+=1
    print(x)
y.sort()
for i in  range(0,orgn):
    if y[i]>a and y[i]<b:
        ans1=(1/(b-a))
    else:
        ans1=0
    ans.append(ans1)
    print(ans1)
plt.plot(y,ans)
plt.show()


