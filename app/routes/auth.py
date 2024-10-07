from fastapi import APIRouter, HTTPException, Depends
from app.models import User
from app.schemas import UserAuth, UserOut, TokenResponse
from app.database import user_collection, user_helper
from app.utils.hash import hash_password, verify_password
from app.utils.jwt_handler import create_access_token
from pymongo.errors import DuplicateKeyError

router = APIRouter()

@router.post('/signup', response_model=UserOut)
async def signup(user: User):
    user.password = hash_password(user.password)
    try:
        user_data = user.dict()
        new_user = await user_collection.insert_one(user_data)
        created_user = await user_collection.find_one({"_id": new_user.inserted_id})
        return user_helper(created_user)
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Email already registered")

@router.post("/login", response_model=TokenResponse)
async def login(user: UserAuth):
    found_user = await user_collection.find_one({"email": user.email})
    if not found_user:
        raise HTTPException(status_code=400, detail="invalid email or password")
    if not verify_password(user.password, found_user["password"]):
        raise HTTPException(status_code=400, detail="invalid email or password")
    access_token = create_access_token({"sub":found_user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}