# AI-Powered Product Description Generator

## Overview
The AI-Powered Product Description Generator is a web application that utilizes the OpenAI GPT-4 API to generate engaging and optimized product descriptions in both Arabic and English. The application incorporates advanced NLP techniques such as prompt engineering, keyword insertion, and tone control to enhance the quality of the generated content.

## Features
- **Multi-language Support**: Generate product descriptions in Arabic and English.
- **Integration with E-commerce Platforms**: Seamlessly integrates with Shopify, WooCommerce, Salla, and Zed for fetching product data.
- **Advanced NLP Techniques**: Utilizes prompt engineering, keyword insertion, and tone control for high-quality descriptions.
- **FastAPI Backend**: A robust backend built with FastAPI for handling requests and responses efficiently.
- **Dashboard**: A simple dashboard built with React and Tailwind CSS for managing and viewing product descriptions.

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

5. For the frontend, navigate to the `frontend` directory and install the dependencies:
   ```
   cd frontend
   npm install
   ```

6. Start the frontend application:
   ```
   npm start
   ```

## Usage
- Access the API endpoints for generating product descriptions and managing integrations through the FastAPI documentation at `http://localhost:8000/docs`.
- Use the frontend dashboard to interact with the application and view generated descriptions.

## Deployment
For deployment instructions, refer to the `deployment/aws/README.md` file.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.