#!/usr/bin/env python
# coding: utf-8

# In[1]:


sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print("Number of vowels:", count)


# In[ ]:




