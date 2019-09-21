#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Time on your clock after

c = int(input('Please enter the time on your 24HR clock: '))

w = int(input('Please enter the wait time to ring the alarm: '))

t = (c + w) % 24

print('Time on your clock after wait time of:', w, 'would be: ','' ,t)




# In[ ]:




