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


## Purchase history

The full transactions_train.csv file was checked in chunks to limit memory use.

It contains 31,788,324 purchase records from 20 September 2018 to 22 September 2020, covering 1,362,281 customer IDs and 104,547 article IDs.

Checks completed:
- No empty or whitespace-only values in the five columns.
- All purchase dates parsed successfully.
- Every article ID matched an entry in articles.csv.
- All price values were numeric and positive.

There are 995 articles in the catalogue with no purchases in this file.

Repeated transaction rows have not yet been checked. Purchase records should not be counted as distinct orders. Price currency and scaling still need verification.

A possible evaluation split is to train on purchases before 16 September 2020 and test against purchases from 16–22 September 2020. This split has not yet been implemented.
