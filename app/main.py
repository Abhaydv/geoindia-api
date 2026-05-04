from fastapi import FastAPI

from app.core.db import engine, Base
import app.models.location
import app.models.user
import app.models.api_key
import app.models.usage

from app.routes import auth
from app.routes import location as location_routes
from app.routes import api_keys as api_keys_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(api_keys_routes.router)
app.include_router(location_routes.router)


@app.get("/")
def home():
    return {"message": "GeoIndia API Running 🚀"}