#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Time on your clock after

current_time = int(input('Please enter the time on your 24HR clock: '))

wait_time = int(input('Please enter the wait time to ring the alarm: '))

t = (current_time + wait_time) % 24

print('Time on your clock after wait time of:', wait_time, 'would be: ','' ,t)




# In[ ]:




