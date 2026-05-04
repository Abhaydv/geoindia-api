from fastapi import FastAPI
from core.db import engine, Base

# 👉 IMPORTANT (yeh line zaroor honi chahiye)
from models import location, user, api_key, usage

import routes.auth as auth
import routes.location as location_routes
import routes.api_keys as api_keys_routes

app = FastAPI()

# 👉 THIS CREATES TABLES
Base.metadata.create_all(bind=engine)

# routers
app.include_router(auth.router)
app.include_router(api_keys_routes.router)
app.include_router(location_routes.router)

@app.get("/")
def home():
    return {"message": "GeoIndia API Running 🚀"}