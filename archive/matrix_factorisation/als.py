import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator


spark = SparkSession.builder.appName("Spark_ML_Pipeline").getOrCreate()

# Load the dataset
df = spark.read.csv("data/books_ratings.csv", header=True, inferSchema=True)

# Preprocess data
indexer = StringIndexer(inputCol="reviewerID", outputCol="reviewerID_index")
df = indexer.fit(df).transform(df)

# Convert userId and bookId into numerical indices
user_indexer = StringIndexer(inputCol="userId", outputCol="userIndex")
book_indexer = StringIndexer(inputCol="bookId", outputCol="bookIndex")

# Assemble features into a vector
assembler = VectorAssembler(inputCols=["userIndex", "bookIndex"], outputCol="features")

# Split data into training and test sets
(training, test) = df.randomSplit([0.8, 0.2], seed=42)


# Define the ALS model
als = ALS(
    maxIter=10,
    regParam=0.01,
    userCol="userIndex",
    itemCol="bookIndex",
    ratingCol="rating",
    coldStartStrategy="drop",
)

# Create a pipeline
pipeline = Pipeline(stages=[user_indexer, book_indexer, als])
model = pipeline.fit(training)

# Make predictions
predictions = model.transform(test)

# Evaluate the model
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Bonus: Experiment with different ALS hyperparameters
als_tuned = ALS(
    maxIter=15, regParam=0.05, rank=30, 
    userCol="userIndex", itemCol="bookIndex", ratingCol="rating", coldStartStrategy="drop"
)

# Retrain the model
model_tuned = als_tuned.fit(training)
predictions_tuned = model_tuned.transform(test)
rmse_tuned = evaluator.evaluate(predictions_tuned)
print(f"Tuned RMSE: {rmse_tuned:.2f}")