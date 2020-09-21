#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup


# In[2]:


url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[4]:


def scrape_first():
    results_list=[]
    browser=Browser('chrome', executable_path='/usr/local/bin/chromedriver',headless)
    browser.visit(url)
    soup=BeautifulSoup(browser.html, 'html.parser')
    results=soup.find(class_='collapsible').find_all('item')
    for each_result in results:
        image_title=each_result.find(class_='description').find('a').find('h3').text
        results_list.append(image_title)
    for each_name in results_list:
        browser.find_link_by_partial_text(each_name).click()
        new_soup=BeautifulSoup(browser.html, 'html.parser')
        link=new_soup.find(class_='downloads').find('ul').find('li').find('a')['href']
        image_urls.append(link)
        browser.back()
    return image_urls


# In[5]:


def scrape_second():
    one_dictionary=''
    return one_dictionary


# In[6]:


def scrape_third():
    one_dictionary=''
    return one_dictionary


# In[7]:


def scrape_all():
    all_data={}
    all_data['headlines']=scrape_first()
    all_data['images_url']=scrape_second()
    all_data['url']=scrape_third()
    return all_data


# In[ ]:




