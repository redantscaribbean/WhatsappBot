from typing import Optional
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, validator, Required, fields
import Models.Inbound as Inbound
import Models.Profile as Profile
import pymongo
from pymongo import MongoClient
import json

app = FastAPI()


client = pymongo.MongoClient("mongodb+srv://redants:disruptiveCaribbean@whtatsappdev.e5gab.azure.mongodb.net/Whatsapp?retryWrites=true&w=majority")
db = client["Whatsapp"]
collection = db["Profile"]
profile = Profile.Profile()
messages = Profile.Messages()

@app.post('/webhook/',  status_code=200)
async def index(message: Inbound.Message):
    if message.type == 'message':
        if message.payload.type == 'text':
            #Check if User Phone number already exists, if exists then add message to user else create user and add message. Search DB for Sender Phone
            results = collection.find_one({"senderPhone": message.payload.sender.phone})
            if results == None:
                #Add user
                profile.senderName = message.payload.sender.name
                profile.senderPhone = message.payload.sender.phone
                messages.type = message.payload.type
                messages.text = message.payload.payload.text
                messages.timestamp = message.payload.payload.url
                messages.url = message.timestamp
                messages.direction = "Recieved"
                profile.messages = messages
                print(profile)
                collection.insert_one(profile.dict())
    return message
