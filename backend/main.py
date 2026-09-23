from fastapi import FastAPI

from app.api.categories import router as categoties_router

app = FastAPI()

app.include_router(categoties_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}