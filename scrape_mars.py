#!/usr/bin/env python
# coding: utf-8




import requests
import pymongo
import pandas as pd

from splinter import Browser
from bs4 import BeautifulSoup
import time


# #### Open chrome driver

# open chrome driver browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

# ## NASA Mars News - Collect Latest News Title and Paragraph Text

def scrape():
    browser = init_browser()
    
    # define url

    mars_news_url = "https://mars.nasa.gov/news/"
    time.sleep(3)
    browser.visit(mars_news_url)
    #putting a sleep function here seems to make the flask application run
    time.sleep(3)
    # create beautiful soup object 
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')


    # I added a few time.sleep(3) functions to allow the browser time to scrape the data. Hopefully that works.
    
    # find the first news title
    news_title = mars_news_soup.body.find("div", class_="content_title").text

    # find the paragraph associated with the first title

    news_p = mars_news_soup.body.find("div", class_="article_teaser_body").text


    time.sleep(3)

    mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(mars_image_url)


    # create the soup item

    html_image = browser.html
    mars_imaging = BeautifulSoup(html_image, 'html.parser')

    # the large image is within the figue element with class = lede
    image = mars_imaging.body.find("figure", class_="lede")

    #obtaining the url for the photo
    feat_img_url = image.find('figure', class_='lede').a['href']
    featured_image_url = f'https://www.jpl.nasa.gov{feat_img_url}'

    featured_image_url

    # ## Mars Weather

    # open url in browser
    #needs time to load
    time.sleep(3)


    # create a soup item


    # ## Mars Facts
    time.sleep(3)

    # define url
    mars_facts_url = "https://space-facts.com/mars/"

    # read html into pandas
    table = pd.read_html(mars_facts_url)

    # returns the value from an html table

    df = table[2]
    df.columns = ["Description", "Value"]

    # converting data to html table

    mars_facts_html=df.to_html()

    mars_facts_html

    # ## Mars Hemispheres

    # define url and open in browser

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)


    # #### Cerberus hemisphere

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Cerberus')

    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create a soup item
    hemispheres_html = browser.html
    cerberus_soup = BeautifulSoup(hemispheres_html, 'html.parser')

    cerberus = cerberus_soup.body.find('img', class_ = 'wide-image')
    cerberus_img = cerberus['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    #will store url later
    cerberus_url = hem_base_url + cerberus_img
    

    # #### Schiaperelli hemisphere

    # define url and open in browser

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Schiaparelli')

    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')
    #schiap html page
    # create a soup item
    schiap_html = browser.html
    schiap_soup = BeautifulSoup(schiap_html, 'html.parser')
    #obtaining the image of the schiaparelli
    schiap = schiap_soup.body.find('img', class_ = 'wide-image')
    schiap_img = schiap['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    schiap_url = hem_base_url + schiap_img
    # print(schiap_url)

    # #### Syrtis hemisphere

    # define url and open in browser

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Syrtis')

    # click on the link for the Cerberus hemisphere

    browser.click_link_by_partial_text('Open')

    # create a soup item
    syrtis_html = browser.html
    syrtis_soup = BeautifulSoup(syrtis_html, 'html.parser')

    syrtis = syrtis_soup.body.find('img', class_ = 'wide-image')
    syrtis_img = syrtis['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    syrtis_url = hem_base_url + syrtis_img
    # print(syrtis_url)

    # #### Valles hemisphere

    # define url and open in browser

    time.sleep(3)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    # click on the link for the Valles hemisphere

    browser.click_link_by_partial_text('Valles')

    # click on the link for the Valles hemisphere

    browser.click_link_by_partial_text('Open')

    # create a soup item
    valles_html = browser.html
    valles_soup = BeautifulSoup(valles_html, 'html.parser')

    valles = valles_soup.body.find('img', class_ = 'wide-image')
    valles_img = valles['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    valles_url = hem_base_url + valles_img
    # print(valles_url)


    # #### Define list of dictionaries that include each hemisphere

    hemispheres_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
        {"title": "Schiaparelli Marineris Hemisphere", "img_url": schiap_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url}
    ]

    # dictionary should be returned 
    mars_dict = {
        'headline': news_title,
        'paragraph':  news_p,
        'featuredimage': featured_image_url,
    #    'currentweather': mars_weather,
        'factstable': mars_facts_html,
        "va_title": "Valles Marineris Hemisphere", "va_img_url": valles_url,
        "ce_title": "Cerberus Hemisphere", "ce_img_url": cerberus_url,
        "sc_title": "Schiaparelli Marineris Hemisphere", "sc_img_url": schiap_url,
        "sy_title": "Syrtis Major Hemisphere", "sy_img_url": syrtis_url}

    # print(mars_dictionary)
    browser.quit()
    return mars_dict
