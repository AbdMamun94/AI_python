#!/usr/bin/env python
# coding: utf-8

# ![rmotr](https://user-images.githubusercontent.com/7065401/52071918-bda15380-2562-11e9-828c-7f95297e4a82.png)
# <hr style="margin-bottom: 40px;">
# 
# # NumPy exercises
# 

# In[ ]:


# Import the numpy package under the name np
import numpy as np

# Print the numpy version and the configuration
print(np.__version__)


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Array creation

# ### Create a numpy array of size 10, filled with zeros.

# In[ ]:


# your code goes here


# In[2]:


#np.array([0] * 10)
import numpy as np
np.zeros(10)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array with values ranging from 10 to 49

# In[ ]:


# your code goes here


# In[3]:


np.arange(10,50)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy matrix of 2*2 integers, filled with ones.

# In[ ]:


# your code goes here


# In[5]:


np.ones([2,2])


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy matrix of 3*2 float numbers, filled with ones.

# In[ ]:


# your code goes here


# In[6]:


np.ones([3,2])


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.

# In[ ]:


# your code goes here


# In[7]:


X = np.arange(4, dtype=np.int)

np.ones_like(X)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with zeros.

# In[ ]:


# your code goes here


# In[8]:


X = np.array([[1,2,3], [4,5,6]], dtype=np.int)

np.zeros_like(X)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy matrix of 4*4 integers, filled with fives.

# In[ ]:


# your code goes here


# In[9]:


np.ones([4,4], dtype=np.int) * 5 


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens.

# In[ ]:


# your code goes here


# In[12]:


X = np.array([[2,3], [6,2]], dtype=np.int)

np.ones_like(X) * 7     # one_like


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere.

# In[ ]:


# your code goes here


# In[13]:


#np.eye(3)
np.identity(3)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array, filled with 3 random integer values between 1 and 10.

# In[ ]:


# your code goes here


# In[21]:


np.random.randint(10, size=3)  # random.randint  = random int num ney


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a 3\*3\*3 numpy matrix, filled with random float values.

# In[ ]:


# your code goes here


# In[22]:


#np.random.random((3,3,3)) 

np.random.randn(3,3,3)  # random.randin =  USE FOR RANDOM FLOAT NUMBER:

# 0 to 1 floats


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X python list convert it to an Y numpy array

# In[ ]:


# your code goes here


# In[27]:


X = [1, 2, 3]

print(X ,type(X))

Y = np.array(X)

print(Y, type(Y))                    # different type


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, make a copy and store it on Y.

# In[ ]:


# your code goes here


# In[28]:


X = np.array([5,2,3], dtype=np.int)

print(X, id(X))

Y = np.copy(X)         # np.copy () COPY KORAR JONNO.

print(Y, id(Y)) # different id


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array with numbers from 1 to 10

# In[ ]:


# your code goes here


# In[29]:


np.arange(1, 11)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array with the odd numbers between 1 to 10

# In[ ]:


# your code goes here


# In[30]:


np.arange(1, 11, 2)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array with numbers from 1 to 10, in descending order.

# In[ ]:


# your code goes here


# In[31]:


