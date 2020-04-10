import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.item_database

# api should be made of ACCESSORS & MUTATORS
# can also hold final var conversion helpers for sake of formatting
# web automation is a subroutine of backend database used for initial retrieval & updating

# python is a SCRIPTING langauge, which means all files must be ACTIONS
# possibly employ cmd parsing for method selection

#ACCESSORS

#Get group of listings.. filter by several options


#MUTATORS

#all internal, perform scheduled updates of items in list to have discount/bump info
#need a way of updating by accessing an item's nested listing page

#need a way of automatically comparing new batch of listings to old batch, 
# and flag discrepancies as sold/removed

#automation & parsing stuff (selenium && beautifulsoup) go in here
#subroutines for updating the database

# list for backend
# TODO impl. database update routine
# TODO impl. re-use for chew_grailed routine to get newly uploaded items & disregard duplicates
# TODO impl. ACCESSOR commands
