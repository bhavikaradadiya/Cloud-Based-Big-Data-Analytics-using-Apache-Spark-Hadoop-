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


### 2️⃣ Upload Dataset to Cloud Storage

gsutil cp dataset.json gs://your-bucket/raw/

### 3️⃣ Copy Data to HDFS

hdfs dfs -mkdir /data
hdfs dfs -copyFromLocal dataset.json /data/

---

## 🗂 Hadoop MapReduce Job

Example run:

hadoop jar wordcount.jar /data/dataset.json /output/wordcount 

Code available in:

src/mapreduce/


---
## 🔥 Spark Analysis Job

Submit PySpark job:

gcloud dataproc jobs submit pyspark src/spark/spark_analysis.py --cluster=yourcluster

Outputs stored in HDFS.

---

## 🤖 Machine Learning – Logistic Regression (Spark MLlib)

Used for binary sentiment classification

Accuracy: 87%

Metrics used: Precision, Recall, F1-Score

Balanced on 80/20 train-test split

Notebook:

notebooks/model_training.ipynb

---

## 📊 Visualizations

Place generated images in:

images/

Examples:

Positive vs negative sentiment distribution

Rating trends

Verified vs non-verified purchase comparison

---

## 📌 Key Insights

Negative reviews help identify product weaknesses

Sentiment data improves product recommendation systems

Helps in inventory and supply chain optimization

Detects unusual/fake reviews

Real-time insights enhance customer satisfaction

---

## 👩‍💻 Author

Bhavikaben Radadiya
MSc Data Analytics – 2025
GitHub:https://github.com/bhavikaradadiya

## 📜 License

This project is licensed under the MIT License.
See the LICENSE file for details.
