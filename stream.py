import findspark

SPARK_VERSION = "3.3.0"
SCALA_VERSION = "2.12"

findspark.add_packages(
    ["org.apache.spark:spark-sql-kafka-0-10_" + SCALA_VERSION + ":" + SPARK_VERSION]
)
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("debezium-demo").getOrCreate()

df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "dbserver1.inventory.customers")
    .option("startingOffsets", "earliest")
    .option("includeHeaders", "true")
    .load()
    .selectExpr("CAST(value AS STRING)")
)

df.writeStream.format("console").outputMode("append").start().awaitTermination()
