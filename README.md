# civo-knowledge-graph-generator

A lightweight knowledge graph generator using FastAPI and Cytoscape.js

![Python](https://img.shields.io/badge/python-3.11-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview
This project is a knowledge graph generator that utilizes FastAPI for the backend and Cytoscape.js for visualizing the graphs in the frontend. It is designed to be lightweight and easy to deploy using Docker and Kubernetes.

## Tutorial Reference
This repository accompanies a tutorial article. You can read it [here](https://www.civo.com/learn/automated-knowledge-graph-generator).

## Prerequisites
- **Python**: Version 3.11
- **Docker**: Version 20.10 or higher
- **Kubernetes**: Version 1.21 or higher
- **Node.js**: For building frontend assets (if applicable)
- **Accounts**: Access to a Kubernetes cluster (e.g., GKE, EKS, AKS)

## Quick Start
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/civo-knowledge-graph-generator.git
   cd civo-knowledge-graph-generator
   ```
2. **Build the Docker images**:
   ```bash
   docker build -t knowledge-backend ./
   docker build -t knowledge-frontend ./frontend
   ```
3. **Set up environment variables** (create a `.env` file):
   ```bash
   echo "RELAXAI_API_KEY=your_api_key" >> .env
   echo "RELAXAI_API_URL=https://api.example.com" >> .env
   ```
4. **Deploy to Kubernetes**:
   ```bash
   kubectl apply -f kubernetes/
   ```
5. **Access the application**:
   - Use the external IP of the frontend service to access the application in your browser.

## Project Structure
```
.
├── .gitignore
├── Dockerfile
├── frontend
│   └── Dockerfile
├── requirements.txt
├── backend
│   └── main.py
├── frontend
│   └── index.html
└── kubernetes
    ├── backend-deployment.yaml
    ├── frontend-deployment.yaml
    ├── backend-service.yaml
    └── frontend-service.yaml
```

## Key Concepts
- **FastAPI**: A modern web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Cytoscape.js**: A JavaScript library for visualizing complex networks and graphs.
- **Docker & Kubernetes**: Tools for containerization and orchestration, allowing for scalable deployment of applications.

## Code Highlights
- **FastAPI Application**: The main FastAPI application in `backend/main.py` demonstrates how to handle API requests and process data for generating knowledge graphs.
- **Docker Configuration**: The `Dockerfile` for the backend shows how to create a lightweight containerized application with proper dependency management.
- **Kubernetes Deployment**: The YAML files in the `kubernetes` directory illustrate how to deploy the application in a Kubernetes environment, including service exposure and scaling.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
