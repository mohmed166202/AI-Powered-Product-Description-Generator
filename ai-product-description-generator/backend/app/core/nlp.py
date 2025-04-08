from transformers import pipeline
from langchain import PromptTemplate
from googletrans import Translator

class NLPProcessor:
    def __init__(self):
        self.translator = Translator()
        self.generator = pipeline('text-generation', model='gpt-4')

    def generate_description(self, product_info, language='en', tone='neutral', keywords=None):
        prompt = self.create_prompt(product_info, tone, keywords)
        description = self.generator(prompt, max_length=150)[0]['generated_text']
        
        if language != 'en':
            description = self.translate_description(description, language)
        
        return description

    def create_prompt(self, product_info, tone, keywords):
        base_prompt = f"Generate a product description for the following product: {product_info}. "
        tone_prompt = f"Make it sound {tone}. "
        
        if keywords:
            keyword_prompt = f"Include the following keywords: {', '.join(keywords)}. "
            return base_prompt + tone_prompt + keyword_prompt
        return base_prompt + tone_prompt

    def translate_description(self, description, target_language):
        translated = self.translator.translate(description, dest=target_language)
        return translated.text

    def insert_keywords(self, description, keywords):
        if keywords:
            for keyword in keywords:
                description += f" Also, it features {keyword}."
        return description.strip()