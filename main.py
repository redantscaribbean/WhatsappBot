from typing import Optional
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, validator, Required, fields
import Models.Inbound as Inbound
import pymongo
from pymongo import MongoClient
import json

app = FastAPI()


client = pymongo.MongoClient("mongodb+srv://redants:disruptiveCaribbean@whtatsappdev.e5gab.azure.mongodb.net/Whatsapp?retryWrites=true&w=majority")
db = client["Whatsapp"]
collection = db["Profile"]


@app.post('/webhook/',  status_code=200)
async def index(message: Inbound.Message):
    if message.type == 'message':
        if message.payload.type == 'text':
            collection.insert_one(message.dict())
    return message
