# Product data audit

I started by checking `articles.csv` before building the recommender.

## Findings

The file contains 105,542 article records and 25 columns.

- Every article ID is unique.
- There are no duplicated rows.
- 416 articles have an empty description.
- The other columns have no empty or whitespace-only values. Placeholder values still need checking.

The catalogue includes product names, categories, colours, patterns and descriptions. It does not include purchase history, prices or stock availability.

## Decisions

Article IDs and product codes will be stored as text so their leading zeros are preserved.

Articles with missing descriptions will be kept because their other attributes may still be useful. The original file will remain unchanged.

## Next step

Check the purchase-history file and confirm that its article IDs match the catalogue.

This audit was run with Python with assistance from Codex. A reproducible audit script has not yet been added to the repository. No model has been trained.

## Data access

The source is the H&M Personalized Fashion Recommendations competition on Kaggle. Usage conditions still need to be reviewed and documented. Raw dataset files will not be uploaded here.
