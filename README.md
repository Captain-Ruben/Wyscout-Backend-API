---

# Wyscout Backend API

This backend API is designed for managing Wyscout export files, with MongoDB and a Swagger interface for easy API documentation and testing.

## Installation

### Requirements
- **Docker** and **Docker Compose** must be installed. You can download Docker from the official [Docker website](https://www.docker.com/).

### Quick Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/wyscout-backend.git
   cd wyscout-backend
   ```

2. **Start the application with Docker Compose:**

   Run the following command to spin up both the MongoDB database and the API:

   ```bash
   docker-compose up
   ```

   This will automatically download the necessary images and start the containers.

3. **Access the Swagger UI:**

   Once the application is up and running, you can access the Swagger UI at:

   ```
   http://localhost:8080/swagger
   ```

   Here you can explore and test all available API endpoints.

---
