#!/usr/bin/env python
# coding: utf-8

# In[3]:


total = 0 

for i in range (1,11) :
    total = total + i
print (total)


# In[4]:


num = input("Enter a number : ") #1234
total = 0

for i in range (0,len(num)) : # 0-1 ,1-2 , 2-3 , 3-4
                
    total = total + int(num[i])

print (total)


# In[6]:


# 1234 = 1+2+3+4 = 10
    
num = input("enter a number :") #1234
total = 0

for i in num :
    total = total + int(i)
    
print (total)


# In[ ]:




