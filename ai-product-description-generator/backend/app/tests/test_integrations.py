from fastapi import HTTPException
from httpx import AsyncClient
import pytest

@pytest.mark.asyncio
async def test_shopify_integration():
    async with AsyncClient() as client:
        response = await client.get("/api/v1/integrations/shopify")
        assert response.status_code == 200
        assert "products" in response.json()

@pytest.mark.asyncio
async def test_woocommerce_integration():
    async with AsyncClient() as client:
        response = await client.get("/api/v1/integrations/woocommerce")
        assert response.status_code == 200
        assert "products" in response.json()

@pytest.mark.asyncio
async def test_salla_integration():
    async with AsyncClient() as client:
        response = await client.get("/api/v1/integrations/salla")
        assert response.status_code == 200
        assert "products" in response.json()

@pytest.mark.asyncio
async def test_zed_integration():
    async with AsyncClient() as client:
        response = await client.get("/api/v1/integrations/zed")
        assert response.status_code == 200
        assert "products" in response.json()