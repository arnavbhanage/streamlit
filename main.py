import streamlit as st
import time
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
    st.write(f"You have entered an expense of ₹{expense} in the category {category}.")


    with st.spinner("Analyzing your terrible spending habits..."):
        time.sleep(2)