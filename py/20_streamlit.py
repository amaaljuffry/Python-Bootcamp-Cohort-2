# Date: 2025-11-17
# Streamlit Application in Python

#Open source python framework for building web apps and create UI
#rapid prototyping data apps
#pip install streamlit
#streamlit run app.py

import streamlit as st
import datetime 

st.title("Personal Dashboard")

#Sidebar for navigation
st.sidebar.header("Personal Dashboard")

name = st.sidebar.text_input("Enter your name:")
age = st.sidebar.number_input("Enter your age:", min_value=0, max_value=120, value=25)
favorite_color = st.sidebar.color_picker("Pick your favorite color:", "#00f900")
hobbies = st.sidebar.multiselect("Select your hobbies:", ["Reading", "Traveling", "Cooking", "Sports", "Music", "Gaming"], default=["Reading"]
)

#Main content
if name:
    st.header(f"Welcome, {name}!")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Age", f"{age} years old")
    with col2:
        st.metric("Hobbies", len(hobbies))
    with col3:
        birth_year = datetime.datetime.now().year - age
        st.metric("Birth Year", birth_year)
        
    #Display favorite color
    if hobbies:
        st.subheader("Your Hobbies:")
        for hobby in hobbies:
            st.write(f"- {hobby}")
            
    # fun fact 
    st.subheader("Fun Fact:")
    days_lived = age * 365
    st.write(f"You have lived for approximately {days_lived} days!")
    
else:
    st.info("Please enter your name in the sidebar to get started.")