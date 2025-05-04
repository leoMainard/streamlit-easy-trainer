import pandas as pd
import streamlit as st

from services.dialogs import textualPreparatorConfigDialog, prepareConfigDialog
from services.preparator_service import getTextualPreparation, createTextualPreparator

# ------ session state ------
if "TP_df" not in st.session_state:
    st.session_state["TP_df"] = pd.DataFrame(columns=["add_your_text", "prepared_text", "encoded_text"])

# ------ config ------
container_config = st.container()
container_config.subheader("Configure your Preparator")
container_config.code("## Textual Preparator", language="python")
tab1_c_col1, tab1_c_col2 = container_config.columns(2)

if tab1_c_col1.button("⚙️ TextualPreparator()", use_container_width=True):
    textualPreparatorConfigDialog()

if tab1_c_col2.button("⚙️ TextualPreparator.prepare()", use_container_width=True):
    prepareConfigDialog()        

container_config.divider()

# ------ data ------
container_data = st.container()
container_data.subheader("Add your data")

container_data.file_uploader("**Upload your data**")
container_data.write("**Or add some text directly in the table**")
# tab1_d_col3.download_button("Download your prepared data", )

container_data.data_editor(
    data=st.session_state["TP_df"],
    key="textual_df",
    num_rows="dynamic",
    disabled=("prepared_text", "encoded_text")
)

tab1_d_col1, tab1_d_col2 = container_data.columns((4,1))
tab1_d_col1.button(label="👀", key="TP-prepare", use_container_width=True, type="primary", on_click=getTextualPreparation, args=(st.session_state,))
tab1_d_col2.button(label="🗑️", key="TP-delete", use_container_width=True, type="secondary", on_click=getTextualPreparation, args=(st.session_state,))
