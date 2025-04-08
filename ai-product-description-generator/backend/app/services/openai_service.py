from typing import Dict, Any
import openai
import os

class OpenAIService:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_product_description(self, product_data: Dict[str, Any], language: str = "en", tone: str = "neutral") -> str:
        prompt = self.create_prompt(product_data, tone, language)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']

    def create_prompt(self, product_data: Dict[str, Any], tone: str, language: str) -> str:
        description_template = f"Generate a product description for the following product:\n\n"
        description_template += f"Product Name: {product_data.get('name')}\n"
        description_template += f"Features: {', '.join(product_data.get('features', []))}\n"
        description_template += f"Tone: {tone}\n"
        description_template += f"Language: {language}\n\n"
        description_template += "Description:"
        return description_template
