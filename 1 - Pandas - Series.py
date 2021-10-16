#!/usr/bin/env python
# coding: utf-8

# ![rmotr](https://user-images.githubusercontent.com/7065401/52071918-bda15380-2562-11e9-828c-7f95297e4a82.png)
# <hr style="margin-bottom: 40px;">
# 
# <img src="https://user-images.githubusercontent.com/7065401/75165824-badf4680-5701-11ea-9c5b-5475b0a33abf.png"
#     style="width:300px; float: right; margin: 0 40px 40px 40px;"></img>
# 
# # Pandas - Series
# 

# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Hands on! 

# In[1]:


import pandas as pd
import numpy as np


# ## Pandas Series
# 
# We'll start analyzing "[The Group of Seven](https://en.wikipedia.org/wiki/Group_of_Seven)". Which is a political formed by Canada, France, Germany, Italy, Japan, the United Kingdom and the United States. We'll start by analyzing population, and for that, we'll use a `pandas.Series` object.

# In[2]:


# In millions
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])


# In[5]:


import pandas as pd
import numpy as np

g7_pop


# Someone might not know we're representing population in millions of inhabitants. Series can have a `name`, to better document the purpose of the Series:

# In[6]:


import pandas as pd
import numpy as np
g7_pop.name = 'G7 Population in millions'


# In[5]:


g7_pop


# Series are pretty similar to numpy arrays:

# In[6]:


g7_pop.dtype


# In[7]:


g7_pop.values


# They're actually backed by numpy arrays:

# In[8]:


type(g7_pop.values)


# And they _look_ like simple Python lists or Numpy Arrays. But they're actually more similar to Python `dict`s.
# 
# A Series has an `index`, that's similar to the automatic index assigned to Python's lists:

# In[9]:


g7_pop


# In[10]:


g7_pop[0]


# In[11]:


g7_pop[1]


# In[12]:


g7_pop.index


# In[13]:


l = ['a', 'b', 'c']


# But, in contrast to lists, we can explicitly define the index:

# In[14]:


g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]


# In[15]:


g7_pop


# Compare it with the [following table](https://docs.google.com/spreadsheets/d/1IlorV2-Oh9Da1JAZ7weVw86PQrQydSMp-ydVMH135iI/edit?usp=sharing): 
# 
# <img width="350" src="https://user-images.githubusercontent.com/872296/38149656-b5ce9816-3431-11e8-88e4-195756e25355.png" />
# 
# We can say that Series look like "ordered dictionaries". We can actually create Series out of dictionaries:

# In[16]:


pd.Series({
    'Canada': 35.467,
    'France': 63.951,
    'Germany': 80.94,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name='G7 Population in millions')


# In[17]:


pd.Series(
    [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom',
       'United States'],
    name='G7 Population in millions')


# You can also create Series out of other series, specifying indexes:

# In[18]:


pd.Series(g7_pop, index=['France', 'Germany', 'Italy', 'Spain'])


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ## Indexing
# 
# Indexing works similarly to lists and dictionaries, you use the **index** of the element you're looking for:

# In[19]:


g7_pop


# In[20]:


g7_pop['Canada']


# In[21]:


g7_pop['Japan']


# Numeric positions can also be used, with the `iloc` attribute:

# In[22]:


g7_pop.iloc[0]


# In[23]:


g7_pop.iloc[-1]


# Selecting multiple elements at once:

# In[24]:


g7_pop[['Italy', 'France']]


# _(The result is another Series)_

# In[25]:


g7_pop.iloc[[0, 1]]


# Slicing also works, but **important**, in Pandas, the upper limit is also included:

# In[28]:


g7_pop['Canada': 'Italy']


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ## Conditional selection (boolean arrays)
# 
# The same boolean array techniques we saw applied to numpy arrays can be used for Pandas `Series`:

# In[31]:


g7_pop


# In[32]:


g7_pop > 70


# In[33]:


g7_pop[g7_pop > 70]


# In[34]:


g7_pop.mean()


# In[35]:


g7_pop[g7_pop > g7_pop.mean()]


# In[ ]:


g7_pop.std()


# In[ ]:


~ not
| or
& and


# In[ ]:


g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ## Operations and methods
# Series also support vectorized operations and aggregation functions as Numpy:

# In[29]:


g7_pop


# In[30]:


g7_pop * 1_000_000


# In[36]:


g7_pop.mean()


# In[37]:


np.log(g7_pop)


# In[38]:


g7_pop['France': 'Italy'].mean()


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ## Boolean arrays
# (Work in the same way as numpy)

# In[39]:


g7_pop


# In[40]:


g7_pop > 80


# In[41]:


g7_pop[g7_pop > 80]


# In[42]:


g7_pop[(g7_pop > 80) | (g7_pop < 40)]


# In[43]:


g7_pop[(g7_pop > 80) & (g7_pop < 200)]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ## Modifying series
# 

# In[44]:


g7_pop['Canada'] = 40.5


# In[45]:


g7_pop


# In[46]:


g7_pop.iloc[-1] = 500


# In[47]:


g7_pop


# In[48]:


g7_pop[g7_pop < 70]


# In[49]:


g7_pop[g7_pop < 70] = 99.99


# In[50]:


g7_pop


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
