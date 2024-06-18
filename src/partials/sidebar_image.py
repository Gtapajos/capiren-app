import streamlit as st

def sidebar_image():
    st.sidebar.markdown(
        """
        <style>
            .icon {
                border-radius: 150px;
                }
        </style>
        <img class="icon" src="https://media.istockphoto.com/id/1197747580/vector/vector-illustration-of-capybara-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=uPmYUPsx5KZC8L685edB2J_itMI7C9Sbgd2Nxxu6d0o=" width="250px">

        """,
        unsafe_allow_html=True
    )
