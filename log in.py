#!/usr/bin/env python
# coding: utf-8

# In[1]:


correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful! Welcome", username)
else:
    print("Invalid username or password!")


# In[ ]:




