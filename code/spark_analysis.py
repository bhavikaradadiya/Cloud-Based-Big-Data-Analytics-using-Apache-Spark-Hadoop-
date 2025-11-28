from pyspark.sql import SparkSession  
from pyspark.sql.functions import col, avg  
  
spark = SparkSession.builder.appName("AmazonReviewAnalysis").getOrCreate()  
  
df = spark.read.json("hdfs:///user/hadoop/dataset.json")  

verified_reviews = df.filter(col("verified_purchase") == True)  

product_ratings = verified_reviews.groupBy("asin").agg(avg("rating").alias("avg_rating"))  

top_products = product_ratings.orderBy(col("avg_rating").desc()).limit(10)  

top_products.show()

