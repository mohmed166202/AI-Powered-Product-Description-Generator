from fastapi import APIRouter, HTTPException
from typing import List, Dict
from app.services.shopify_service import ShopifyService
from app.services.woocommerce_service import WooCommerceService
from app.services.salla_service import SallaService
from app.services.zed_service import ZedService

router = APIRouter()

shopify_service = ShopifyService()
woocommerce_service = WooCommerceService()
salla_service = SallaService()
zed_service = ZedService()

@router.get("/shopify/products", response_model=List[Dict])
async def get_shopify_products():
    try:
        products = await shopify_service.fetch_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/woocommerce/products", response_model=List[Dict])
async def get_woocommerce_products():
    try:
        products = await woocommerce_service.fetch_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/salla/products", response_model=List[Dict])
async def get_salla_products():
    try:
        products = await salla_service.fetch_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/zed/products", response_model=List[Dict])
async def get_zed_products():
    try:
        products = await zed_service.fetch_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))