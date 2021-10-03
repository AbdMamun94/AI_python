#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


a = [1,2,3]


# In[22]:


b = [5,3,4]


# In[23]:


u = np.array(b) 


# In[24]:


u+u


# In[18]:


v=np.array(a) # most important line


# In[13]:


v+v


# In[11]:


a+a


# In[ ]:


v = np.array([1,2,3,123,145,156,1789,174764894,137648239])


# In[14]:


v.size


# In[15]:


np.linalg.norm(v)


# In[ ]:


v = np.array([1,2,3])


# In[ ]:


u = np.array([4,5,6])


# In[25]:


np.dot (v,u)


# In[26]:


u


# In[27]:


v


# In[29]:


dot_product_uv = np.dot(u,v) # dot gunon hoiloo... 


# In[30]:


dot_product_uv


# In[31]:


norm_u = np.linalg.norm(u)


# In[32]:


norm_u


# In[33]:


norm_v = np.linalg.norm(v)


# In[34]:


norm_v


# In[35]:


cos_theta = dot_product_uv / (norm_u * norm_v)


# In[36]:


cos_theta


# In[37]:


np.arccos(cos_theta)


# In[38]:


np.pi


# In[ ]:


degrees = radians * 180/pi


# In[39]:


theta_degrees = np.arccos(cos_theta) * 180/ np.pi 


# In[41]:


theta_degrees


# In[ ]:


import matplotlib.pylot as plt


# In[66]:


from matplotlib import pyplot as plt


# In[70]:


u = np.array ([1,2])
v = np.array ([-4,1])
origin = np.array([0,0])
dot_product_uv = np.dot(u,v)
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
cos_theta = dot_product_uv / (norm_u*norm_v)

theta_radians = np.arccos(cos_theta)

theta_degrees =  np.arccos( cos_theta ) * 180/np.pi


# In[71]:


theta_degrees


# In[72]:


plt.quiver (origin,origin , u ,v , scale = 21)


# 2+2
# 

# In[ ]:





# In[ ]:




