#!/usr/bin/env python
# coding: utf-8

# In[67]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time


# In[69]:


def init(): 
    browser=Browser('chrome', executable_path='chromedriver', headless=False)
    news_title, news_p=mars_news(browser)
    data={
        'news_title': news_title, 
        'news_p': news_p, 
        'featured_image': mars_image(browser), 
        'facts': mars_facts(), 
        'hemispheres': mars_hemispheres(browser)
    }
    browser.quit()
    return data


# In[70]:


# init()


# In[3]:


# browser=Browser('chrome', executable_path='chromedriver', headless=False)


# In[64]:


def mars_news(browser): 
    website_path='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(website_path)
    time.sleep(2)
    soup=BeautifulSoup(browser.html, 'html.parser')
    try: 
        results=soup.find_all('ul', class_='item_list')[0].find_all('li', class_='slide')
        news_title=results[0].find('div', class_='content_title').a.text
        news_p=results[0].find('div', class_='article_teaser_body').text
    except: 
        news_title='issue'
        news_p='issue'
    print(news_title)
    print(news_p)
    return news_title, news_p


# In[22]:


# mars_news(browser)


# In[56]:


def mars_image(browser): 
    base_url='https://www.jpl.nasa.gov'
    website_path='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(website_path)
    time.sleep(1)
    browser.click_link_by_id('full_image')
    time.sleep(1)
    browser.click_link_by_partial_text('more info')
    soup=BeautifulSoup(browser.html, 'html.parser')
    try: 
        featured_image_url=soup.find('figure', class_='lede').a.img.get('src')
        featured_image_url=base_url+featured_image_url
    except: 
        featured_image_url='issue'
    print(featured_image_url)
    return featured_image_url


# In[34]:


# mars_image(browser)


# In[57]:


def mars_facts():
    website_path='https://space-facts.com/mars/'
    # read_html returns a list -> tables is a list
    tables=pd.read_html(website_path)
    df=tables[0]
    html_string=df.to_html()
    print(html_string)
    return html_string


# In[41]:


# mars_facts()


# In[59]:


def mars_hemispheres(browser):
    base_url='https://astrogeology.usgs.gov/'
    hemisphere_image_urls=[]
    links={}
    website_path='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(website_path)
    time.sleep(1)
    soup=BeautifulSoup(browser.html, 'html.parser')
    try: 
        hemispheres=soup.find_all('div', class_='item')
        for each_hemispheres in hemispheres: 
            links[each_hemispheres.find('div', class_='description').find('a').text]=base_url+each_hemispheres.find('a').get('href')
        for each_hemispheres in links: 
            browser.visit(links[each_hemispheres])
            time.sleep(1)
            new_soup=BeautifulSoup(browser.html, 'html.parser')
            link=new_soup.find(class_='downloads').find('ul').find('li').find('a')['href']
            new_dict={}
            new_dict['title']=each_hemispheres
            new_dict['image_url']=link
            hemisphere_image_urls.append(new_dict)
            # browser.click_link_by_text('Sample')
    except: 
        pass
    print(hemisphere_image_urls)
    return hemisphere_image_urls


# In[55]:


# mars_hemispheres(browser)


# In[2]:


# url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[4]:


# def scrape_first():
#     results_list=[]
#     browser=Browser('chrome', executable_path='/usr/local/bin/chromedriver',headless)
#     browser.visit(url)
#     soup=BeautifulSoup(browser.html, 'html.parser')
#     results=soup.find(class_='collapsible').find_all('item')
#     for each_result in results:
#         image_title=each_result.find(class_='description').find('a').find('h3').text
#         results_list.append(image_title)
#     for each_name in results_list:
#         browser.find_link_by_partial_text(each_name).click()
#         new_soup=BeautifulSoup(browser.html, 'html.parser')
#         link=new_soup.find(class_='downloads').find('ul').find('li').find('a')['href']
#         image_urls.append(link)
#         browser.back()
#     return image_urls


# In[ ]:




