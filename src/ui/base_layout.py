import streamlit as st

def style_base_home():
    st.markdown(""" 
    <style>
        .stApp {
            background: #d0e6ff !important;
        }
                
        .stApp div[data-testid="stColumn"]{
            background-color: #9c7bac !important;
            padding: 2rem !important;
            border-radius: 5rem !important;
        }
    </style>
    """, unsafe_allow_html=True)         # HTML ko allow krna padega

def style_base_dashboard():
    st.markdown(""" 
    <style>
        .stApp {
            background: #7cb078 !important;
        }
    </style>
    """, unsafe_allow_html=True) 

def style_background_dashboard():
    st.markdown(""" 
    <style>
        .stApp {
            background: #d0e6ff !important;
            color: black !important;
        }
                
        label {
            color: #3d348b !important;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True) 

def style_base_layout():
    st.markdown(""" 
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Love+Ya+Like+A+Sister&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&family=Poppins:wght@300;400;500;600&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Love+Ya+Like+A+Sister&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Outfit:wght@100..900&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&family=Poppins:wght@300;400;500;600&display=swap');
                
       /* Hide Top Bar Of Streamit */
                
            #MainMenu, footer, header{
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }
                
            /* Streamlit ke by defualt cheezon ko overwrite kr rhe hain */
            h1 {
                font-family: "Love Ya Like A Sister", cursive !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }
                
            h2 {
                font-family: "Love Ya Like A Sister", cursive !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }
            
            h3, h4, p{
                font-family: "Outfit", sans-serif
            }
                
            /* Input box background */
            .stTextInput > div > div > input {
                background-color: white;
                color: black;
                border: 2px solid #6C63FF;
                border-radius: 10px;
            }
                
            /* Placeholder color */
            .stTextInput input::placeholder {
                color: gray;
            }
                
            button[kind="primary"] {
                border-radius: 1.5rem !important;
                background: #3d348b !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
                
            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background: #4a4b4b !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
                
            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background: #4cb1ff !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
                
            button:hover{
                transform:scale(1.05);
            }
                
    </style>
    """, unsafe_allow_html=True) 