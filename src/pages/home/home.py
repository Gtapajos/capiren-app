import streamlit as st
import pandas as pd
import numpy as np
from src.services.labels_service import LabelsService
from src.services.pdf_service import PdfService
from streamlit_modal import Modal
from src.utils.annotate import display_annotated_text
from src.shared.categories_dict import categories
from src.partials.sidebar_image import sidebar_image
from src.partials.sidebar_title import sidebar_title
from src.partials.sidebar_spacer import sidebar_spacer

def format_response_chart(response):
    dict_chart = {}
    categories = []
    labels_count = []
    for entity in response:
        categories.append(entity['entity_group'])
    for entity in categories:
        labels_count.append((entity, categories.count(entity)))

    labels_count = set(labels_count)
    
    dict_chart["categories"] = [entity[0] for entity in list(labels_count)]
    dict_chart["quantities"] = [entity[1] for entity in list(labels_count)]

    return dict_chart
def home():
    st.title("Início")

    sidebar_spacer()
    sidebar_title()

    sidebar_image()

    modal = Modal("Entidades Rotuladas", key="demo-modal")

    # Initialize pdf_text in session state
    if "pdf_text" not in st.session_state:
        st.session_state["pdf_text"] = ""

    # Display the text area with either extracted text or existing text
    text = st.text_area("Digite o texto a ser rotulado", value=st.session_state["pdf_text"], height=320)

    col1, col2 = st.columns(2)

    with col1:
        label_button = st.button("Iniciar Rotulação", type="primary")
    with col2:
        category = st.selectbox(label="Categoria do texto", options=("Geral", "Jurídico", "Geologia"))

    if label_button:
        labels = LabelsService()
        st.session_state["response"] = labels.get_labels(text, categories[f'{category}'])
        modal.open()
    
    if modal.is_open():
        with modal.container():
            visualization = st.radio("Opções de visualização",
                     ["Texto", "Gráfico"])
            if visualization == "Texto":
                display_annotated_text(text, st.session_state["response"])
            elif visualization == "Gráfico":
                chart_elements = format_response_chart(st.session_state["response"])
                data = {
                    'Category': chart_elements['categories'],
                    'Values': chart_elements['quantities'],
                }
                df = pd.DataFrame(data)    
                st.bar_chart(df.set_index('Category'))        

    file = st.file_uploader("Submeter Arquivo", type="pdf")
    
    if file is not None:
        text_pdf = PdfService()
        new_text = text_pdf.get_text(file)
        if new_text['extracted_text'] != st.session_state["pdf_text"]: 
            st.session_state["pdf_text"] = new_text['extracted_text']
            st.rerun()

if __name__ == "__main__":
    home()
