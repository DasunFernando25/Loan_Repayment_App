import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Gold Loan Calculator")

st.write("### Input Data")
col1, col2 = st.columns(2)
gold_value = col1.number_input("Gold Value", min_value=0, value=0)
deposit = col1.number_input("Deposit", min_value=0, value=0)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=0.0)
loan_term = col2.number_input("Loan Term (in months)", min_value=1, value=1)

# Calculate the repayments.
loan_amount = gold_value - deposit
number_of_payments = loan_term
monthly_loan_amount = loan_amount / number_of_payments
monthly_interest = (loan_amount/100) * interest_rate
monthly_payment = monthly_loan_amount + monthly_interest

# Display the repayments.
total_payments = monthly_payment * number_of_payments
total_interest = monthly_interest * number_of_payments

st.write("### Repayments")
col1, col2, col3 = st.columns(3)
col1.metric(label="Monthly Repayments", value=f"Rs.{monthly_payment:,.2f}")
col2.metric(label="Total Repayments", value=f"Rs.{total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"Rs.{total_interest:,.0f}")
