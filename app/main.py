# app/main.py

from fastapi import FastAPI
from app.routes import auth
import uvicorn

app = FastAPI()

# Include the authentication routes
app.include_router(auth.router, prefix="/auth")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)