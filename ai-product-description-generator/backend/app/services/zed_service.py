from fastapi import HTTPException
import requests

class ZedService:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_product_data(self, product_id: str):
        url = f"{self.base_url}/products/{product_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        return response.json()

    def upload_csv(self, csv_file_path: str):
        url = f"{self.base_url}/upload"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "multipart/form-data"
        }
        with open(csv_file_path, 'rb') as file:
            response = requests.post(url, headers=headers, files={"file": file})

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())

        return response.json()