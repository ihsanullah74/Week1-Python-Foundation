#!/usr/bin/env python
# coding: utf-8

# In[1]:


marks = []
n = int(input("How many subjects? "))
for i in range(n):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)
print("Average marks:", average)


# In[ ]:




