import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter The Details Of New Subject")
    sub_id = st.text_input("Subject Code", placeholder="CSC23428")
    sub_name = st.text_input("Subject Name", placeholder="Data Science")
    sub_section = st.text_input("Section", placeholder="A")

    if st.button("Create Subject", type='primary', width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject Created Successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")

        else:
            st.warning("All fields Are Required.")