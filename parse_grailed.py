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
        print('==========')
        title = tag.find('p', {"class": "truncate listing-title"})
        designer = tag.find('p', {'class': 'listing-designer truncate'})
        size = tag.find('p', {'class': 'listing-size sub-title'})
        ogPrice = tag.find('p', {'class': 'sub-title original-price'})
        oldPrice = tag.find('p', {'class': 'sub-title original-price strike-through'})
        newPrice = tag.find('p', {'class': 'sub-title new-price'})
        bump = tag.find('span', {'class': 'date-ago'})
        origin = tag.find('span', {'class': 'bumped date-ago'})
        
        print(title.string)
        print(designer.string)
        print(size.string)

        listing = { "name": title.string,
                    "designer": designer.string,
                    "size": size.string}
        
        if ogPrice == None:
            listing["original price"] = oldPrice.string
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