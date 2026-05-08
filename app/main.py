from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.db import engine, Base

# ------------------ IMPORT MODELS ------------------

import app.models.user
import app.models.location
import app.models.api_key
import app.models.usage

# ------------------ IMPORT ROUTES ------------------

from app.routes import auth, location, api_keys

# ------------------ APP ------------------

app = FastAPI()

# ------------------ CORS ------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ CREATE TABLES ------------------

Base.metadata.create_all(bind=engine)

# ------------------ ROUTERS ------------------

app.include_router(auth.router)
app.include_router(location.router)
app.include_router(api_keys.router)

# ------------------ HOME ROUTE ------------------

@app.get("/")
def home():
    return {
        "message": "GeoIndia API Running 🚀"
    }