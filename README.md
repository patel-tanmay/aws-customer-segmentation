Retail Customer Segmentation with RFM Analysis (End-to-End on AWS)

This project builds an end-to-end customer segmentation pipeline using RFM (Recency, Frequency, Monetary) analysis, powered by Python, scikit-learn, and AWS SageMaker.
It automates the entire process — from raw data ingestion to deploying a real-time inference API — helping businesses identify high-value, loyal, and at-risk customers for personalized marketing.

📊 1. Project Overview

Customer segmentation is essential for data-driven marketing.
This project demonstrates how to:

Clean and preprocess 500K+ retail transactions

Derive RFM features for each customer

Apply K-Means clustering to segment customers

Deploy the trained model via a Dockerized Flask API on AWS SageMaker

Enable real-time scoring for new customers using /invocations endpoint

🧩 2. Architecture
        ┌─────────────────────────────┐
        │       Raw Data (S3)         │
        └────────────┬────────────────┘
                     │
                     ▼
        ┌─────────────────────────────┐
        │ Data Cleaning & RFM Feature │
        │ Engineering (Python, Pandas)│
        └────────────┬────────────────┘
                     │
                     ▼
        ┌─────────────────────────────┐
        │ K-Means Model Training      │
        │ (scikit-learn, joblib)      │
        └────────────┬────────────────┘
                     │
                     ▼
        ┌─────────────────────────────┐
        │  Model Serialization (.pkl) │
        │  + Scaler Save              │
        └────────────┬────────────────┘
                     │
                     ▼
        ┌─────────────────────────────┐
        │ Dockerized Flask API        │
        │ (inference.py + Dockerfile) │
        └────────────┬────────────────┘
                     │
                     ▼
        ┌─────────────────────────────┐
        │ AWS ECR → SageMaker Endpoint│
        │ Real-time Predictions (POST)│
        └─────────────────────────────┘

🧠 3. Key Features

✅ Data Engineering:

Processed 500K+ e-commerce transactions stored in AWS S3.

Engineered RFM features using pandas & numpy.

✅ Modeling:

Used K-Means clustering with optimal k determined via the elbow method.

Scaled data using StandardScaler for consistent clustering.

Persisted models with joblib for reproducibility.

✅ Deployment:

Created an inference API using Flask.

Containerized with Docker and pushed to AWS ECR.

Deployed on AWS SageMaker as a real-time inference endpoint.

✅ Business Insight:

Found top 20% of customers contributing ~60% of total revenue.

Enabled marketing teams to target loyal & at-risk customer groups efficiently.

⚙️ 4. Tech Stack
Category	Tools / Services
Languages	Python (3.9)
Libraries	pandas, numpy, scikit-learn, joblib, flask, gunicorn
Cloud Services	AWS S3, AWS ECR, AWS SageMaker
Containerization	Docker
Orchestration	SageMaker Studio
Version Control	Git + GitHub
📁 5. Project Structure
rfm_project/
│
├── data/
│   └── retail_dataset.csv
│
├── models/
│   ├── kmeans_model.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── rfm_analysis.ipynb
│
├── api/
│   └── app/
│       └── main.py            # FastAPI local testing API
│
├── docker_inference/
│   ├── inference.py           # Flask inference logic
│   ├── Dockerfile             # Container setup
│   ├── requirements.txt       # Dependencies
│
└── scripts/
    └── utils.py               # Helper functions

🚀 6. Steps to Reproduce
🧹 Step 1: Data Preparation
# Load and preprocess dataset
python notebooks/rfm_analysis.ipynb


Generates:

rfm_segments.csv in /outputs

Saved models in /models

🧠 Step 2: Train and Save Models
joblib.dump(kmeans_model, "models/kmeans_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

🐳 Step 3: Build Docker Image
cd docker_inference
docker build -t rfm-segmentation .

☁️ Step 4: Push to AWS ECR
aws ecr create-repository --repository-name rfm-segmentation
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin <account_id>.dkr.ecr.us-east-2.amazonaws.com
docker tag rfm-segmentation:latest <account_id>.dkr.ecr.us-east-2.amazonaws.com/rfm-segmentation:latest
docker push <account_id>.dkr.ecr.us-east-2.amazonaws.com/rfm-segmentation:latest

🧩 Step 5: Deploy on SageMaker
import sagemaker
from sagemaker.model import Model

model = Model(
    image_uri="<account_id>.dkr.ecr.us-east-2.amazonaws.com/rfm-segmentation:latest",
    role="<sagemaker_execution_role>"
)
predictor = model.deploy(initial_instance_count=1, instance_type="ml.m5.large")

🌐 Step 6: Test the Endpoint
import requests
response = requests.post(
    "https://<endpoint-url>/invocations",
    json={"recency": 5, "frequency": 12, "monetary": 400}
)
print(response.json())


Expected Output:

{
  "cluster": 2,
  "input_data": {"recency": 5, "frequency": 12, "monetary": 400}
}

📈 7. Results & Insights

3 key customer clusters identified:

Cluster 0: High-value loyal customers

Cluster 1: New/Occasional buyers

Cluster 2: At-risk or churned users

The top 20% customers drove ~60% revenue contribution.

Helped prioritize personalized campaigns and retention strategies.

🧱 8. Next Improvements

Integrate AWS Lambda for serverless batch scoring

Store predictions in AWS RDS or DynamoDB

Build a Power BI dashboard for segment visualization

🧑‍💻 Author

Tanmay Patel
Data Scientist | AWS + Python + Machine Learning
