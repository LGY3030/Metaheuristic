#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
TS algorithm

k = 1
s = initial solution
WHILE the stopping condition is not met DO 
    Identify N(s). (Neighbourhood set) 
    Identify T(s,k). (Tabu set) 
    Identify A(s,k). (Aspirant set) 
    N(s,k) = {N(s) - T(s,k)} + A(s,k)
    Choose the best s’  in  N(s,k)
    Memorize s’ if it improves the previous best known solution
    s = s’. 
    k = k + 1
END WHILE
"""


# In[3]:


import numpy as np
import pandas as pd
import random


# In[4]:


# 讀取資料
def readData():
  data = pd.read_csv("data.csv")
  return data


# In[5]:


data=readData()
print(data.loc[:,"Jobs"].size)


# In[6]:


def get(a):
    total=0
    b=0
    for i in a:
        total+=data.loc[i-1,"Weights"]*(np.max(data.loc[i-1,"Process Time"]+b-data.loc[i-1,"Due Date"],0))
        b+=data.loc[i-1,"Process Time"]
    return total


# In[32]:


q= [x for x in range(1,data.loc[:,"Jobs"].size+1)]
random.shuffle(q)
t=q[:]
print(t)


# In[33]:


solution=get(t)
a=[]
b=[]
tabu=[]
remove=[]
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
        for j in range(0,4):
            if i[j]==ta[0] and i[j+1]==ta[1]:
                remove.append(a.index(i))
for i in remove:
    a.remove(a[index])
    b.remove(b[index])
print(max)
print(a)
print(b)
indexnum=min(b)
index=b.index(indexnum)
if len(tabu)==2:
    tabu.remove(tabu[1])
    tabu.append([t[index],t[index+1]])
else:
    tabu.append([t[index],t[index+1]])
print(tabu)
t=a[index]


# In[ ]:





# In[ ]:




