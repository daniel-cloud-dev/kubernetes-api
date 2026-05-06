# Kubernetes Flask API Project

## 📌 Overview

This project demonstrates a containerized Flask API deployed on Kubernetes with production-like configurations.
It includes Ingress, ConfigMap, Secret, and Persistent Volumes, simulating a real-world environment.

---

## 🏗 Architecture

```
Client → Ingress → Service → Pods → Persistent Volume
```

---

## ⚙️ Technologies

* Kubernetes
* Docker
* Flask (Python)
* NGINX Ingress Controller

---

## 🚀 Features

* Containerized Flask API
* Kubernetes Deployment with multiple replicas
* Service (ClusterIP) for internal communication
* Ingress for external access
* ConfigMap for environment configuration
* Secret for sensitive data
* PersistentVolumeClaim for data persistence
* Liveness and Readiness Probes
* Rolling updates with zero downtime

---

## 📂 Project Structure

```
project-ks8/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   └── pvc.yaml
└── README.md
```

---

## 🛠 How to Run Locally (Kind)

### 1. Build Docker image

```bash
docker build -t flask-api .
```

### 2. Load image into Kind

```bash
kind load docker-image flask-api
```

### 3. Apply Kubernetes manifests

```bash
kubectl apply -f k8s/
```

### 4. Port-forward Ingress

```bash
kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80
```

### 5. Test application

```bash
curl -H "Host: flask.local" http://localhost:8080
```

---

## 🧪 Troubleshooting Scenarios

* **ImagePullBackOff** → image not loaded into Kind
* **Service without endpoints** → label mismatch
* **503 from Ingress** → backend not reachable
* **DNS issues** → missing host mapping or Host header

---

## 📚 Key Learnings

* Kubernetes core components and architecture
* Debugging real cluster issues
* Managing configuration with ConfigMaps and Secrets
* Implementing persistent storage
* Exposing applications with Ingress
* Handling rolling updates and health checks

---

## 📈 Future Improvements

* Deploy on AWS (EKS)
* Add CI/CD pipeline
* Use Terraform for infrastructure provisioning
* Implement HTTPS with TLS

