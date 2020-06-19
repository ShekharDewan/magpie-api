from bs4 import BeautifulSoup
import pymongo
import datetime
import pprint

def soup_parse(db, grailedSoup):
    soup = grailedSoup
    listings = db.listings

    num = 0
    for tag in grailedSoup:
        print(num)
        
        
        title = tag.find('p', {'class': "truncate listing-title"})
        designer = tag.find('p', {'class': 'listing-designer truncate'})
        size = tag.find('p', {'class': 'listing-size sub-title'})
        oldPrice = tag.find('p', {'class': 'sub-title original-price strike-through'})
        grailed_ID = tag.find('button', {'class': "heart-follow"})
        
        newPrice = tag.find('p', {'class': 'sub-title new-price'})
        ogPrice = tag.find('p', {'class': 'sub-title original-price'})
        bump = tag.find('span', {'class': 'date-ago'})
        origin = tag.find('span', {'class': 'bumped date-ago'})
        
        if title != None:
            listing = { "name": title.contents[0],
                        "designer": designer.string,
                        "size": size.string,
                        "grailed_ID": grailed_ID['id'].replace('fr','')}
            
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
        num = num + 1

    #Count the amount of bumps over time thru incrementing value in listing
    #armount of time between bumps