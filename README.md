# Cloud-Based Big Data Analytics Using Apache Spark & Hadoop on Google Cloud Dataproc

This project implements end-to-end Big Data analytics using **Google Cloud Dataproc**, **Hadoop MapReduce**, **Apache Spark**, and **Spark MLlib** to analyze the **Amazon Reviews 2023** dataset.  
This work is part of the *MSc Data Analytics (2025)* coursework by **Bhavikaben Bavchandbhai Radadiya**.

---

## 📌 Project Overview

The goal of this project is to address a real-world e-commerce business problem:  
**Customer sentiment analysis, product trend discovery, and behavior analysis** using large-scale datasets processed on a cloud platform.

The project includes:

- Google Cloud Dataproc cluster setup  
- Hadoop MapReduce for preprocessing  
- Apache Spark for data analysis  
- Logistic Regression using Spark MLlib  
- Performance comparison (MapReduce vs Spark)  
- Business insights and visualizations  

---

## 📁 Dataset Information

**Dataset Name:** Amazon Reviews 2023  
**Size:** >10 GB  
**Source:** GitHub (Public Dataset)  

**Fields Included:**
- Product ID  
- Customer ID  
- Review Text  
- Rating (1-5)  
- Timestamp  
- Verified Purchase  
- Sentiment  

Because of its large size, the dataset was stored and processed through:
- **Google Cloud Storage bucket:** `mybucket15560`  
- **Google Cloud Dataproc HDFS (for Hadoop & Spark jobs)**  

---

## 🏗 Cloud Infrastructure (Google Cloud)

### **Bucket Name (Used in the Project):**

mybucket15560


### **Dataproc Cluster (Configuration Used):**
| Component | Configuration |
|----------|---------------|
| Region | europe-west4 |
| Zone | europe-west4-a |
| Cluster Mode | Standard |
| Master Node | n1-standard-4 |
| Worker Nodes | n1-standard-2 |
| Preemptible Workers | 2 |
| Autoscaling | Enabled (min 2, max 10) |

---

## 🔧 Setup Instructions

### **1️⃣ Create Google Cloud Project**
- Sign in to Google Cloud Console  
- Create a new project  
- Link billing  


### **2️⃣ Enable Required APIs**
- Dataproc API
- Compute Engine API  
- Cloud Storage API  


### **3️⃣ Create Cloud Storage Bucket**
Bucket created in this project:


mybucket15560


### **4️⃣ Upload Dataset to Storage**
  
gsutil cp amazon_reviews_2023.json gs://mybucket15560/


### **5️⃣ Create the Dataproc Cluster**
Using UI or gcloud command:


gcloud dataproc clusters create mycluster \
    --region=europe-west4 \
    --zone=europe-west4-a \
    --master-machine-type=n1-standard-4 \
    --worker-machine-type=n1-standard-2 \
    --num-workers=2

---

## 📥 HDFS Data Upload

SSH into Master Node:

hdfs dfs -mkdir /amazon_data
hdfs dfs -copyFromLocal amazon_reviews_2023.json /amazon_data
hdfs dfs -ls /amazon_data

---

## 🗂 Hadoop MapReduce Job

File Used: wordcount.py

Run MapReduce:  
python wordcount.py amazon_reviews_2023.json > wordcount_output.txt

**OR using Hadoop:**

hdfs dfs -cat /user/hadoop/wordcount_output.txt | head

**Purpose:**

Remove anomalies

Word frequency extraction

Base text preprocessing

---
## 🔥 Apache Spark Job (PySpark)

File Used: spark_analysis.py

Run via Dataproc:

gcloud dataproc jobs submit pyspark spark_analysis.py --cluster=mycluster

**Outputs:**

Verified purchase filtering

Average ratings

Top-rated products

Exploratory analytics

---
## 🤖 Machine Learning (Spark MLlib)

ML Script: logistic_regression.py

Model: Logistic Regression

Accuracy Achieved: 87%

Metrics Used: Accuracy, Precision, Recall, F1-Score

**Steps performed:**

Tokenization

Stopword removal

TF-IDF feature extraction

Train-test split (80/20)

Binary sentiment prediction

Model evaluation

---
## 📊 Visualizations & Insights

**Generated visualizations include:**

Positive vs Negative review distribution

Rating distributions

Category-wise sentiment trends


**Place plots in:**

Result/

---
## 📌 Key Business Insights

Negative reviews highlight product defects

Useful for improving recommendation systems

Helps inventory management

Detects fake/unusual reviews

Real-time sentiment shifts support marketing decisions

---

## 👩‍💻 Author

Bhavikaben Bavchandbhai Radadiya

MSc Data Analytics — 2025

GitHub Repository:
(https://github.com/bhavikaradadiya/Cloud-Based-Big-Data-Analytics-using-Apache-Spark-Hadoop)

---
## 📜 License

This project uses the MIT License (see LICENSE file)

