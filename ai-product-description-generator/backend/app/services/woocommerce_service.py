from fastapi import HTTPException
import requests

class WooCommerceService:
    def __init__(self, api_url: str, consumer_key: str, consumer_secret: str):
        self.api_url = api_url
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def get_product(self, product_id: int):
        response = requests.get(
            f"{self.api_url}/wp-json/wc/v3/products/{product_id}",
            auth=(self.consumer_key, self.consumer_secret)
        )
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

    def create_product(self, product_data: dict):
        response = requests.post(
            f"{self.api_url}/wp-json/wc/v3/products",
            json=product_data,
            auth=(self.consumer_key, self.consumer_secret)
        )
        if response.status_code != 201:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

    def update_product(self, product_id: int, product_data: dict):
        response = requests.put(
            f"{self.api_url}/wp-json/wc/v3/products/{product_id}",
            json=product_data,
            auth=(self.consumer_key, self.consumer_secret)
        )
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

    def delete_product(self, product_id: int):
        response = requests.delete(
            f"{self.api_url}/wp-json/wc/v3/products/{product_id}",
            auth=(self.consumer_key, self.consumer_secret)
        )
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()