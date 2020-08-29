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

    # Working  
    # db = client.get_database('flask_mongodb_atlas')
    # user_collection = pymongo.collection.Collection(db, 'user_collection')
    # db.db.collection.insert_one({"name": "Timmmm79"})
    # return


# Read
@app.route("/Read")
def fetchEntry():
    return


# Update
@app.route("/Update")
def updateEntry():
    return


# Delete
@app.route("/Delete")
def deleteEntry():
    return


if __name__ == "__main__":
    app.run(port=8000)
    main()




'''
How to install the venv ?
- Go to home folder of this project and type in
python3 -m venv venv


How to activate venv ?
. venv/bin/activate



Notes
1. The App configuration MUST be defined globally


'''