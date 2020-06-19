import sys, argparse, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from lxml import etree
from helper import percentage
from parse_grailed import soup_parse

def chewFeed(name):

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    url = "https://www.grailed.com/designers/"+name
    driver.get(url)

    count = driver.find_element_by_xpath(".//*[@class='ais-Panel-body']").text
    count_value = count.split()
    count_int = int(count_value[0].replace(',',''))
    print(count_int)
    feedCount = 0
    prevCount = 0

    print("parsing "+ name + " feed items...")
    while feedCount < count_int:
            
        feedCount = len(driver.find_elements_by_xpath(".//*[@class='feed']/div"))
        
        driver.execute_script("window.scrollTo(0, 0);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        if feedCount > prevCount:
            print(percentage(feedCount,count_int))
        prevCount = feedCount

    print("done!")
    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')
    driver.quit()
    return soup.find_all("div", {"class": "feed-item"})
