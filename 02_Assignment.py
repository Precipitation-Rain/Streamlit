import streamlit as st
import datetime

st.title("Age Calculator")
today = datetime.date.today()
min_date = today.replace(year=today.year - 120)
max_date = today

dob = st.date_input(
    "Select your Date of Birth",
    value=datetime.date(2000, 1, 1),   # default value
    min_value=min_date,
    max_value=max_date
)

age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

st.write(f"Your age is: {age} years")

