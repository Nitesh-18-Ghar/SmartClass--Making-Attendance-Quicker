import streamlit as st

def header_home():          # BY default h2 use karta hai

    logo_url = "https://static.vecteezy.com/system/resources/previews/014/604/541/non_2x/smart-education-logo-design-vector.jpg"

    st.markdown(f""" 
        <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 0.5px; margin-top: 30px;'>
           <img src='{logo_url}' style='height:100px'/>
           <h1 style='text-align: center;'>SMART CLASS</h1> 
        </div>
        """, unsafe_allow_html=True)  