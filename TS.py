#!/usr/bin/env python
# coding: utf-8

# In[47]:


import numpy as np
import pandas as pd
import random
import time as tm

# function---讀取資料
def readData():
  data = pd.read_csv("data_1.csv")
  return data

# function---取得 total weighted tardiness 
def get(a):
    total=0
    b=0
    for i in a:
        total+=data.loc[i-1,"Weights"]*(np.max(data.loc[i-1,"Process Time"]+b-data.loc[i-1,"Due Date"],0))
        b+=data.loc[i-1,"Process Time"]
    return total


# 輸入n(迭代次數) 和 tabu size
time=int(input("n:"))
tabu_size=int(input("tabu size:"))

# 開始時間
start_time = tm.time()

# 讀取資料
data=readData() 

# 打亂資料, 讓資料隨機排列
q= [x for x in range(1,data.loc[:,"Jobs"].size+1)]
random.shuffle(q)

# t為目前的move
t=q[:]

# a為鄰近可行解
a=[]

# b為鄰近可行解的 total weighted tardiness
b=[]

# fa為a的固定list
fa=[]

# fb為b的固定list
fb=[]

# tabu list
tabu=[]

# 紀錄a和b中,與tabu list相抵觸而要被移除的解
removeindex=[]

# 初始的解,value和move
solution_value=get(t)
solution_list=t[:]

# 迭代n次
for n in range(time):
    
    # 把目前move的鄰近可行解加入a
    for i in range(data["Jobs"].size-1):
        tmp=t[i]
        t[i]=t[i+1]
        t[i+1]=tmp
        a.append(t)
        t=q[:]

    # 把目前move的鄰近可行解的 total weighted tardiness加入b
    for i in a:
        b.append(get(i))
        
    # 找出a中,與tabu list相抵觸而要被移除的解的index
    for ta in tabu:
        for i in a:
            for j in range(0,3):
                if i[j]==ta[0] and i[j+1]==ta[1]:
                    for k in removeindex:
                        if removeindex[k]!=a.index(i):
                            removeindex.append(a.index(i))
                    break
    # 將a和b複製到fa和fb
    fa=a[:]
    fb=b[:]
            
                    
    # 如果此時a裡面沒有解, 則結束搜尋
    if len(a)==0:
        break
    
    # 依照removeindex中的index, 刪除a和b
    for i in removeindex:
        a.remove(fa[i])
        b.remove(fb[i])
        
    # 如果此時a裡面沒有解了, 則結束搜尋
    if len(a)==0:
        break
    
    # 找出b裡最小的值, 並記錄index
    indexnum=min(b)
    index=b.index(indexnum)
    
    # 如果最小的值比原本的值小, 則原本的值=最小的值
    if indexnum<solution_value:
        solution_value=indexnum
        solution_list=a[index][:]
        
    # 調整tabu list的內容
    if len(tabu)==tabu_size:
        tabu.remove(tabu[tabu_size-1])
        tabu.append([t[index],t[index+1]])
    else:
        tabu.append([t[index],t[index+1]])
        
    # 將t存為最佳的鄰近解, 初始化a,b,fa,fb,removeindex
    t=a[index][:]
    a=[]
    b=[]
    fa=[]
    fb=[]
    removeindex=[]

# 結束時間
end_time = tm.time()    

# 總時間
total_time = end_time-start_time

# 印出結果
print("total weighted tardiness(approximate optimal solution): ",solution_value)
print("job sequence(approximate optimal solution): ",solution_list)
print("run time: ",total_time)


# In[1]:


import numpy as np
import pandas as pd
import random
import time as tm

# function---讀取資料
def readData():
  data = pd.read_csv("data_1.csv")
  return data

# function---取得 total weighted tardiness 
def get(a):
    total=0
    b=0
    for i in a:
        total+=data.loc[i-1,"Weights"]*(np.max(data.loc[i-1,"Process Time"]+b-data.loc[i-1,"Due Date"],0))
        b+=data.loc[i-1,"Process Time"]
    return total


