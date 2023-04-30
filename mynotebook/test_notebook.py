# Databricks notebook source
dbutils.fs.ls("/databricks-datasets")

# COMMAND ----------

spark.read.format("csv").option("header","true").load("file:/Workspace/Repos/sridhar.kothalanka@microsoft.com/public/data/aircraft-rul/rul-dataset.csv").display()

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup privatelink.mydatastorage.blob.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup dbfslacxnj.privatelink.blob.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup dbfslacxnj.dfs.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup dbfslacxnj.blob.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup adblacxnjallowedstorage.blob.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup adblacxnjdeniedstorage.blob.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup adblacxnjmydatastorage.blob.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup adblacxnjmydatastorage.dfs.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup adblacxnjmydatastorage.blob.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup adblacxnjallowedstorage.dfs.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup adblacxnjallowedstorage.dfs.core.windows.net

# COMMAND ----------

# MAGIC %sh
# MAGIC nslookup adblacxnjallowedstorage.blob.core.windows.net
