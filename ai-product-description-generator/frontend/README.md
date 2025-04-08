# AI-Powered Product Description Generator

This project is an AI-Powered Product Description Generator that utilizes the OpenAI GPT-4 API to generate engaging product descriptions in both Arabic and English. The application is built using FastAPI for the backend and React with Tailwind CSS for the frontend.

## Features

- **AI-Powered Descriptions**: Generate product descriptions using advanced NLP techniques.
- **Multi-Language Support**: Supports both Arabic and English languages.
- **E-commerce Integrations**: Integrates with Shopify, WooCommerce, Salla, and Zed for seamless product data management.
- **Customizable Dashboard**: Provides a user-friendly dashboard for managing product descriptions and settings.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Node.js and npm
- AWS account for deployment

### Backend Setup

1. Navigate to the `backend` directory.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Deployment

For deployment instructions, refer to the `deployment/aws/README.md` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.