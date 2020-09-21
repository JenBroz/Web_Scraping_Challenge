#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import time
import requests


# In[3]:


url = 'https://space-facts.com/mars/'
df_list = pd.read_html(url)
df_list[2]


# In[ ]:




