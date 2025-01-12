Explanation of all PySpark RDD, DataFrame and SQL examples present on this project are available at [Apache PySpark Tutorial](https://sparkbyexamples.com/pyspark-tutorial/), All these examples are coded in Python language and tested in our development environment.


##  SparkSession

SparkSession also includes all the APIs available in different contexts –

```
SparkContext,
SQLContext,
StreamingContext,
HiveContext.

```



##  Docs
- https://sparkbyexamples.com/pyspark-tutorial/
- https://sparkbyexamples.com/pyspark/pyspark-what-is-sparksession/

## Install

```

JAVA_HOME = C:\Program Files\Java\jdk1.8.0_201
PATH = %PATH%;C:\Program Files\Java\jdk1.8.0_201\bin


SPARK_HOME  = C:\apps\spark-3.0.0-bin-hadoop2.7
HADOOP_HOME = C:\apps\spark-3.0.0-bin-hadoop2.7
PATH=%PATH%;C:\apps\spark-3.0.0-bin-hadoop2.7\bin

** Spark Shell + Web UI
- $SPARK_HOME/sbin/pyspark

Spark-shell also creates a Spark context web UI and by default, it can access from http://localhost:4041.



```

* Spark
```
scala -version
spark-submit --version
spark-shell --version
spark-sql --version
```

* Jupyter  notebook
```
pip install jupyter
jupyter notebook


```

## The spark-submit

```
The spark-submit command is a utility to run or submit a Spark or PySpark application program (or job) to the cluster by specifying options and configurations, the application you are submitting can be written in Scala, Java, or Python (PySpark). spark-submit command supports the following.

Submitting Spark application on different cluster managers like Yarn, Kubernetes, Mesos, and Stand-alone.
Submitting Spark application on client or cluster deployment modes.
```

```
 spark-3.0.1-bin-hadoop3.2/bin/spark-submit test.py
 ```

# Create SparkSession from builder

```scala

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]") \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()

```

# Table of Contents (Spark Examples in Python)

# PySpark Basic Examples
- [How to create SparkSession](https://sparkbyexamples.com/pyspark/pyspark-what-is-sparksession/)
- [PySpark – Accumulator](https://sparkbyexamples.com/pyspark/pyspark-accumulator-with-example/)
- [PySpark Repartition vs Coalesce](https://sparkbyexamples.com/pyspark/pyspark-repartition-vs-coalesce/)
- [PySpark Broadcast variables](https://sparkbyexamples.com/pyspark/pyspark-broadcast-variables/)
- [PySpark – repartition() vs coalesce()](https://sparkbyexamples.com/pyspark/pyspark-repartition-vs-coalesce/)
- [PySpark – Parallelize](https://sparkbyexamples.com/pyspark/pyspark-parallelize-create-rdd/)
- [PySpark – RDD](https://sparkbyexamples.com/pyspark-rdd)
- [PySpark – Web/Application UI](https://sparkbyexamples.com/spark/spark-web-ui-understanding/)
- [PySpark – SparkSession](https://sparkbyexamples.com/pyspark/pyspark-what-is-sparksession/)
- [PySpark – Cluster Managers](https://sparkbyexamples.com/pyspark-tutorial/#cluster-manager)
- [PySpark – Install on Windows](https://sparkbyexamples.com/pyspark-tutorial/#pyspark-installation)
- [PySpark – Modules & Packages](https://sparkbyexamples.com/pyspark-tutorial/#modules-packages)
- [PySpark – Advantages](https://sparkbyexamples.com/pyspark-tutorial/#advantages)
- [PySpark – Features](https://sparkbyexamples.com/pyspark-tutorial/#features)
- [PySpark – What is it? & Who uses it?](https://sparkbyexamples.com/pyspark/what-is-pyspark-and-who-uses-it/)


## PySpark DataFrame Examples 
- [PySpark – Create a DataFrame](https://sparkbyexamples.com/pyspark/different-ways-to-create-dataframe-in-pyspark/)
- [PySpark – Create an empty DataFrame](https://sparkbyexamples.com/pyspark/pyspark-create-an-empty-dataframe/)
- [PySpark – Convert RDD to DataFrame](https://sparkbyexamples.com/pyspark/convert-pyspark-rdd-to-dataframe/)
- [PySpark – Convert DataFrame to Pandas](https://sparkbyexamples.com/pyspark/convert-pyspark-dataframe-to-pandas/)
- [PySpark – StructType & StructField](https://sparkbyexamples.com/pyspark/pyspark-structtype-and-structfield/)
- [PySpark Row using on DataFrame and RDD](https://sparkbyexamples.com/pyspark/pyspark-row-using-rdd-dataframe/)
- [Select columns from PySpark DataFrame ](https://sparkbyexamples.com/pyspark/select-columns-from-pyspark-dataframe/)
- [PySpark Collect() – Retrieve data from DataFrame](https://sparkbyexamples.com/pyspark/pyspark-collect/)
- [PySpark withColumn to update or add a column](https://sparkbyexamples.com/pyspark/pyspark-withcolumn/)
- [PySpark using where filter function ](https://sparkbyexamples.com/pyspark/pyspark-where-filter/)
- [PySpark – Distinct to drop duplicate rows ](https://sparkbyexamples.com/pyspark/pyspark-distinct-to-drop-duplicates/)
- [ PySpark orderBy() and sort() explained](https://sparkbyexamples.com/pyspark/pyspark-orderby-and-sort-explained/)
- [PySpark Groupby Explained with Example](https://sparkbyexamples.com/pyspark/pyspark-groupby-explained-with-example/)
- [PySpark Join Types Explained with Examples](https://sparkbyexamples.com/pyspark/pyspark-join/)
- [PySpark Union and UnionAll Explained](https://sparkbyexamples.com/pyspark/pyspark-union-and-unionall/)
- [PySpark UDF (User Defined Function)](https://sparkbyexamples.com/pyspark/pyspark-udf-user-defined-function/)
- [PySpark flatMap() Transformation](https://sparkbyexamples.com/pyspark/pyspark-flatmap-transformation/)
- [PySpark map Transformation](https://sparkbyexamples.com/pyspark/pyspark-map-transformation/)


## PySpark SQL Functions
- [PySpark Aggregate Functions with Examples](https://sparkbyexamples.com/pyspark/pyspark-aggregate-functions/)
- [PySpark Window Functions](https://sparkbyexamples.com/pyspark/pyspark-window-functions/)


## PySpark Datasources
- [PySpark Read CSV file into DataFrame](https://sparkbyexamples.com/pyspark/pyspark-read-csv-file-into-dataframe/)
- [PySpark read and write Parquet File ](https://sparkbyexamples.com/pyspark/pyspark-read-and-write-parquet-file/)

