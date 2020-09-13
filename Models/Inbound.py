from typing import Optional
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, validator, Required, fields

app = FastAPI()

db = []


class Url(BaseModel):
    url: Optional[str] = None
    type: Optional[str] = None


class Phones(BaseModel):
    phone: Optional[str] = None
    type: Optional[str] = None


class Org(BaseModel):
    company: Optional[str] = None


class Name(BaseModel):
    first_name: Optional[str] = None
    formatted_name: Optional[str] = None
    last_name: Optional[str] = None


class IMS(BaseModel):
    ims:  Optional[str] = None


class Email(BaseModel):
    email: Optional[str] = None
    type: Optional[str] = None


class Address(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None
    countryCode: Optional[str] = None
    state: Optional[str] = None
    street: Optional[str] = None
    type: Optional[str] = None
    zip: Optional[str] = None


class Contact(BaseModel):
    addresses: Optional[List[Address]] = None
    emails: Optional[List[Email]] = None
    ims: Optional[List[IMS]] = None
    name: Optional[Name] = None
    org: Optional[Org] = None
    phones: Optional[List[Phones]] = None
    urls: Optional[List[Url]] = None


class PayloadContent(BaseModel):
    caption: Optional[str] = None
    text: Optional[str] = None
    url: Optional[str] = None
    contentType: Optional[str] = None
    urlExpiry: Optional[int] = None
    ts: Optional[int] = None
    longitude: Optional[str] = None
    latitude: Optional[str] = None
    contacts: Optional[List[Contact]] = None


class Sender(BaseModel):
    phone: str
    name: str
    country_code: str
    dial_code: str


class Payload(BaseModel):
    id: str
    source: int
    type: str
    phone: Optional[str] = None
    gsId: Optional[str] = None
    destination: Optional[str] = None
    payload: PayloadContent
    sender: Sender


class Message(BaseModel):
    app: str
    timestamp: int
    version: Optional[int] = None
    type: str
    payload: Payload