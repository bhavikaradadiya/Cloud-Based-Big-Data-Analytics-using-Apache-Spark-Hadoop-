# Cloud-Based Big Data Analytics using Apache Spark & Hadoop (Google Cloud Dataproc)

This project implements end-to-end Big Data Analytics using **Google Cloud Dataproc**, **Hadoop MapReduce**, **Apache Spark**, and **Spark MLlib** on the **Amazon Reviews 2023 dataset**.  
It is developed as part of the MSc Data Analytics coursework.

---

## 📌 Project Overview

The objective of this project is to solve an e-commerce business problem—customer sentiment analysis and trend identification—using Big Data tools and cloud technologies.

This repository contains:

- Google Cloud Dataproc setup documentation  
- Hadoop MapReduce data preprocessing  
- Apache Spark data engineering & analytics  
- Logistic Regression ML model using Spark MLlib  
- Performance comparison of MapReduce vs Spark  
- Visualizations & insights  

---

---

## 🚀 Technologies Used

- Google Cloud Platform  
  - Dataproc  
  - Cloud Storage (GCS)  
- Hadoop MapReduce  
- Apache Spark (PySpark)  
- Spark MLlib  
- Python 3.x  

---

## 📁 Dataset – Amazon Reviews 2023

- Size: **>10GB**  
- Source: Public GitHub Dataset  
- Contains:  
  - Product ID  
  - Customer ID  
  - Review Text  
  - Rating  
  - Timestamp  
  - Verified Purchase  
  - Sentiment  

⚠️ Due to size, the dataset is **not included** in this repository.  
Upload it to **Google Cloud Storage (GCS)** and access it from there.

---

## ⚙️ Cloud Architecture

<img width="1536" height="1024" alt="cloud Architecture" src="https://github.com/user-attachments/assets/04ff5408-925c-4758-8541-64d9fa93112c" />

---

## 🔧 Setup & Execution

### 1️⃣ Create and Configure Dataproc Cluster  
- Enable APIs  
- Create bucket  
- Configure master and worker nodes  
- Choose appropriate machine types

---

### 2️⃣ Upload Dataset to Cloud Storage

```bash
gsutil cp dataset.json gs://your-bucket/raw/








