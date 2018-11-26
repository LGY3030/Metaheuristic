#!/usr/bin/env python
# coding: utf-8

# In[7]:


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


# In[8]:


import numpy as np
import pandas as pd
import random


# In[9]:


# 讀取資料
def readData():
  data = pd.read_csv("data.csv")
  return data


# In[10]:


data=readData()
print(data.loc[:,"Jobs"].size)


# In[32]:


def get(a):
    total=0
    b=0
    for i in a:
        total+=data.loc[i-1,"Weights"]*(np.max(data.loc[i-1,"Process Time"]+b-data.loc[i-1,"Due Date"],0))
        b+=data.loc[i-1,"Process Time"]
    return total


# In[33]:


solution=0
q= [x for x in range(1,data.loc[:,"Jobs"].size+1)]
random.shuffle(q)
t=q[:]
print(t)


# In[34]:


max=100000000
for i in range(data["Jobs"].size-1):
    tmp=t[i]
    t[i]=t[i+1]
    t[i+1]=tmp
    total=get(t)
    t=q[:]
    if max>total:
        max=total


# In[ ]:





# In[ ]:




