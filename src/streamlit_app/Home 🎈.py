import streamlit as st

st.set_page_config(page_title="Easy Trainer", layout="wide")
st.markdown("# Welcome to Easy Trainer 🎈")
st.markdown("Select a page in the sidebar to get started.")


st.markdown(
    """
    <style>
    /* Target dataframes to make them wider */
    .element-container div[data-testid="stDataFrame"] {
        width: 100% !important;
    }

    /* Target expanders to make them wider */
    .element-container div[data-testid="stExpander"] {
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)