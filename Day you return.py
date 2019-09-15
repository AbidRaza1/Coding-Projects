#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Day you will return



calender = print('Calendar days:','Sudnay-Saturday:', '0-6')

day = int(input('Please enter number of day you are planning to leave from calender '))

length = int(input('How long would you like to stay(No.of days) '))

t = (day + length) % 7

print('You will return on ', t, "calenday day of the week")





# In[ ]:




