# Simple FastAPI server test
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def hello():
#     return {"message": "Hello from LoveTag! 🚀"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
from typing import Optional

app = FastAPI()

# CORS Setup (allow frontend to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production!
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example endpoint
@app.post("/claim")
async def claim_partner(
    user_id: int = Form(...),
    selfie: UploadFile = File(...),
    partner_photo: UploadFile = File(...)
):
    # Save files temporarily
    selfie_path = f"temp_selfie_{uuid.uuid4()}.jpg"
    partner_path = f"temp_partner_{uuid.uuid4()}.jpg"
    
    with open(selfie_path, "wb") as buffer:
        buffer.write(await selfie.read())
    
    with open(partner_path, "wb") as buffer:
        buffer.write(await partner_photo.read())
    
    # TODO: Add face recognition logic
    return {"success": True, "message": "Partner claimed!"}

# Run with: uvicorn main:app --reload