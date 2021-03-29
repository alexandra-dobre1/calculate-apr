#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:55:58 2021

@author: alexandradobre
"""
# Import libraries
import pandas as pd
import math
import os
import subprocess
import sys

# Install numpy-financial
def install(package):
   subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("numpy-financial")
import numpy_financial as npf

# Change directory
os.chdir('/Users/alexandradobre/Desktop/Python')

# Load in the data
df = pd.read_csv('loan_info.csv')
#df['index_col'] = df.index
#df = df[['index_col', 'loan_amount','total_fees','interest_rate', 'years','months']]
#df.set_index('index_col')
df.head()

# Generate present value variable
# present_val = loan amount - total_fees
present_val = df["loan_amount"] - df["total_fees"]
df["present_value"] = present_val
df.head()

# Define calc_monthly_payment, which calculates monthly payment amount
def calc_monthly_payment(principal, interest, months):
    
    # Interest rate
    interest_rate = interest/(100 * 12)
    
    # Total number of payments
    payment_num = months
        
    # Monthly payment
    payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))

    return payment

# Monthly payment var
df["monthly_pmt"]=0.0

for i in df.index:
    principal=df.at[i, 'loan_amount']
    interest=df.at[i, 'interest_rate']
    months=df.at[i, 'months']
    df.at[i, 'monthly_pmt'] = round(calc_monthly_payment(principal, interest, months),2)
    
df.head()

# APR variable
df["apr_value"]=0.0

for i in df.index:
    months = df.at[i, 'months']
    monthly_pmt = df.at[i, 'monthly_pmt']
    present_value = df.at[i, 'present_value']
    apr_val = round(npf.rate(months, -1*monthly_pmt, present_value,0)*1200,3)
    df.at[i, 'apr_value'] = apr_val
    
df.head()

df.to_csv('loan_info_with_apr.csv')