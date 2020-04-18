import pymongo
from pymongo import MongoClient
import datetime
import pprint
import sys, argparse, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from lxml import etree
from helper import percentage
from parse_grailed import soup_parse
import pprint

#def update_grailed(db, cond):
client = MongoClient('localhost', 27017)
db = client.item_database
options = Options()
    #options.headless = True
#driver = webdriver.Firefox(options=options)
#with client:
query = db.listings.find({"size":"l"})
        
# need to create a versioning system to keep track of bumps & dates executed. most important step!!!
# TODO create mongo versioning system
# separate database for old versions of listing
# sort by ID
# collection of PER-ID documents for each listing
# 'timestamp' data array-style consisting of:
# date bumped
# new price 
# 
# cna count number of bumps by getting total entries in document


for listing in query:
    url = "https://www.grailed.com/listings/"+listing["grailed_ID"]
    # driver.get(url)
    pprint.pprint(listing)