
#=======================================================
# Title: jeanBaptiste-user-service.py
# Author: Professor Krasso
#  Date: 07/24/2021
#  Modifier: Sarah Jean Baptiste
#  Description: Querying and creating documents
#========================================================

# Import statements
import pymongo 
import pprint
import datetime
from pymongo import MongoClient

# Connect to local database
client = MongoClient('localhost', 27017)
db = client.web335

# Create a new user.
user = {
    "first_name": "Amy",
    "last_name": "Winehouse",
    "email": "back2black@gmail.com",
    "employee_id": "124",
    "date_created": datetime.datetime.utcnow()
}

# Insert new user with id.
user_id = db.users.insert_one(user).inserted_id

# Find one user and return results.
print(user_id)
pprint.pprint(db.users.find_one({"employee_id": "124"}))

