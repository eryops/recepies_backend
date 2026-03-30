from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routers import recipes

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


# Register routers
app.include_router(recipes.router)