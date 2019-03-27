import random
import numpy as np
n = int(input("Enter number of samples"))
d = int(input("Enter the dimension"))
sa = []
temp = 0
meana = []
for i in range(0, d):
    sa.append([])
    temp = 0
    for j in range(0,n):
        sa[i].append(0)
        sa[i][j]=random.uniform(-3,3)


for i in range(0,d):
    temp = 0
    for j in range (0,n):
        temp = temp + sa[i][j]
    temp = temp/n
    meana.append(temp)

seco = []
for i in range(0,d):
    seco.append([])
    for j in range(0,n):
        seco[i].append(0)
        seco[i][j] = sa[i][j]-meana[i]



ansa=[]

for i in range(0,d):
    ansa.append([])
    for j in range (0,d):
        tema=np.array(seco[i])
        temb=np.array(seco[j])
        temb=np.transpose(temb)
        ans1=np.dot(tema,temb)
        ans1 = ans1/(n-1)
        ansa[i].append(0)
        ansa[i][j]=ans1
print(ansa)