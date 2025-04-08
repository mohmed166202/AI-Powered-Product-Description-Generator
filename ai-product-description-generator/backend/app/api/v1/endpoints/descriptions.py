from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.services.openai_service import generate_product_description
from app.core.nlp import process_keywords, control_tone
from app.models.description import ProductDescription

router = APIRouter()

class DescriptionRequest(BaseModel):
    product_name: str
    features: List[str]
    keywords: Optional[List[str]] = None
    tone: Optional[str] = "neutral"
    language: str = "en"

class DescriptionResponse(BaseModel):
    description: str

@router.post("/generate", response_model=DescriptionResponse)
async def create_description(request: DescriptionRequest):
    try:
        processed_keywords = process_keywords(request.keywords)
        tone_controlled_text = control_tone(request.tone)
        
        description = await generate_product_description(
            product_name=request.product_name,
            features=request.features,
            keywords=processed_keywords,
            tone=tone_controlled_text,
            language=request.language
        )
        
        return DescriptionResponse(description=description)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))