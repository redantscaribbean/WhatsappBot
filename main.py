from typing import Optional
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, validator, Required, fields
import Models.Inbound as Inbound
from http import HTTPStatus
import bottle

app = FastAPI()

db = []


@app.post('/webhook/',  status_code=200)
async def index(message: Inbound.Message):
    return bottle.HTTPResponse(status=200)
