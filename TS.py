#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[22]:


import numpy as np
import pandas as pd
import random


# In[10]:


# 讀取資料
def readData():
  data = pd.read_csv("data.csv")
  return data


# In[14]:


data=readData()
print(data.loc[:,"Jobs"].size)


# In[66]:


def get(a):
    total=0
    b=0
    #for i in range(len(a)):
    b=a[i]
    total+=data.loc[b,"Weights"]*(np.max(data.loc[b,"Process Time"]-data.loc[b,"Due Date"],0))


# In[60]:


solution=0
q= [x for x in range(1,data.loc[:,"Jobs"].size+1)]
random.shuffle(q)
t=q[:]
print(t)
for i in range(5):
    print(i)


# In[61]:


for i in range(data.loc[:,"Jobs"].size-1):
    tmp=t[i]
    t[i]=t[i+1]
    t[i+1]=tmp
    b[i]=t[:]
    t=q[:]
    print(b[i])


# In[ ]:




