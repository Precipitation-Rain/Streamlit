#basic streamlit
import streamlit as st

st.title("Hello Streamlit")
st.subheader("I am Rajvardhan Shewale")
st.text("I am pursuing undergraduate from RIT")
st.write("Choose the variety of chai")

chai = st.selectbox("Your favorite chai:",["Masala chai","Lemon Tea","Black Tea","Adrak Chai","Kesar Chai"])
st.write(f"You choose {chai}.Exllent choice!")
st.success(f"You choose {chai}")