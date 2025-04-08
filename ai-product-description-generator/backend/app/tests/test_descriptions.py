from fastapi import HTTPException
from app.services.openai_service import OpenAIService
from app.models.description import ProductDescription
import pytest

@pytest.fixture
def openai_service():
    return OpenAIService()

def test_generate_product_description(openai_service):
    product_data = {
        "title": "Wireless Headphones",
        "features": ["Noise Cancelling", "Bluetooth 5.0", "20-hour battery life"],
        "keywords": ["headphones", "wireless", "audio"],
        "language": "en"
    }
    
    description = openai_service.generate_description(product_data)
    
    assert isinstance(description, str)
    assert len(description) > 0
    assert "Wireless Headphones" in description

def test_generate_product_description_arabic(openai_service):
    product_data = {
        "title": "سماعات رأس لاسلكية",
        "features": ["إلغاء الضوضاء", "بلوتوث 5.0", "عمر بطارية 20 ساعة"],
        "keywords": ["سماعات", "لاسلكية", "صوت"],
        "language": "ar"
    }
    
    description = openai_service.generate_description(product_data)
    
    assert isinstance(description, str)
    assert len(description) > 0
    assert "سماعات رأس لاسلكية" in description

def test_invalid_product_data(openai_service):
    product_data = {
        "title": "",
        "features": [],
        "keywords": [],
        "language": "en"
    }
    
    with pytest.raises(HTTPException) as exc_info:
        openai_service.generate_description(product_data)
    
    assert exc_info.value.status_code == 400
    assert "Invalid product data" in str(exc_info.value.detail)