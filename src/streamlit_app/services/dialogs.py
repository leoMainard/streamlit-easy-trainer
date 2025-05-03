import streamlit as st

from services.preparator_service import createTextualPreparator

@st.dialog("⚙️ Configure your textual Preparator", width="large")
def testdialog():
    st.write("**Parameters**")
    st.text_input(label="to_lower", key="TP-to_lower", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="to_upper", key="TP-to_upper", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_stopwords", key="TP-drop_stopwords", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_digits", key="TP-drop_digits", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="lemmatize", key="TP-lemmatize", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_special_characters", key="TP-drop_special_characters", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_accents", key="TP-drop_accents", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_words_less_than_N_letters", key="TP-drop_words_less_than_N_letters", value=None, label_visibility="visible", placeholder="Order, Minimum number of letters, Filter only alphabetic words : Optional[Tuple[int, int, bool]]")

    if st.button(label="Create Preparator", key="create-preparator", use_container_width=True, type="primary"):
        createTextualPreparator(st.session_state)
        st.rerun()