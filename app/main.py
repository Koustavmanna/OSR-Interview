from fastapi import FastAPI
from app.routes.osr import router as osr_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="OSR Model Builder")
app.include_router(osr_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
