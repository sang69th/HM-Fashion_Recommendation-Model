# Progress

## First notebook: exploring articles

Created `hm_fashion.raw_data` in Databricks Free Edition and uploaded `articles.csv`.

The notebook reads the CSV with Spark, previews five articles, counts records and checks column names. The column count returned 25. Article IDs in the preview retained their leading zeros.

Saved the notebook in `notebooks/01_explore_articles.py`.

One observation: product names alone can be misleading. An article named “OP T-shirt (Idro)” is classified as a bra. Recommendations will need to consider categories and descriptions alongside names.

Next: practise filtering the catalogue, then load the purchase history.

No recommendation model has been built yet.
