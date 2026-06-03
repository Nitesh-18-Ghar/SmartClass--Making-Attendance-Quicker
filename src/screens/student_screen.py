import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier 
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_cards import subject_cards
from PIL import Image
import numpy as np
import time

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()

    with c2:
        st.subheader(f"Welcome, {student_data['name']}!", text_alignment='center')
        if st.button("Log out", type='secondary', key='loginbackbtn', shortcut="control + backspace", icon=':material/wifi_home:'):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1,c2 = st.columns(2)
    with c1:
        st.header("Your Enrolled Subjects")
    with c2:
        if st.button("Enroll In Subject", type='primary', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner("Loading Your Enrolled Subjects.."):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        s_id = log['subject_id']
        if s_id not in stats_map:
            stats_map[s_id] = {"total": 0, "attended": 0}

        stats_map[s_id]['total'] += 1

        if log.get('is_present'):
            stats_map[s_id]['attended'] += 1

    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        s_id = sub['subject_id']

        stats = stats_map.get(s_id, {"total": 0, "attended": 0} )
        def unenroll_button():
            if st.button("Unenroll From This Course", key = f"unenroll_{s_id}", type='tertiary', width='stretch', icon=":material/delete_forever:"):
                unenroll_student_to_subject(student_id, s_id)
                st.toast(f'Unenrolled Successfully From {sub['name']}')
                st.rerun()

        with cols[i % 2]:
            subject_cards(
                name = sub['name'],
                code = sub['subject_code'],
                section = sub['section'],
                stats = [
                    ("🗓️", 'Total', stats['total']),
                    ("✅", "Attended", stats['attended'])
                ],
                footer_callback= unenroll_button
            )

    footer_dashboard()

def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
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

    show_registration = False
    photo_source = st.camera_input("Position Your Face In The Center..")

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
