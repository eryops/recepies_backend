from fastapi import FastAPI
from app.routers import recipes

app = FastAPI()

# Register routers
app.include_router(recipes.router)