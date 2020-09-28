from typing import Optional, List
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, validator, Required, fields
import Models.Inbound as Inbound
import Models.Profile as Profile
import pymongo
from pymongo import MongoClient
import json
import requests
import datetime

app = FastAPI()


client = pymongo.MongoClient("mongodb+srv://redants:disruptiveCaribbean@whtatsappdev.e5gab.azure.mongodb.net/Whatsapp?retryWrites=true&w=majority")
db = client["Whatsapp"]
collection = db["Profile"]


UserProfile = Profile.Profile()
MessageArray = []



@app.post('/webhook/',  status_code=200)
async def index(DBMessage: Inbound.Message):
    if DBMessage.type == 'message':
        #Check if User Phone number already exists, if exists then add message to user else create user and add message. Search DB for Sender Phone
        DBMessage.payload.payload.direction = "Received"
        DBMessage.payload.payload.type = DBMessage.payload.type
        DBMessage.payload.payload.timestamp = DBMessage.timestamp
        DBMessage.payload.payload.date = datetime.datetime.now()
        results = collection.find_one({"senderPhone": DBMessage.payload.sender.phone})
        if results == None:
            #Add user
            UserProfile.senderName = DBMessage.payload.sender.name
            UserProfile.senderPhone = DBMessage.payload.sender.phone
            MessageArray.append(DBMessage.payload.payload)
            UserProfile.message = MessageArray
            collection.insert_one(UserProfile.dict())
        else:   #Append message
            MessageArray.append(DBMessage.payload)
            where = {"senderPhone": DBMessage.payload.sender.phone}
            update = {"$push": {"messages": DBMessage.payload.payload.dict()}}
            collection.update_one(where, update)
    return "hi How are you"


def sendMessage():
    url = 'https://api.gupshup.io/sm/api/v1/msg'
    payload = {"channel" : "whatsapp","source" : "18683039164","destination" : "18687067421","src.name":"BottixWhatsappDemo", "message":json.dumps({"isHSM":"false","type": "text","text": "Hi John, how are you?"})}
    headers = {'content-type': 'application/x-www-form-urlencoded', 'apikey': '6ca26a782aeb4f1ecfea2e1b5252aabe', 'Cache-Control': 'no-cache' }
    r = requests.post(url, data=payload, headers=headers)
    print(r.text)

sendMessage()