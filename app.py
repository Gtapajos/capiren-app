import streamlit as st
from st_pages import Page, show_pages
from src.partials.sidebar_image import sidebar_image
from src.partials.sidebar_title import sidebar_title
from src.partials.sidebar_spacer import sidebar_spacer
from src.pages.home.home import home

# Set the page title and layout
st.set_page_config(page_title="My Streamlit App", layout="wide")

def main():

    home()

    # Show the pages after the title and image
    show_pages(
        [
            Page(r"src/pages/home/home.py", "Início", "🏠"),
            Page(r"src/pages/about/about.py", "Sobre", "📖"),
        ]
    )

if __name__ == "__main__":
    main()
