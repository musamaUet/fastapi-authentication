# app/database.py

import motor.motor_asyncio
from bson import ObjectId
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client['fastapi-auth']
user_collection = database.get_collection('users')

# Helper function to convert mongodb db document to python dictionary

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "username": user["username"]
    }