from pydantic import BaseModel, EmailStr

class UserAuth(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(BaseModel):
    email: EmailStr
    username: str
    
class TokenResponse(BaseModel):
    access_token: str
    token_type: str