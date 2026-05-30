import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_base_home, style_base_dashboard

def home_screen():

    header_home()      # For Smart Class at the top of every screen

    style_base_layout()
    style_base_home()
    style_base_dashboard()      # For green Background

    col1, col2 = st.columns(2, gap='large')

    with col1:
        st.header("Teacher's Page")
        st.image("https://thumbs.dreamstime.com/b/smart-boy-child-teacher-avatar-school-cartoon-419270228.jpg", width=145)
        if st.button('Teacher Portal', type='secondary', icon=':material/call_made:', icon_position='right'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()   # Refresh the page to reflect the change in login_type

    with col2:
        st.header("Student's Page")
        st.image("https://static.vecteezy.com/system/resources/thumbnails/031/610/037/small/a-of-a-3d-cartoon-little-boy-in-class-world-students-day-images-ai-generative-photo.jpg", width=160)
        if st.button('Student Portal', type='secondary', icon=':material/call_made:', icon_position='right'):
            st.session_state['login_type'] = 'student'
            st.rerun()   # Since abhi humne back button nhi diya hai so refresh krne pe home screen par aa jayega

    footer_home()