#!/usr/bin/env python
# coding: utf-8

# 1.Write a function so that the columns of the output matrix are powers of the input
# vector.
# The order of the powers is determined by the increasing boolean argument. Specifically,
# when increasing is False, the i-th output column is the input vector raised element-wise
# to the power of N - i - 1.

# In[1]:


import numpy as np


# In[2]:


x = np.array([1, 2, 3, 5])


# In[3]:


N = 3


# In[4]:


np.vander(x, N)


# In[5]:


np.vander(x, increasing=False)


# In[6]:


np.vander(x, increasing=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




