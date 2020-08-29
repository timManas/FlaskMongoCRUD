#!/usr/bin/env python3

from flask import Flask
from flask_pymongo import pymongo

# Define Connections here
# Must be GLOBAL Variables
app = Flask(__name__) 
CONNECTION_STRING = "mongodb+srv://timmanas:Apple@cluster0-9czdc.mongodb.net/flask_mongodb_atlas?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client['flask_mongodb_atlas']
collection = db['SampleCollection']

def main():
    # app = Flask(__name__)       # You cannot put app here. It has to be a global variable
    pass


# Home Page
@app.route("/")
def homePage():
    return "<h1> Hello World </h1>"


# Create
@app.route("/Create")
def createEntry():
    document = {"Name" : "Tina", "Age": "None of Yo Bizness", "Occupation":"SoundCloudRapper"}
    id = collection.insert_one(document).inserted_id
    return ("<h1>Id: " + str(id) + "</h1>")

    # Ex2: Working Code
    # db = client.get_database('flask_mongodb_atlas')
    # user_collection = pymongo.collection.Collection(db, 'user_collection')
    # db.db.collection.insert_one({"name": "Timmmm79"})
    # return


# Read
@app.route("/Read")
def fetchEntry():
    obj = collection.find_one({"Name": "Tina"})     # Returns Object
    print ("Find_one: " + str(obj) + "            | Find Age:" + str(obj["Age"]))

    obj = collection.find({"company": "Quincy Inc"})     # Returns Cursor
    print ("Find: " + str(obj))

    return "Found Element"


# Update
@app.route("/Update")
def updateEntry():
    obj = collection.update_one({"Name" : "Tony"}, {"$set": {"Name" : "Ulyses"}})     # Finds the first occurences and replaces
    obj = collection.update_many({"Name" : "Tina"}, {"$set": {"Name" : "Timmm"}})     # Finds All occurences and replaces All of them

    print ("Update_one: " + str(obj))


    return "Replaced Element"


# Delete
@app.route("/Delete")
def deleteEntry():
    return "Deleted Element"


if __name__ == "__main__":
    app.run(port=8000)
    main()




'''
How to install the venv ?
- Go to home folder of this project and type in
python3 -m venv venv


How to activate venv ?
. venv/bin/activate


Port Already in use ? Kill it with this command:
lsof -i:8000
kill $(lsof -t -i:8000)

Notes
1. The App configuration MUST be defined globally


'''