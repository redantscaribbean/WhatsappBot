from typing import Optional
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import Models.Inbound as Inbound


class TextMessage(BaseModel):
    isHSM: Optional[str] = None
    type: Optional[str] = None
    text: Optional[str] = None
    originalUrl: Optional[str] = None
    previewUrl: Optional[str] = None
    caption: Optional[str] = None
    url: Optional[str] = None
    filename: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    name: Optional[str] = None
    address: Optional[str] = None
    contacts: Optional[List[Inbound.Contact]] = None
