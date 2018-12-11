#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import random
# 讀取資料
def readData():
  data = pd.read_csv("data_1.csv")
  return data

def get(a):
    total=0
    b=0
    for i in a:
        total+=data.loc[i-1,"Weights"]*(np.max(data.loc[i-1,"Process Time"]+b-data.loc[i-1,"Due Date"],0))
        b+=data.loc[i-1,"Process Time"]
    return total

data=readData()
q= [x for x in range(1,data.loc[:,"Jobs"].size+1)]
random.shuffle(q)
t=q[:]
solution_value=get(t)
solution_list=t[:]
a=[]
b=[]
tabu=[]
remove=[]
time=int(input("n:"))
tabu_size=int(input("tabu size:"))
for n in range(time):
    for i in range(data["Jobs"].size-1):
        tmp=t[i]
        t[i]=t[i+1]
        t[i+1]=tmp
        a.append(t)
        t=q[:]
    for i in a:
        b.append(get(i))
    for ta in tabu:
        for i in a:
            for j in range(0,3):
                if i[j]==ta[0] and i[j+1]==ta[1]:
                    remove.append(a.index(i))
    if len(a)==0:
        break
    for i in remove:
        a.remove(a[index])
        b.remove(b[index])
    if len(a)==0:
        break
    indexnum=min(b)
    index=b.index(indexnum)
    if indexnum<solution_value:
        solution_value=indexnum
        solution_list=a[index][:]
    if len(tabu)==tabu_size:
        tabu.remove(tabu[tabu_size-1])
        tabu.append([t[index],t[index+1]])
    else:
        tabu.append([t[index],t[index+1]])
    t=a[index][:]
    a=[]
    b=[]
    remove=[]
print(solution_value)
print(solution_list)


# In[12]:


print(get([1,2,3,4]))
print(get([1,2,4,3]))
print(get([1,3,2,4]))
print(get([1,3,4,2]))
print(get([1,4,2,3]))
print(get([1,4,3,2]))
print(get([2,1,3,4]))
print(get([2,1,4,3]))
print(get([2,3,1,4]))
print(get([2,3,4,1]))
print(get([2,4,1,3]))
print(get([2,4,3,1]))
print(get([3,1,2,4]))
print(get([3,1,4,2]))
print(get([3,2,1,4]))
print(get([3,2,4,1]))
print(get([3,4,2,1]))
print(get([3,4,1,2]))
print(get([4,1,2,3]))
print(get([4,1,3,2]))
print(get([4,2,1,3]))
print(get([4,2,3,1]))
print(get([4,3,1,2]))
print(get([4,3,2,1]))


# In[ ]:




