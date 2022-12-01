
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:20:19 2020
@author: prabha
"""

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()


