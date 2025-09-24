import streamlit as st

st.title("Hello coders!")
st.subheader("How are you all! I hope all you doing Fine!")
st.text("Today you are choosing you favourite coding language")

language = st.selectbox("Select your favourite language:",["Python","Java","C","C++","JavaScript","HTML","CSS"])
st.text(f"You choose {language}.Excellent selection")

st.success(f"You select {language}")