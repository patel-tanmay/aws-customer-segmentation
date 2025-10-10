# Retail Customer Segmentation with RFM Analysis (End-to-End AWS + ML Deployment)

## 📖 Introduction

This project focuses on building an **end-to-end Retail Customer Segmentation pipeline** using the **RFM (Recency, Frequency, Monetary)** framework.
The goal was to help the marketing team identify different customer segments — such as *Champions*, *Loyal Customers*, or *At-Risk* — to design better-targeted retention and engagement campaigns.

Unlike a typical offline notebook project, this one goes beyond analytics — the trained model was **containerized using Docker**, pushed to **Amazon ECR**, and **deployed as a real-time inference endpoint on Amazon SageMaker**, making the insights **production-ready**.

---

## 💼 Business Problem

E-commerce platforms often deal with a vast number of customers but lack visibility into **who their most valuable customers are**.
The marketing spend was being distributed uniformly across all users, leading to inefficient ROI.

**Objective:**

* Identify key customer segments based on behavioral and spending patterns.
* Enable data-driven marketing strategies that increase retention and revenue efficiency.

---

## 📊 Dataset

* **Source:** Public e-commerce retail dataset (~500K transactions).
* **Fields:** `CustomerID`, `InvoiceDate`, `Quantity`, `UnitPrice`, `Country`.
* **Derived Metrics:**

  * **Recency:** Days since the last purchase.
  * **Frequency:** Number of purchases made.
  * **Monetary:** Total revenue generated.

Data was uploaded to **Amazon S3**, cleaned and transformed using **AWS Glue and Python (pandas)**, and later queried using **AWS Athena** for validation.

---

## ⚙️ Methodology

1. **Data Preparation (ETL on AWS)**

   * Stored raw CSV files in **S3** and connected through **AWS Glue** for schema inference and cleaning.
   * Used **pandas** for feature engineering to compute RFM metrics.

2. **Feature Scaling & Transformation**

   * Log-transformed skewed variables (Recency, Frequency, Monetary).
   * Standardized features using `StandardScaler()` to prepare for clustering.

3. **Modeling (K-Means Clustering)**

   * Used **Elbow Method** and **Silhouette Score** to determine optimal clusters.
   * Trained a **K-Means model** to segment customers into interpretable groups:

     * *Champions*
     * *Loyal Customers*
     * *At-Risk Customers*
     * *Hibernating Customers*

4. **Model Saving & Deployment**

   * Serialized the trained model (`kmeans_model.pkl`) and scaler (`scaler.pkl`) using **joblib**.
   * Built a **Flask-based inference API** (`inference.py`) to handle real-time predictions.
   * Created a **Docker image** with all dependencies and pushed it to **Amazon ECR**.
   * Deployed the containerized model as a **real-time SageMaker Endpoint**, making it accessible via REST API.

---

## 🧰 Tech Stack

| Category                | Tools / Services                       |
| ----------------------- | -------------------------------------- |
| Data Storage            | Amazon S3                              |
| Data Cleaning & ETL     | AWS Glue, pandas                       |
| Modeling                | scikit-learn (K-Means, StandardScaler) |
| Model Serialization     | joblib                                 |
| API Framework           | Flask                                  |
| Containerization        | Docker                                 |
| Cloud Deployment        | Amazon SageMaker, ECR                  |
| Orchestration / Scripts | Python                                 |
| Visualization           | matplotlib, seaborn                    |

---

## 🚀 Results

* Created **4 key customer segments** that revealed strong revenue concentration —
  the **top 20% of customers generated nearly 60% of total revenue**.
* Delivered an **API-ready segmentation service**, deployable directly in production via SageMaker.
* Enabled potential marketing automation for high-value customer targeting and churn prevention.

Example API Input:

```json
{
  "recency": 15,
  "frequency": 12,
  "monetary": 540
}
```

Example API Output:

```json
{
  "cluster": 1,
  "input_data": {
    "recency": 15,
    "frequency": 12,
    "monetary": 540
  }
}
```

---

## 🧩 Project Structure

```
rfm_project/
│
├── api/
│   ├── app/
│   │   └── main.py                # FastAPI-based local testing API
│   ├── requirements.txt
│
├── docker_inference/
│   ├── Dockerfile                 # For containerization and SageMaker deployment
│   ├── inference.py               # Flask inference API
│   ├── models/                    # Contains trained model & scaler
│   └── requirements.txt
│
├── notebooks/
│   └── rfm_analysis.ipynb         # Core analysis & feature engineering
│
├── outputs/
│   └── rfm_segments.csv           # Final cluster results
│
└── scripts/
    └── utils.py                   # Helper functions
```

---

## 📈 Visual Insights

* Revenue vs. Cluster Size visualization showed a clear 80/20 pattern.
* RFM heatmaps helped validate cluster separation and customer behavior distribution.
* Segment-wise retention rates suggested strong opportunity in **cross-selling** and **loyalty campaigns**.

---

## 🧠 Key Learnings

* Understood how to **move from offline ML to deployable ML services** using AWS infrastructure.
* Learned the complete flow of **building, containerizing, and hosting** a machine learning model in SageMaker.
* Improved awareness of **IAM roles, ECR permissions**, and **endpoint troubleshooting** in production.
* Strengthened understanding of **data-to-decision pipelines** — from business framing to actionable insight.

---

## 🤝 Acknowledgements

This project was part of a continuous effort to bridge analytical insight with deployable machine learning.
Special thanks to the AWS documentation and open-source community for guidance on SageMaker and Docker deployment workflows.
