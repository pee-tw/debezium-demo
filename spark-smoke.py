import pyspark

sc = pyspark.SparkContext("local[*]")

txt = sc.textFile("./Debezium_tutorial")
print(txt.count())

python_lines = txt.filter(lambda line: "debezium" in line.lower())
print(python_lines.count())
