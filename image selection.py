import os
import random
filelist=os.listdir('C:\\Users\\Rohith Reddy\\Pictures\\tongue')
count = 0
for fichier in filelist[:]:
    if not(fichier.endswith(".jpg")):
        filelist.remove(fichier)
        count += 1
num =[]
n = len(filelist)
for i in range(0, int(n*0.8)):
    num.append(int(random.uniform(0, n)))





print(filelist)