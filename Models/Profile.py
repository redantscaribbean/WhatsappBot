from pydantic import BaseModel
from typing import Optional
from typing import List
from fastapi import FastAPI


class Messages(BaseModel):
    type: Optional[str] = None
    text: Optional[str] = None
    timestamp: Optional[str] = None
    direction: Optional[str] = None
    url: Optional[str] = None


class Profile(BaseModel):
    senderName: Optional[str] = None
    senderPhone: Optional[str] = None
    messages: Optional[Messages] = None
