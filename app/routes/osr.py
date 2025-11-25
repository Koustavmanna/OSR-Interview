from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.request import OSRRequest
from app.schemas.response import OSRResponse
from app.services.llm_service import generate_osr

router = APIRouter()

@router.post("/generate-osr", response_model=OSRResponse)
async def generate_osr_model(payload: OSRRequest):
    try:
        osr = await generate_osr(payload.description)
        return JSONResponse(status_code=200, content=osr)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
