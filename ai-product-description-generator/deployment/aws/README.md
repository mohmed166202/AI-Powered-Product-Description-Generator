# AI-Powered Product Description Generator - AWS Deployment Documentation

This README file provides instructions and information for deploying the AI-Powered Product Description Generator on AWS.

## Prerequisites

Before deploying the application, ensure you have the following:

- An AWS account
- AWS CLI installed and configured
- Docker installed
- Docker Compose installed

## Deployment Steps

1. **Clone the Repository**
   Clone the repository to your local machine:
   ```
   git clone <repository-url>
   cd ai-product-description-generator/deployment/aws
   ```

2. **Configure Environment Variables**
   Create a `.env` file in the `aws` directory and set the necessary environment variables, including API keys and other configurations required for the application.

3. **Build Docker Images**
   Use Docker Compose to build the application images:
   ```
   docker-compose build
   ```

4. **Run Docker Containers**
   Start the application using Docker Compose:
   ```
   docker-compose up
   ```

5. **Deploy to AWS ECS**
   - Create an ECS cluster in the AWS Management Console.
   - Use the `ecs-task-definition.json` file to register a new task definition in ECS.
   - Launch the task in your ECS cluster.

6. **Access the Application**
   Once the application is running, you can access it via the public IP or domain name assigned to your ECS service.

## Additional Information

- For more details on the application architecture and components, refer to the main project README file located in the root directory.
- Ensure that your AWS security groups and IAM roles are configured correctly to allow access to the necessary services.

## Troubleshooting

If you encounter issues during deployment, check the following:

- Ensure that all environment variables are set correctly.
- Review the logs from the Docker containers for any error messages.
- Verify that your AWS resources (ECS, IAM, etc.) are properly configured.

## Support

For further assistance, please open an issue in the repository or contact the project maintainers.