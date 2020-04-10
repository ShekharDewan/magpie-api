import pymongo
import datetime
import pprint
import sys, argparse, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from lxml import etree
from helper import percentage
from parse_grailed import soup_parse

def update_grailed(db, cond):
    query = db.listings.find(cond)
    for listing in query:
        