from pydantic import BaseModel
from typing import Optional
from typing import List
from fastapi import FastAPI


class Profile(BaseModel):
    senderName: Optional[str] = None
    senderPhone: Optional[str] = None
    message: Optional[List] = None
