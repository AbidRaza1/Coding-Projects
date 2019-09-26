#!/usr/bin/env python
# coding: utf-8

# ## GROCERY COUNTER

# In[6]:


nitems = 0
ncount =0
more = True
while more:
            x = float(input('Enter item price or zero if no item is left: '))
            if x > 0 and x != 0:
                    nitems =  x + nitems
                    ncount =  1 + ncount
            else:
                 break
print('Total Price',nitems)
print('Total Items',ncount)
            


# In[ ]:




