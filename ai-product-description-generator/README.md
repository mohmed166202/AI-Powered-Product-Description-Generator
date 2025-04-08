# AI-Powered Product Description Generator

## Overview
The AI-Powered Product Description Generator is a web application that utilizes the OpenAI GPT-4 API to generate product descriptions in both Arabic and English. The application incorporates advanced NLP techniques such as prompt engineering, keyword insertion, and tone control to create engaging and relevant product descriptions. It integrates with various e-commerce platforms including Shopify, WooCommerce, Salla, and Zed.

## Features
- **Multi-Language Support**: Generate product descriptions in Arabic and English.
- **Advanced NLP Techniques**: Utilize prompt engineering, keyword insertion, and tone control for high-quality descriptions.
- **E-commerce Integrations**: Seamlessly connect with Shopify, WooCommerce, Salla, and Zed to fetch product data.
- **FastAPI Backend**: A robust backend built with FastAPI for handling API requests and responses.
- **Frontend Dashboard**: A user-friendly dashboard built with React and Tailwind CSS for managing product descriptions and settings.

## Project Structure
```
ai-product-description-generator
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── api
│   │   │   ├── v1
│   │   │   │   ├── endpoints
│   │   │   │   │   ├── descriptions.py
│   │   │   │   │   └── integrations.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── core
│   │   │   ├── config.py
│   │   │   ├── nlp.py
│   │   │   └── utils.py
│   │   ├── models
│   │   │   └── description.py
│   │   ├── services
│   │   │   ├── openai_service.py
│   │   │   ├── shopify_service.py
│   │   │   ├── woocommerce_service.py
│   │   │   ├── salla_service.py
│   │   │   └── zed_service.py
│   │   ├── tests
│   │   │   ├── test_descriptions.py
│   │   │   └── test_integrations.py
│   │   └── __init__.py
│   ├── requirements.txt
│   └── README.md
├── frontend
│   ├── src
│   │   ├── components
│   │   │   ├── Dashboard.jsx
│   │   │   └── LanguageSelector.jsx
│   │   ├── pages
│   │   │   ├── Home.jsx
│   │   │   └── Settings.jsx
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── styles
│   │       └── tailwind.css
│   ├── package.json
│   ├── tailwind.config.js
│   └── README.md
├── deployment
│   ├── aws
│   │   ├── docker-compose.yml
│   │   ├── ecs-task-definition.json
│   │   └── README.md
│   └── README.md
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-product-description-generator
   ```

2. Navigate to the backend directory and install the required dependencies:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. Set up environment variables for API keys and configurations as specified in `backend/app/core/config.py`.

4. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

5. For the frontend, navigate to the frontend directory and install dependencies:
   ```
   cd frontend
   npm install
   ```

6. Start the frontend application:
   ```
   npm start
   ```

## Deployment
For deployment instructions, refer to the `deployment/aws/README.md` file.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.