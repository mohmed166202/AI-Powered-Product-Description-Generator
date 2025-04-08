from fastapi import HTTPException
import requests

class SallaService:
    def __init__(self, api_key: str, base_url: str = "https://api.salla.sa/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def get_product_data(self, product_id: str):
        url = f"{self.base_url}/products/{product_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        
        return response.json()

    def update_product(self, product_id: str, product_data: dict):
        url = f"{self.base_url}/products/{product_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.put(url, headers=headers, json=product_data)
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        
        return response.json()