np.arange(1, 11)[::-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a 3*3 numpy matrix, filled with values ranging from 0 to 8

# In[ ]:


# your code goes here


# In[32]:


np.arange(9).reshape(3,3)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Show the memory size of the given Z numpy matrix

# In[ ]:


# your code goes here


# In[33]:


Z = np.zeros((10,10))

print("%d bytes" % (Z.size * Z.itemsize))


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Array indexation
# 

# ### Given the X numpy array, show it's first element

# In[ ]:


# your code goes here


# In[34]:


X = np.array(['A','B','C','D','E'])

X[0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show it's last element

# In[ ]:


# your code goes here


# In[35]:


X = np.array(['A','B','C','D','E'])

#X[len(X)-1]

X[-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show it's first three elements

# In[ ]:


# your code goes here


# In[36]:


X = np.array(['A','B','C','D','E'])

X[0:3] # remember! elements start at zero index


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show all middle elements

# In[ ]:


# your code goes here


# In[37]:


X = np.array(['A','B','C','D','E'])

X[1:-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show the elements in reverse position

# In[ ]:


# your code goes here


# In[38]:


X = np.array(['A','B','C','D','E'])


X[::-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show the elements in an odd position

# In[ ]:


# your code goes here


# In[40]:


X = np.array(['A','B','C','D','E'])


#X[[0, 2, -1]]

X[::2]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the first row elements

# In[ ]:


# your code goes here


# In[41]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X[0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the last row elements

# In[ ]:


# your code goes here


# In[44]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X[-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the first element on first row

# In[ ]:


# your code goes here


# In[45]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

#X[0][0]

X[0, 0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the last element on last row

# In[ ]:


# your code goes here


# In[46]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

#X[-1][-1]

X[-1, -1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the middle row elements

# In[ ]:


# your code goes here


# In[47]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

#X[1:-1][1:-1] wrong!

X[1:-1, 1:-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the first two elements on the first two rows

# In[ ]:


# your code goes here


# In[48]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

#X[:2][:2] wrong!

#X[0:2, 0:2]

X[:2, :2]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the last two elements on the last two rows

# In[ ]:


# your code goes here


# In[49]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X[2:, 2:]


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Array manipulation
# 

# ### Convert the given integer numpy array to float

# In[ ]:


# your code goes here


# In[50]:


X = [-5, -3, 0, 10, 40]


np.array(X, np.float)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Reverse the given numpy array (first element becomes last)

# In[ ]:


# your code goes here


# In[51]:


X = [-5, -3, 0, 10, 40]

X[::-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Order (sort) the given numpy array

# In[ ]:


# your code goes here


# In[52]:


X = [0, 10, -5, 40, -3]

X.sort()

X


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, set the fifth element equal to 1

# In[ ]:


# your code goes here


# In[55]:


X = np.zeros(10)

X[4] = 1
X


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, change the 50 with a 40

# In[ ]:


# your code goes here


# In[56]:


X = np.array([10, 20, 30, 50])

X[3] = 40
X


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, change the last row with all 1

# In[ ]:


# your code goes here


# In[57]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X[-1] = np.array([1, 1, 1, 1])
X


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, change the last item on the last row with a 0

# In[ ]:


# your code goes here


# In[58]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X[-1, -1] = 0

X


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, add 5 to every element

# In[ ]:


# your code goes here


# In[59]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X + 5


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Boolean arrays _(also called masks)_
# 

# ### Given the X numpy array, make a mask showing negative elements

# In[ ]:


# your code goes here


# In[60]:


X = np.array([-1,2,0,-4,5,6,0,0,-9,10])

mask = X <= 0

mask


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, get the negative elements

# In[ ]:


# your code goes here


# In[61]:


X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])

mask = X <= 0

X[mask]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, get numbers higher than 5

# In[ ]:


# your code goes here


# In[62]:


X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])

mask = X > 5

X[mask]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, get numbers higher than the elements mean

# In[ ]:


# your code goes here


# In[71]:


X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])

mask = X > X.mean()
# mean mane hoche ( -1+2+0-4+5+6+0-9+10 / 10 )
X[mask]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, get numbers equal to 2 or 10

# In[ ]:


# your code goes here


# In[72]:


X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])

mask = (X == 2) | (X == 10)

X[mask]


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Logic functions
# 

# ### Given the X numpy array, return True if none of its elements is zero

# In[ ]:


# your code goes here


# In[73]:


X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])

X.all()    # TRUE OR FALSE CECK KORE 


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, return True if any of its elements is zero

# In[ ]:


# your code goes here


# In[74]:


X = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])

X.any()


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Summary statistics

# ### Given the X numpy array, show the sum of its elements

# In[ ]:


# your code goes here


# In[75]:


X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])

#np.sum(X)

X.sum()


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show the mean value of its elements

# In[ ]:


# your code goes here


# In[76]:


X = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])

#np.mean(X)

X.mean()


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the sum of its columns

# In[ ]:


# your code goes here


# In[77]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X.sum(axis=0)            # remember: axis=0 columns; axis=1 rows


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the mean value of its rows

# In[ ]:


# your code goes here


# In[78]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

X.mean(axis=1)       # remember: axis=0 columns; axis=1 rows


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show the max value of its elements

# In[ ]:


# your code goes here


# In[79]:


X = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])

#np.max(X)


X.max()


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
