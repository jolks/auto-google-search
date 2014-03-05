#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import re, codecs, time, random, urllib2

# https://www.google.com/search?q=indonesian+restaurant+singapore&hl=en&safe=off&filter=0&start=0
# https://www.google.com/search?q=indonesian+restaurant+singapore&hl=en&safe=off&filter=0&start=10
# https://www.google.com/search?q=indonesian+restaurant+singapore&hl=en&safe=off&filter=0&start=N where N = 0, 10, 20, 30, ...

search_term = 'john lau singapore blog'
target = 'jolks'
#google_url = 'https://www.google.com'  # secure search, will appear as (not provided) in Google Analytics
google_url = 'http://www.google.com'    # the search_term will appear in Google Analytics

browser = webdriver.Firefox() # Get local session of firefox
start_num = 0

search_url = google_url + '/search?hl=en&q=' + search_term + '&safe=off&filter=0&start=' + str(start_num)
browser.get(search_url)

try:
    has_target = browser.find_element_by_xpath("//a[contains(@href,'" + target + "')]")
except NoSuchElementException:
    print target, 'not found...'
    browser.close()        

target_url = has_target.get_attribute('href')   # Before click(), can get real target URL
has_target.click()  # click and go to the target website
#target_url = has_target.get_attribute('href')   # After click(), can get Google search result full link
        
print target_url
time.sleep(random.uniform(110, 185))
# Use BeautifulSoup to get any URL on current website using target_url
site = urllib2.urlopen(target_url)
        
data = site.read()
parsed = BeautifulSoup(data)
results = parsed.findAll('a')
if results:
    for i in results:
        target_url_url = i['href']
        if target_url_url != target_url:
            print target_url_url
            break

browser.get(target_url_url)
time.sleep(random.uniform(30, 100))

browser.close()
