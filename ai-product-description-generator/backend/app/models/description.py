from pydantic import BaseModel, Field
from typing import Optional, List

class ProductDescription(BaseModel):
    title: str = Field(..., description="The title of the product")
    features: List[str] = Field(..., description="A list of features of the product")
    benefits: List[str] = Field(..., description="A list of benefits of the product")
    keywords: Optional[List[str]] = Field(None, description="Keywords for SEO optimization")
    language: str = Field(..., description="The language of the description (e.g., 'en' for English, 'ar' for Arabic")
    tone: Optional[str] = Field("neutral", description="The tone of the description (e.g., 'formal', 'casual', 'enthusiastic')")

    class Config:
        schema_extra = {
            "example": {
                "title": "Wireless Headphones",
                "features": ["Noise Cancelling", "20-hour battery life", "Bluetooth 5.0"],
                "benefits": ["Enjoy music without distractions", "Long-lasting use", "Seamless connectivity"],
                "keywords": ["headphones", "wireless", "audio"],
                "language": "en",
                "tone": "enthusiastic"
            }
        }