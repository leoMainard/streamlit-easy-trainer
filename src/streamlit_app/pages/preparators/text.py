import pandas as pd
import streamlit as st

from services.dialogs import textualPreparatorConfigDialog, prepareConfigDialog
from services.preparator_service import (
    getTextualPreparation,
    loadTextualPreparatorCode, 
    readExcelorCSVFile
)

# ------ session state ------
if "TP-df" not in st.session_state:
    st.session_state["TP-df"] = pd.DataFrame(columns=["add_your_text"])

# ------ config ------
container_config = st.container()
container_config.subheader("Configure your Preparator")
container_config.code(loadTextualPreparatorCode(st.session_state), language="python")
tab1_c_col1, tab1_c_col2 = container_config.columns(2)

if tab1_c_col1.button("⚙️ TextualPreparator()", use_container_width=True, type="primary"):
    textualPreparatorConfigDialog()

if tab1_c_col2.button("⚙️ TextualPreparator.prepare()", use_container_width=True, type="primary"):
    prepareConfigDialog()        

container_config.divider()

# ------ data ------
container_data = st.container()
container_data.subheader("Add your data")

container_data.file_uploader("**Upload your data**", key="container_data_file", type=["csv", "xlsx"], on_change=readExcelorCSVFile, args=(st.session_state,))
container_data.write("**Or add some text directly in the table**")

container_data.data_editor(
    data=st.session_state["TP-df"],
    key="textual_df",
    num_rows="dynamic"
)

st.button(label="👀", key="TP-prepare", use_container_width=True, type="primary", on_click=getTextualPreparation, args=(st.session_state,))