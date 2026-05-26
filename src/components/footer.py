import streamlit as st

def footer_home():          # BY default h2 use karta hai

    logo_url = "https://i.ibb.co/jPrBJhM0/Ramniad-Logo.png"
    st.markdown(f""" 
        <div style='margin-top: 2rem; display: flex; gap: 6px; justify-content: center; align-items:center;'>
        <p style="font-weight: bold;"> Created with ❤️ by </p>
        <img src='{logo_url}' style='max-height:40px' />
        </div>
                """, unsafe_allow_html=True)  