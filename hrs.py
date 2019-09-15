#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Find hours minutes and seconds in given number number of seconds 

sec = 899008

hours = sec // 3600

remainsec = sec % 3600

minutes = remainsec // 60

secsnow = remainsec % 60

print("the number of hours are:", hours,"the number of minutes are:", minutes, "the number of secs are:", secsnow)


# In[ ]:




