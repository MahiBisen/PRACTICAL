#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''The probability that it is Friday and that a student is absentis 3%. Since there are 5 school days in
a week,the probability that it is Friday is 20%. What is the probability that a student is absent
given that today is Friday? Apply Baye’s rule in python to get the result.
'''
PA = float(input( " P(A) :  "))
PB =  float(input( " P(B) :  "))
PBA =  float(input( " P(B/A) :  "))
PAB =  (PBA*PA)/PB
print(" P(A/B) = ",PAB)


# In[ ]:





# In[ ]:




