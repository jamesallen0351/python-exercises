#!/usr/bin/env python
# coding: utf-8

# In[16]:


little_mermaid = 3
brother_bear = 5
hercules = 1
movie_price_per_day = 3

days = 3 + 5 + 1

total = movie_price_per_day * days
print(f"The total amount paid is ${total}")


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

print(f'The total payment is ${payment}')


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
username_no_more_than_20_characters = len(username) <= 20
password_not_equal_username = password != username

username_has_spaces = username != username.strip()
password_has_spaces = password != password.strip()

username_is_good = username_no_more_than_20_characters and password_not_equal_username and not username_has_spaces
password_is_good = password_at_least_5_characters and password_not_equal_username and not password_has_spaces

print(username)
print(password)





