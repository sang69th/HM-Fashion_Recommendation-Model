# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT current_catalog() AS catalog_name;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS hm_fashion;
# MAGIC CREATE VOLUME IF NOT EXISTS hm_fashion.raw_data;

# COMMAND ----------

article_path = "/Volumes/workspace/hm_fashion/raw_data/articles.csv"

articles = spark.read.options(
    header=True,
    inferSchema=False,
    multiLine=True,
    escape='"'
).csv(article_path)

display(
    articles.select(
        "article_id",
        "prod_name",
        "product_type_name",
        "colour_group_name",
        "detail_desc"
    ).limit(5)
)

# COMMAND ----------

articles.count()


# COMMAND ----------

articles.columns
len(articles.columns)
