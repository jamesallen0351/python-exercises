#!/usr/bin/env python
# coding: utf-8

# In[16]:


little_mermaid = 3
brother_bear = 5
hercules = 1
movie_price_per_day = 3

days = 3 + 5 + 1

total = movie_price_per_day * days
total


# In[8]:


movies = [
    "little_mermaid",
    "brother_bear",
    "hercules"
]

movies


# In[10]:


company = [
    "Google",
    "Amazon",
    "facebook"
]
company


# In[17]:


google = 400
amazon = 380
facebook = 350

payment = (google * 6) + (amazon * 4) + (facebook * 10)

payment


# In[18]:


class_not_full = True
does_not_conflict = True

student_enroll_in_class = class_not_full and does_not_conflict


# In[19]:


buy_2_or_more = True
offer_not_expired = True
premium_member = True

product_offer = (buy_2_or_more or premium_member) and offer_not_expired


# In[20]:


username = 'codeup'
password = 'notastrongpassword'


# In[21]:


password_at_least_5_characters = len(password) >= 5
username_no_more_than_20_characters = len(username) < 20
password_not_equal_username = password != username
username_or_password_not_start_or_end_whitespace = (password[0] != ' ' and password[-1] != ' ') and (username[0] != ' ' and username[-1] != ' ')


# In[ ]:




