import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog

def main():
    st.set_page_config(
        page_title = "SmartClass - Making Attendance Faster Using AI",
        page_icon = "https://static.vecteezy.com/system/resources/previews/014/604/541/non_2x/smart-education-logo-design-vector.jpg"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None     # Just Initialization

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)

main()
