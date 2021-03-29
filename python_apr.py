#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:06:27 2021

@author: dobrea
"""
# Import some libraries
import math
import numpy_financial as npf
import subprocess
import sys

# Install numpy-financial
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("numpy-financial")

# Define calc_mortgage, which calculates monthly payment amount
def calc_mortgage(principal, interest, months):
    # monthly rate from annual percentage rate
    interest_rate = interest/(100 * 12)
    # total number of payments
    payment_num = months
    # calculate monthly payment
    payment = principal * \
        (interest_rate/(1-math.pow((1+interest_rate), (-payment_num))))
    return payment

# Enter values below
# principal - enter the loan amount
# interest  - enter interest rate as a percent, not a decimal
# months    - enter number of months in the loan term
# fees      - enter any origination fees or amount paid for discount points

principal = 100000
interest = 8
months = 36
fees = 1000

monthly_payment = round(calc_mortgage(principal, interest, months), 2)
total_amount = monthly_payment * months

# Calculate APR including origination fees
present_val = principal-fees

apr_val = round(npf.rate(months,-1*monthly_payment,present_val,0)*1200, 3)
print("Monthly payment = $", monthly_payment)
print("APR (%) = ", apr_val)





























