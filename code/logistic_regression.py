from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF, StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.sql.functions import col
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder.appName("AmazonReviewSentiment").getOrCreate()

df = spark.read.json("hdfs:///user/hadoop/dataset.json")

df = df.filter(df.review_text.isNotNull())

df = df.withColumn("label", (col("rating") >= 4).cast("integer"))

tokenizer = Tokenizer(inputCol="review_text", outputCol="words")

stopwords_remover = StopWordsRemover(inputCol="words", outputCol="filtered_words")

hashing_tf = HashingTF(inputCol="filtered_words", outputCol="raw_features", numFeatures=10000)
idf = IDF(inputCol="raw_features", outputCol="features")

lr = LogisticRegression(featuresCol="features", labelCol="label")

pipeline = Pipeline(stages=[tokenizer, stopwords_remover, hashing_tf, idf, lr])

train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

model = pipeline.fit(train_data)

predictions = model.transform(test_data)

predictions.select("review_text", "prediction").show(10)


evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Model Accuracy: {accuracy:.2f}")

