from fastapi import FastAPI
from . import models
from .database import engine
from .routers import location, image, price, package


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(location.router)
app.include_router(image.router)
app.include_router(price.router)
app.include_router(package.router)
        


@app.get('/')
async def index():
    return {"data":"Hello, lets build that API for Mohammed Ibrahim"}
