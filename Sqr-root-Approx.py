#!/usr/bin/env python
# coding: utf-8

# In[4]:



def mySqrt(n):
        
        fG = n/2
       
        for i in range(5):
                    g = (0.5) * (fG + (n/fG))
                    fG = g
        return g

n = int(input("Enter the Number(Except 0): "))
print(mySqrt(n))    


# In[ ]:





# In[ ]:




