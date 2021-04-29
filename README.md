# calculate-apr
This repository contains Python code that generates fixed APR values given a subset of parameters.

## Order of steps

1. The file `loan_info.csv` contains (randomized) data with the following loan information fields:

    - **loan_amount:** the principal balance on the loan
    - **years:** the loan term in years
    - **months:** the loan term in months (`years` * 12)
    - **interest_rate:** the interest rate on the loan (in percentage points)
    - **total_fees:** the sum of all fees on the loan (including amount paid for discount points and other closing costs)
 
2. The script `loan_info.py` reads in the data from `loan_info.csv` and generates the APR values.
3. A new file, `loan_info_with_apr.csv`, is generated containing the APR values given the loan information. 

## Jupyter Notebook
This repository also includes the Jupyter notebook file `loan_info_cleaning.ipynb` which tests the ipynb format. It is under construction still.
