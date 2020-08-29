#!/usr/bin/env python3

from flask import Flask
from flask_pymongo import pymongo

# Define App here
app = Flask(__name__) 
client = None
collection = None

def main():
    # app = Flask(__name__)       # You cannot put app here. It has to be a global variable
    app.run(port=8000)

    # Set up the client
    CONNECTION_STRING = "mongodb+srv://timmanas:Apple@cluster0-9czdc.mongodb.net/flask_mongodb_atlas?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
    client = pymongo.MongoClient(CONNECTION_STRING)

    # Set up Database & Collection
    db = client['flask_mongodb_atlas']
    collection = db['SampleCollection']
    

    

# Home Page
@app.route("/")
def homePage():
    return "<h1> Hello World </h1>"


# Create
@app.route("/Create")
def createEntry():
    document = {"Name" : "Tim", 
                "Age": "None of Yo Bizness",
                "Occupation":"SoundCloudRapper"}
    
    id = collection.insert_one(document).inserted_id
    pass


# Read
@app.route("/Read")
def fetchEntry():
    pass


# Update
@app.route("/Update")
def updateEntry():
    pass


# Delete
@app.route("/Delete")
def deleteEntry():
    pass


if __name__ == "__main__":
    main()




'''
How to install the venv ?
- Go to home folder of this project and type in
python3 -m venv venv


How to activate venv ?
. venv/bin/activate


'''