import streamlit as st

st.set_page_config(page_title="Easy Trainer") #, layout="wide")

pages = {
    " ": [
        st.Page("pages/home.py", icon=":material/home:"),
    ],
    "Preparators": [
        st.Page("pages/preparators/text.py", title="Text", icon=":material/settings:"),
    ],
    "Models": [
        st.Page("pages/models/models.py", title="Classifiers", icon=":material/toggle_on:"),
    ],
}

pg = st.navigation(pages)
pg.run()