import pandas as pd
import streamlit as st

from services.dialogs import testdialog
from services.preparator_service import getTextualPreparation, createTextualPreparator

st.set_page_config(page_title="Easy Trainer", layout="wide")

tab1, tab2, tab3 = st.tabs(["Text", "Numeric", "Image"])
col1, col2 = st.columns((5,1))
if "TP_df" not in st.session_state:
    st.session_state["TP_df"] = pd.DataFrame(columns=["add_your_text", "prepared_text", "encoded_text"])

with tab1:
    tab1_container_config = st.container()
    tab1_c_col1, tab1_c_col2 = tab1_container_config.columns((2,1))
    tab1_c_col1.code("## Textual Preparator", language="python")

    if tab1_c_col2.button("⚙️ TextualPreparator()", use_container_width=True):
        testdialog()
    
    if tab1_c_col2.button("⚙️ TextualPreparator.prepare()", use_container_width=True):
        testdialog()        

    tab1_container_config.divider()
    tab1_container_data = st.container()

    tab1_container_data.file_uploader("Upload your data")
    tab1_container_data.write("**Or add some text directly in the table**")
    # tab1_d_col3.download_button("Download your prepared data", )

    tab1_container_data.data_editor(
        data=st.session_state["TP_df"],
        key="textual_df",
        num_rows="dynamic",
        disabled=("prepared_text", "encoded_text")
    )

    tab1_d_col1, tab1_d_col2 = tab1_container_data.columns((4,1))
    tab1_d_col1.button(label="👀", key="TP-prepare", use_container_width=True, type="primary", on_click=getTextualPreparation, args=(st.session_state,))
    tab1_d_col2.button(label="🗑️", key="TP-delete", use_container_width=True, type="secondary", on_click=getTextualPreparation, args=(st.session_state,))
with tab2:
    st.info("Coming soon!")
with tab3:
    st.info("Coming soon!")