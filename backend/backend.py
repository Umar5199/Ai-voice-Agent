# token_server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from livekit import api
import uvicorn
import os
from dotenv import load_dotenv
import uuid

load_dotenv()

app = FastAPI()

# Allow your frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
LIVEKIT_URL = os.getenv("LIVEKIT_URL")

@app.get("/get_token")
async def get_token(room: str = "my-room"):
    # Generate unique identity
    identity = f"user-{uuid.uuid4().hex[:8]}"
    
    # Create token
    token = api.AccessToken(LIVEKIT_API_KEY, LIVEKIT_API_SECRET) \
        .with_identity(identity) \
        .with_name("User") \
        .with_grants(api.VideoGrants(
            room_join=True,
            room=room,
            can_publish=True,
            can_subscribe=True,
        )).to_jwt()
    
    return {"token": token, "url": LIVEKIT_URL, "room": room}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)