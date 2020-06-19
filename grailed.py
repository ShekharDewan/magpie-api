import sys, argparse, time
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import etree
from helper import percentage
from parse_grailed import soup_parse
from chew_grailed import chewFeed
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.item_database
listings = db.listings

parser = argparse.ArgumentParser("Process list")
parser.add_argument('-l', '--list', nargs='+', type=str, help='<Required> set flag', required=False)
parser.add_argument('-i', '--id', nargs='+', type=str, help='individual listing', required=False)
args = parser.parse_args()

if args.list is not None:

    designerLst = args.list
    designerLst = [name.replace(" ", "-").lower().split(",") for name in designerLst]
    designerLst = designerLst[0] #list is within a list, so have to extract it like this
    print(designerLst)

    for designer in designerLst:
        output = chewFeed(designer)
        soup_parse(db, output)
