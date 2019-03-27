import csv
import random
import numpy as np
mat =[]
with open("ionosphere.csv.txt", 'r') as csvfile:
 reader = csv.reader(csvfile)
 for row in reader:
    mat.append(row)
print(len(mat))
sa = []
for i in range(0, len(mat)):
    mat[i].pop()
n = len(mat)
d = len(mat[1])
meana=[]
# for i in range(0,n):
#     sum = 0
#     for j in range(0,d):
#         sum += float(mat[i][j])
#     meana.append(sum/n)
# print(meana)
for i in range(0, d):
    sa.append([])
    temp = 0
    for j in range(0, n):
        sa[i].append(0)
        sa[i][j] = float(mat[j][i])


for i in range(0, d):
    temp = 0
    for j in range(0, n):
        temp = temp + float(sa[i][j])
    temp = temp/n
    meana.append(temp)

seco = []
for i in range(0, d):
    seco.append([])
    for j in range(0, n):
        seco[i].append(0)
        seco[i][j] = sa[i][j]-meana[i]



ansa=[]

for i in range(0, d):
    ansa.append([])
    for j in range(0, d):
        tema = np.array(seco[i])
        temb = np.array(seco[j])
        temb = np.transpose(temb)
        ans1=np.dot(tema, temb)
        ans1 = ans1/(n-1)
        ansa[i].append(0)
        ansa[i][j] = ans1
print(ansa[1])
pee = np.linalg.eigvals(ansa)
print(pee)
count = 0
#pee.sort()
#print(pee)
lamda = max(pee)


xmat = []
for i in range(0, d):
    xmat.append([])
    for j in range(0, d):
        if i == j:
            xmat[i].append(lamda)
        else:
            xmat[i].append(0)
print(xmat)
ei = np.subtract(ansa, xmat)
b = []
for i in range (0,n):
    b.append(0)
answ = np.linalg.tensorsolve(ei,b)
print(answ)
# mat = []
# for i in range(0,d):
#     mat.append([])
#     for j in range(0,n):
#         mat.append(0)
#         mat[i][j]=input()