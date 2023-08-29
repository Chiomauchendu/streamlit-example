#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!")


# In[2]:


import numpy as np


# In[6]:


np.identity(3)


# In[20]:


import numpy as np
matrix=np.random.rand(3,3)
print("The numpy matrix of random values is :\n", matrix)


# In[42]:


import numpy as np
m=np.identity(3)
print(m)


# In[41]:


import numpy as np
a=np.random.rand(3,3)
print(a)


# In[24]:


import numpy as np
m=np.identity(3)
a=np.random.rand(3,3)
print("\nThe multiplication of the matrix is : ",np.multiply(m,a))


# In[34]:


import numpy as np
m=np.identity(3)
a=np.random.rand(3,3)
print(m + a)


# In[38]:


a.max(axis=0)


# In[37]:


a.max()
m.max()


# In[43]:


a<2


# In[44]:


a>2


# In[46]:


three_Dim_random=np.zeros((4,3,2))


# In[47]:


three_Dim_random


# In[48]:


three_Dim_random.shape


# In[ ]:




