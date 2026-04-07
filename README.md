# DevOps Candidate Assignment - Agnos

## Architecture Overview
This project consists of a containerized API service (FastAPI) and a background worker service. Both are deployed on Kubernetes with high availability and automated CI/CD.

## Setup & Usage
1. **Docker:** Build images using `docker build -t api-service ./api`.
2. **Kubernetes:** Deploy using `kubectl apply -f k8s/`.
3. **CI/CD:** Automated via GitHub Actions in `.github/workflows/main.yml`.

## Failure Scenario Handling
* [cite_start]**API crashes during peak hours:** Kubernetes will auto-restart pods via Liveness Probes and scale out using HPA[cite: 28, 29].
* [cite_start]**Worker fails and infinitely retries:** We track high error rates via Prometheus alerts and perform rollbacks if needed[cite: 41, 52].
* [cite_start]**Bad deployment is released:** Immediate rollback using `kubectl rollout undo`[cite: 45].
* [cite_start]**Kubernetes node goes down:** Pods are automatically rescheduled to healthy nodes[cite: 46].