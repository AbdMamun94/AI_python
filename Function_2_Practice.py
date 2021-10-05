#!/usr/bin/env python
# coding: utf-8

# In[4]:


def bigger_num(a,b):
    if a>b :
        return a
    else :
        return b
    
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

#print (bigger_num(num1 , num2))
bigger= bigger_num(num1 , num2)

print (f"{bigger} is greater")


# In[5]:


def greatest (a,b,c):
    if a>b and a>c :
        return a
    
    elif b>a and b>c:
        return b
    else :
        return c
    
print(greatest (100,40,50))
 


# In[18]:


def is_palindrom(word) :
    reversed_word = word [ : :-1]
    if word == reversed_word :
         #return True
        #return "its palindrom" 
        print (" its palindrom ") 

    else : 
         #return False
        #return "its not palindrom"   # return er pore jodi kichu return korate icha hoy tahole " " use korte hobe 
        print (" its not palindrom ") # if or else er pore jodi print korate hoy tahole place focus rakhte hobe.
    
print( is_palindrom ( "madam" ) )
print( is_palindrom ( "shuvo" ) )


# In[27]:


#FIBONACCI SERIES

def fibonacci_seq (n) :
    a =0
    b =1
    if n == 1 :
        print (a)
    elif n == 2 :
        print (b)
        
    else :
        print ( a,b, end = " ")
        for i in range (n-2) :
            c = a + b
            a = b
            b = c
            print (b , end =" ")

fibonacci_seq (10)




# In[ ]:




