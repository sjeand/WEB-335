#=======================================================
# Title: jeanBaptiste-user-update.py
# Author: Professor Krasso
#  Date: 07/24/2021
#  Modifier: Sarah Jean Baptiste
#  Description: Updating and deleting documents
#========================================================

# Import statements
import pymongo
import pprint
import datetime
from pymongo import MongoClient

# Connect to local database
client = MongoClient('localhost', 27017)
db = client.web335

# Update user by id
db.users.update_one(
    {"employee_id": "124"},
    {
        "$set":{
            "email":"sjbaptiste@my365.bellevue.edu"
        }
    }
)

# Print results
pprint.pprint(db.users.find_one({"employee_id":"124"}))