# 讀取資料
data=readData() 

# 設定time(迭代次數) 和 tabu size
time=[100,200,300,400,500]
tabu_size=[1,2,3,4,5,6,7,8,9,10]

# 所有的最佳解
best_value=100000000
best_list=[]
best_n=0
best_size=0
best_time=0

# 跑不同的time(迭代次數) 和 tabu size
for x in time:
    
    for y in tabu_size:
        
         # 開始時間
        start_time = tm.time()

        # 打亂資料, 讓資料隨機排列
        q= [x for x in range(1,data.loc[:,"Jobs"].size+1)]
        random.shuffle(q)

        # t為目前的move
        t=q[:]

        # a為鄰近可行解
        a=[]

        # b為鄰近可行解的 total weighted tardiness
        b=[]

        # fa為a的固定list
        fa=[]

        # fb為b的固定list
        fb=[]
        
        # tabu list
        tabu=[]

        # 紀錄a和b中,與tabu list相抵觸而要被移除的解
        removeindex=[]

        # 初始的解,value和move
        solution_value=get(t)
        solution_list=t[:]
        
        # 迭代n次
        for n in range(x):
    
            # 把目前move的鄰近可行解加入a
            for i in range(data["Jobs"].size-1):
                tmp=t[i]
                t[i]=t[i+1]
                t[i+1]=tmp
                a.append(t)
                t=q[:]

            # 把目前move的鄰近可行解的 total weighted tardiness加入b
            for i in a:
                b.append(get(i))
        
            # 找出a中,與tabu list相抵觸而要被移除的解的index
            for ta in tabu:
                for i in a:
                    for j in range(0,19):
                        if i[j]==ta[0] and i[j+1]==ta[1]:
                            for k in removeindex:
                                if removeindex[k]!=a.index(i):
                                    removeindex.append(a.index(i))
                            break
            # 將a和b複製到fa和fb
            fa=a[:]
            fb=b[:]
            
            # 如果此時a裡面沒有解, 則結束搜尋
            if len(a)==0:
                break
    
            # 依照removeindex中的index, 刪除a和b
            for i in removeindex:
                a.remove(fa[i])
                b.remove(fb[i])
        
            # 如果此時a裡面沒有解了, 則結束搜尋
            if len(a)==0:
                break
    
            # 找出b裡最小的值, 並記錄index
            indexnum=min(b)
            index=b.index(indexnum)
    
            # 如果最小的值比原本的值小, 則原本的值=最小的值
            if indexnum<solution_value:
                solution_value=indexnum
                solution_list=a[index][:]
        
            # 調整tabu list的內容
            if len(tabu)==y:
                tabu.remove(tabu[y-1])
                tabu.append([t[index],t[index+1]])
            else:
                tabu.append([t[index],t[index+1]])
            # 將t存為最佳的鄰近解, 初始化a,b,fa,fb,removeindex
            t=a[index][:]
            a=[]
            b=[]
            fa=[]
            fb=[]
            removeindex=[]
        
        # 結束時間
        end_time = tm.time()    

        # 總時間
        total_time = end_time-start_time
        
        # 印出各結果
        print("迭代次數: ",x)
        print("tabu list size: ",y)
        print("total weighted tardiness(approximate optimal solution): ",solution_value)
        print("job sequence(approximate optimal solution): ",solution_list)
        print("run time: ",total_time)
        print("")
        
        # 取best
        if solution_value<best_value:
            best_value=solution_value
            best_list=solution_list
            best_n=x
            best_size=y
            best_time=total_time
print("")
print("最佳結果:")
print("迭代次數: ",best_n)
print("tabu list size: ",best_size)
print("total weighted tardiness(approximate optimal solution): ",best_value)
print("job sequence(approximate optimal solution): ",best_list)
print("run time: ",best_time)

        


# In[ ]:




