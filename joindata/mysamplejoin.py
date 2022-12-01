
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:20:19 2020
@author: prabha
"""

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

## https://www.learnbymarketing.com/1100/pyspark-joins-by-example/

# Setting up the Data in Pyspark

valuesA = [('Pirate',1),('Monkey',2),('Ninja',3),('Spaghetti',4)]
TableA = spark.createDataFrame(valuesA,['name','id'])
 
valuesB = [('Rutabaga',1),('Pirate',2),('Ninja',3),('Darth Vader',4)]
TableB = spark.createDataFrame(valuesB,['name','id'])
 
TableA.show()
TableB.show()

ta = TableA.alias('ta')
tb = TableB.alias('tb')

# Pyspark Inner Join Example
