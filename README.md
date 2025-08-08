# 🩺 Medicare Prediction Model – Your First MLOps Project (FastAPI + Docker + K8s)

> 🎥 YouTube video for the project: **"Build Your First MLOps Project"**

This project helps you learn **Building and Deploying an ML Model** using a simple and real-world use case: predicting whether a person is diabetic based on health metrics. We’ll go from:

- ✅ Model Training
- ✅ Building the Model locally
- ✅ API Deployment with FastAPI
- ✅ Dockerization
- ✅ Kubernetes Deployment

---

## 📊 Problem Statement

Predict if a person is diabetic based on:
  - Average_Covered_Charges
  - Average_Total_Payments
  - Reimbursement_Rate
  - Total_Discharges
  - Total_Payment

We use a Random Forest Classifier trained on the **Pima Indians Medicare Dataset**.

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/kasimbasaragi/medicare-mlops.git
cd medicare-mlops
```

### 2. Create Virtual Environment

```
python3 -m venv .mlops
source .mlops/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

## Train the Model

```
python train.py
```

## Run the API Locally

```
uvicorn main:app --reload
```

### Sample Input for /predict

```
  "Average_Covered_Charges": 0,
  "Average_Total_Payments": 0,
  "Reimbursement_Rate": 0,
  "Total_Discharges": 5,
  "Total_Payment": 0
```

## Dockerize the API

## 1. Build the Docker Image

```
docker build -t kasimbasaragi/medicare:v1 .

```

## 2. Push Image to Docker Hub

docker login
docker push kasimbasaragi/medicare:v1



## ☸️ Deploy to Kubernetes

## Apply the Deployment YAML

kubectl apply -f k8s-deployment.yaml



## Check pod status:

kubectl get pods
kubectl logs <pod-name>


## 📁 File Structure

medicare-mlops/
│
├── train.py               # Training script to generate the model
├── main.py                # FastAPI app for prediction
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker instructions
├── .dockerignore          # Docker ignore rules
├── medicare_model.pkl     # Trained ML model (auto-generated after train.py)
└── medicare-deployment.yaml  # Kubernetes deployment file


## 🙌 Author
Project by Kashim Basaragi
Docker Hub: kasimbasaragi


## 📌 Notes
Make sure medicare_model.pkl is not ignored in .dockerignore.

Always run train.py before building the Docker image to include the model.

Confirm Docker image is pushed with the correct tag (e.g. v1) before Kubernetes deployment.


