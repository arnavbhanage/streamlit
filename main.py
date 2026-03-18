import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Hello and welcome to a finance dashboard")
st.write("You can use this dashboard to track your expenses, set budgets, and visualize your financial data.")

st.header("Expense Tracker")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello, {name}! Let's start tracking your expenses. ")

age= st.number_input("Enter your age: ", min_value=0)
if age:
    if age < 18:
        st.write("You are a minor. Please ask your guardian for help with managing your finances.")
    else:
        st.write("You are an adult. You can manage your finances independently.")

expense = st.number_input("Enter your expense amount: ", min_value=0.0)

category = st.selectbox("Select expense category: ", ["Food", "Transportation", "Entertainment", "Utilities", "Other"])
if expense and category:
    st.session_state.data.append({
        "Name": name,
        "Age": age,
        "Expense": expense,
        "Category": category
    })

    st.write(f"You have entered an expense of ₹{expense} in the category {category}.")   
if st.button("Add Expense"):
    if expense and category:
        st.session_state.data.append({
            "Name": name,
            "Age": age,
            "Expense": expense,
            "Category": category
        })
if "data" not in st.session_state:
    st.session_state.data = []
if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.subheader("Your Expenses Table")
    st.dataframe(df)

    category_sum = df.groupby("Category")["Expense"].sum()
    st.subheader("Spending by Category")
    st.bar_chart(category_sum)

if st.button("Reset Data"):
    st.session_state.data = []
    if "data" not in st.session_state:
        st.session_state.data = []

if len(st.session_state.data) > 0:
    df = pd.DataFrame(st.session_state.data)

    st.dataframe(df)

    category_sum = df.groupby("Category")["Expense"].sum()
    st.bar_chart(category_sum)
else:
    st.write("No data yet. Add some expenses first.")
    col1, col2 = st.columns(2)

uploaded_file = st.file_uploader(
    "Upload your expense file (CSV or Excel)", 
    type=["csv", "xlsx"]
)
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".csv"):
            df_uploaded = pd.read_csv(uploaded_file)
        else:
            df_uploaded = pd.read_excel(uploaded_file)

        st.subheader("Uploaded Data")
        st.dataframe(df_uploaded)

    except Exception as e:
        st.error(f"Error reading file: {e}")
        mode = st.radio("Choose input method:", ["Manual Entry", "Upload File"])
        if mode == "Manual Entry":
            st.write("Please enter your expenses manually using the form above.")
        else:
            st.write("Please upload a valid CSV or Excel file containing your expenses.")