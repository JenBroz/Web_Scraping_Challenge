#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# In[ ]:


app=Flask(_name_)


# In[6]:


app.config['MONGO_URI']='mongodb://localhost:27017/mars_app'
mongo=PyMongo(app)


# In[4]:


@app.route('/')
def index():
    results=mongo.db.mars.find_one()
    print(results)
    print(type(results))


# In[8]:


@app.route('/scrape')
def scrape():
    mongo.db.mars.update({}, test_data, upsert=True)
    return "updated"


# In[5]:


if_name_=='main':
    app.run()


# In[ ]:




