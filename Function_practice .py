#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add_two(a,b):
    return a+b

print ( add_two(4,5))


# In[3]:


def add_two(a,b):
    return a+b

a = int (input("enter first num :") )
b = int (input("enter second num :") )

print (add_two(a,b))


# In[4]:


def add_two(a,b):
    return a+b

a = input("enter first name :") 
b = input("enter second name :") 

print (add_two(a,b))


# In[6]:


def last_char (name):
    return name [-1]
print (last_char ("Abdullah"))


# In[8]:


def odd_even(num):
    if num%2 ==0 :
        return "even"
    
    else :
        return "odd "
    
print (odd_even(10))


# In[ ]:


def bigger_num(a,b):
    if a>b :
        return a
    else :
        return b
    
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

print (bigger_num(num1 , num2))
# bigger= bigger_num(num1 , num2)

# print (f "{bigger} is greater")


# In[ ]:




