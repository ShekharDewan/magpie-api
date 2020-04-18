from bs4 import BeautifulSoup
import pymongo
import datetime
import pprint

def soup_parse(db, grailedSoup):
    soup = grailedSoup
    listings = db.listings

    # NEED attributes:
    # name
    # brand
    # size
    # old price
    # new price
    # date posted
    # date bumped
    # (later) origin site

    #TODO sizing guide for subscribers?

    for tag in grailedSoup:
 
        # title = tag.find('p', {"class": "truncate listing-title"})
        # designer = tag.find('p', {'class': 'listing-designer truncate'})
        # size = tag.find('p', {'class': 'listing-size sub-title'})
        # oldPrice = tag.find('p', {'class': 'sub-title original-price strike-through'})
        # grailed_ID = tag.find('button', {'class': "heart-follow"})['id']
        
        newPrice = tag.find('p', {'class': 'sub-title new-price'})
        ogPrice = tag.find('p', {'class': 'sub-title original-price'})
        bump = tag.find('span', {'class': 'date-ago'})
        origin = tag.find('span', {'class': 'bumped date-ago'})

        listing = { "name": tag.find('p', {"class": "truncate listing-title"}).string,
                    "designer": tag.find('p', {'class': 'listing-designer truncate'}).string,
                    "size": tag.find('p', {'class': 'listing-size sub-title'}).string,
                    "grailed_ID": tag.find('button', {'class': "heart-follow"})['id'].replace('fr','')}
        
        if ogPrice == None:
            listing["original price"] = tag.find('p', {'class': 'sub-title original-price strike-through'}).string
            listing["current price"] = newPrice.string
        else:
            listing["price"] = ogPrice.string
        if origin == None:
            listing["listed"] = bump.string
        else:
            listing["bumped"] = bump.string
            listing["listed"] = origin.string

        listings.insert_one(listing)

    #Count the amount of bumps over time thru incrementing value in listing
    #armount of time between bumps