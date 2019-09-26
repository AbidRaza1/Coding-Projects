#!/usr/bin/env python
# coding: utf-8

# 
# 
# Counting number of Iterations
# 
# 
# 

# In[ ]:


def se(a):
    
    count = 0
    while a != 1:
      
        
        if a % 2 == 0:        
            a = a // 2
        else:                 
            a = a * 3 + 1
                  
        count = count + 1
    return count
    
    
p = se(10)
print(p)

