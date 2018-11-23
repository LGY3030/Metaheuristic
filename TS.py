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


# In[4]:


import numpy as np
import pandas as pd


# In[5]:


# 讀取資料
def readData():
  data = pd.read_csv("data.csv")
  return data


# In[23]:


data=readData()
print(data.ix[:,"Jobs"])


# In[ ]:




