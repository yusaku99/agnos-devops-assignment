# DevOps Candidate Assignment - Agnos

## 1. Architecture Overview
This project is designed as a production-ready system consisting of two main microservices:
* **API Service**: A FastAPI-based service handling web requests, health checks, and logging.
* **Worker Service**: A background processor responsible for updating record timestamps and other internal tasks.

Both services are containerized using Multi-stage Docker builds for optimization and deployed on Kubernetes with high availability (HA) and automated scaling.

## 2. Tech Stack
* **Application**: FastAPI (Python 3.9-slim).
* **Containerization**: Docker (Multi-stage builds).
* **Orchestration**: Kubernetes (Deployments, Services, HPA, Secrets).
* **CI/CD**: GitHub Actions.
* **Observability**: Structured JSON Logs, Prometheus (Metrics & Alerts).

## 3. Setup & Usage Instructions
### Docker
To build the container images locally:
```bash
docker build -t api-service ./api
docker build -t worker-service ./worker

#Kubernetes

To deploy the entire stack to your cluster:

# Apply secrets and configurations first
kubectl apply -f k8s/api-secret.yaml

# Apply the main services
kubectl apply -f k8s/api-deployment.yaml
kubectl apply -f k8s/api-service.yaml
kubectl apply -f k8s/worker-deployment.yaml
kubectl apply -f k8s/api-hpa.yaml

4. Configuration & CI/CD

    Environment Variables: Managed via Kubernetes Secrets and ConfigMaps to separate configurations for DEV, UAT, and PROD environments.

    CI/CD Pipeline: Our GitHub Actions workflow automates the following stages:

        Linting and code quality checks.

        Building multi-stage Docker images.

        Deployment to the Kubernetes cluster.

5. Failure Scenario Handling
Scenario	Resolution Strategy
API crashes during peak hours	Kubernetes automatically restarts failed pods via Liveness Probes. The Horizontal Pod Autoscaler (HPA) scales replicas up to 5 pods based on CPU utilization to handle load.
Worker fails and infinitely retries	We monitor high error rates and stalled workers via Prometheus alerts. Structured JSON logs allow for rapid troubleshooting of task failures.
Bad deployment is released	We utilize kubectl rollout undo for immediate rollback to the last stable version.
Kubernetes node goes down	Due to our High Availability design and Pod Anti-Affinity, Kubernetes automatically reschedules pods to remaining healthy nodes.
6. Observability

    Logging: Both services implement structured JSON logging to facilitate centralized log management and analysis.

    Monitoring: Metrics such as request latency and error rates are tracked, with automated alerts for high error rates or crash looping pods.