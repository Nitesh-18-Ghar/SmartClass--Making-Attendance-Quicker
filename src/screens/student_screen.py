import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier 
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student
from PIL import Image
import numpy as np
import time

def student_dashboard():
    st.header("Your Dashboard")

def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_id" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()

    with c2:
        if st.button("Back To Home", type='primary', key='loginbackbtn', shortcut="control + backspace", icon=':material/wifi_home:'):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login Using FaceID", text_alignment="center")
    st.space()
    st.space()

    photo_source = st.camera_input("Position Your Face In The Center..")

    show_registration = False
    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner("Processing Your Face.."):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning("No face detected!")
            elif num_faces > 1:
                st.warning("Multiple faces detected! Ensure only your face is visible.")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s["student_id"] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = "student"
                        st.session_state.student_data = student
                        st.toast(f"Login Successful! Welcome Back {student['name']}")
                        time.sleep(2)
                        st.rerun()
                else:
                    st.info("Face Not Identified! You Might Be a New Student.")
                    show_registration = True
    if show_registration:
        with st.container(border=True):
            st.header("New Student Registration")
            new_name = st.text_input("Enter Your Name", placeholder='eg. Nitesh Ghar')

            st.subheader("Optional: Voice ID")
            st.info("Enrolling Voice Only Attendance")

            audio_data = None
            try:
                audio_data = st.audio_input("Record Your Short Voice like I am Present, My Name is Nitesh.")
            except Exception:
                st.error("Error In Recording Audio..")

            if st.button("Create Account", type='primary'):
                if new_name:
                    with st.spinner("Creating Account.."):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_embedding = face_emb, voice_embedding = voice_emb)

                            if response_data:
                                train_classifier() 
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = "student"
                                st.session_state.student_data = response_data[0]
                                st.toast(f"Account Created! Welcome {new_name}")
                                time.sleep(2)
                                st.rerun()
                        else:
                            st.error("Couldn't Capture Face For Registration")
                else:
                    st.warning("Please Enter Your Name!")

    footer_dashboard()