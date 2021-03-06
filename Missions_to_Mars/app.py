#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars


# In[ ]:


app=Flask(__name__)


# In[6]:


app.config['MONGO_URI']='mongodb://localhost:27017/mars_app'
mongo=PyMongo(app)


# In[4]:


@app.route('/')
def index():
    results=mongo.db.mars.find_one()
    print(results)
    print(type(results))
    return render_template('index.html', mars_data=results)

# In[8]:


@app.route('/scrape')
def scrape(): 
	test_data=scrape_mars.init()
	print(test_data)
	mongo.db.mars.update({}, test_data, upsert=True)
	return redirect('/')

# In[5]:


if __name__=='__main__':
    app.run()


# In[ ]:




