from pyspark.sql import *
from pyspark.sql.functions import explode, col, asc, countDistinct


spark = SparkSession \
 .builder \
 .appName("Python Dataframe basic example") \
 .getOrCreate()

# Create Example Data - Departments and Employees


# Create the Employees

employees = []

Employee = Row("firstName", "lastName", "email", "salary")
employees.append(Employee('michael', 'armbrust', 'no-reply@berkeley.edu', 100000))
employees.append(Employee('xiangrui', 'meng', 'no-reply@stanford.edu', 120000))
employees.append(Employee('matei', None, 'no-reply@waterloo.edu', 140000))
employees.append(Employee(None, 'wendell', 'no-reply@berkeley.edu', 160000))
employees.append(Employee('michael', 'jackson', 'no-reply@neverla.nd', 80000))

df1 = spark.createDataFrame(employees)

df1.show()

