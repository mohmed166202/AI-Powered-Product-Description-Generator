from typing import List, Dict
import requests

class ShopifyService:
    def __init__(self, shop_name: str, api_key: str, password: str):
        self.shop_name = shop_name
        self.api_key = api_key
        self.password = password
        self.base_url = f"https://{self.api_key}:{self.password}@{self.shop_name}.myshopify.com/admin/api/2023-01"

    def get_products(self) -> List[Dict]:
        url = f"{self.base_url}/products.json"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('products', [])

    def get_product_by_id(self, product_id: int) -> Dict:
        url = f"{self.base_url}/products/{product_id}.json"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get('product', {})

    def create_product(self, product_data: Dict) -> Dict:
        url = f"{self.base_url}/products.json"
        response = requests.post(url, json={"product": product_data})
        response.raise_for_status()
        return response.json().get('product', {})

    def update_product(self, product_id: int, product_data: Dict) -> Dict:
        url = f"{self.base_url}/products/{product_id}.json"
        response = requests.put(url, json={"product": product_data})
        response.raise_for_status()
        return response.json().get('product', {})

    def delete_product(self, product_id: int) -> None:
        url = f"{self.base_url}/products/{product_id}.json"
        response = requests.delete(url)
        response.raise_for_status()