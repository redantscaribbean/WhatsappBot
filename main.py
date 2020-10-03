from fastapi import FastAPI
import Models.Inbound as Inbound
import Models.Profile as Profile
import pymongo
import json
import requests
import datetime
import Models.Outbound as Outbound

app = FastAPI()


client = pymongo.MongoClient("mongodb+srv://redants:disruptiveCaribbean@whtatsappdev.e5gab.azure.mongodb.net/Whatsapp?retryWrites=true&w=majority")
db = client["Whatsapp"]
collection = db["Profile"]


UserProfile = Profile.Profile()
MessageArray = []


msgg = Outbound.TextMessage()
msgg.type = "text"
msgg.text = "Another one!"


@app.post('/webhook/',  status_code=200)
async def index(DBMessage: Inbound.Message):
    if DBMessage.type == 'message':
        # Check if User Phone number already exists, if exists then add message to user else create user and add message. Search DB for Sender Phone
        DBMessage.payload.payload.direction = "Received"
        DBMessage.payload.payload.type = DBMessage.payload.type
        DBMessage.payload.payload.timestamp = DBMessage.timestamp
        DBMessage.payload.payload.date = datetime.datetime.now()
        #Check if user exists in DB
        results = collection.find_one({"senderPhone": DBMessage.payload.sender.phone})
        if results is None:
            # Add user
            UserProfile.senderName = DBMessage.payload.sender.name
            UserProfile.senderPhone = DBMessage.payload.sender.phone
            MessageArray.append(DBMessage.payload.payload)
            UserProfile.message = MessageArray
            addToDB(UserProfile, "insert")
        else:
            # Append message
            addToDB(DBMessage, "update")
    return "hi How are you"


def sendMessage():
    url = 'https://api.gupshup.io/sm/api/v1/msg'
    payload = {"channel": "whatsapp","source": "18683039164","destination": "18687067421","src.name": "BottixWhatsappDemo", "message": json.dumps(msgg.dict())}
    headers = {'content-type': 'application/x-www-form-urlencoded', 'apikey': '6ca26a782aeb4f1ecfea2e1b5252aabe','Cache-Control': 'no-cache'}
    r = requests.post(url, data=payload, headers=headers)
    print(r.text)


def addToDB(message, type):
    if type == "insert":
        collection.insert_one(message.dict())
    else:
        where = {"senderPhone": message.payload.sender.phone}
        update = {"$push": {"messages": message.payload.payload.dict()}}
        collection.update_one(where, update)


#sendMessage()


