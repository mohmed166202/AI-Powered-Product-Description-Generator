# AI-Powered Product Description Generator Deployment Documentation

## Overview
This document provides guidelines for deploying the AI-Powered Product Description Generator application on AWS. The application utilizes FastAPI for the backend, integrates with various e-commerce platforms, and supports both Arabic and English languages.

## Deployment Steps

1. **Prerequisites**
   - Ensure you have an AWS account.
   - Install Docker and Docker Compose on your local machine.
   - Configure AWS CLI with appropriate permissions.

2. **Clone the Repository**
   Clone the project repository to your local machine:
   ```
   git clone <repository-url>
   cd ai-product-description-generator
   ```

3. **Docker Setup**
   Navigate to the `deployment/aws` directory and run the following command to build and start the Docker containers:
   ```
   docker-compose up --build
   ```

4. **ECS Task Definition**
   The ECS task definition is defined in `ecs-task-definition.json`. You can register this task definition using the AWS CLI:
   ```
   aws ecs register-task-definition --cli-input-json file://ecs-task-definition.json
   ```

5. **Deploying to ECS**
   Create a new ECS service using the registered task definition. Ensure that you have a suitable cluster set up in AWS ECS.

6. **Accessing the Application**
   Once deployed, you can access the application via the public IP or domain name assigned to your ECS service.

## Additional Information
- For detailed information on the backend setup, refer to the `backend/README.md`.
- For frontend deployment instructions, see `frontend/README.md`.

## Support
For any issues or questions regarding the deployment process, please contact the development team or refer to the project's issue tracker on GitHub.