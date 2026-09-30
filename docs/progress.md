# Progress

## First notebook: exploring articles

Created `hm_fashion.raw_data` in Databricks Free Edition and uploaded `articles.csv`.

The notebook reads the CSV with Spark, previews five articles, counts records and checks column names. The column count returned 25. Article IDs in the preview retained their leading zeros.

Saved the notebook in `notebooks/01_explore_articles.py`.

One observation: product names alone can be misleading. An article named “OP T-shirt (Idro)” is classified as a bra. Recommendations will need to consider categories and descriptions alongside names.

Next: practise filtering the catalogue, then load the purchase history.

No recommendation model has been built yet.

## Filtering by colour

Filtered the catalogue where `colour_group_name` equals `Black`.

Previewed five matching articles and counted 22,670 matching records, about 21.5% of the catalogue.

Practised:
- `=` to assign a name.
- `==` to compare values.
- `.filter()` to keep matching rows.
- `.select()` to choose columns.
- `.limit()` to preview a few rows.
- `.count()` to count records.

This count describes catalogue articles, not sales or customer preferences.

Combined colour and product-type filters using & (AND). Found 2,728 articles where colour_group_name is Black and product_type_name is Trousers
