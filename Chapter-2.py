#Weighits
import streamlit as st

st.title("Chai maker App!")
#Button
if st.button("Make chai"):
    st.write("Your chai is being prepared!")
#Checkbox
add_masala = st.checkbox("Add masala")

if add_masala:
  st.write("Masala Added")

#radio
chai_base = st.radio("Select the chai base",["Milk","Water","Almond Milk"])
st.write(f"You selected {chai_base} as a chai base")

#selectbox
flavour = st.selectbox("Slect Flavour:",["Adrak","Kesar","Kadak"])
st.write(f"You selected {flavour} flavour")

#slider
sugar_level = st.slider("Enter sugar level:", 0,5,2)
st.write(f"Your sugar level is {sugar_level}")

#number input
cups = st.number_input("How many cups:",min_value=1,max_value=10,step=1)
st.write(f"You ordered {cups} cup os Tea")

#text input
name = st.text_input("Enter your name")

if name:
   st.write(f"Welcome {name},Thanks for order!")

dob = st.date_input("Enter Date of birth")

if dob:
   st.write(f"Your dob is {dob}")