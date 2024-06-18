import streamlit as st

def sidebar_spacer():
    st.sidebar.markdown(
        """
        <style>
        .spacer {
            margin-top: 75%;  /* Adjust the margin as needed */
        }
        </style>
        <div class="spacer"></div>
        """,
        unsafe_allow_html=True
    )
