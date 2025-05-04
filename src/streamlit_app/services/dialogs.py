import streamlit as st

from services.preparator_service import createTextualPreparator

@st.dialog("⚙️ Configure your textual Preparator", width="large")
def textualPreparatorConfigDialog():
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

@st.dialog("⚙️ How to prepare your data ?", width="large")
def prepareConfigDialog():
    st.write("**Parameters**")
    st.checkbox(label="all", key="TP-all", value=False)
    st.text_input(label="encoder_name_to_fit", key="TP-encoder_name", value=None, label_visibility="visible", placeholder="")
    st.text_input(label="custom_encoder_to_fit", key="TP-custom_encoder_to_fit", value=None, label_visibility="visible", disabled=True, placeholder="You could use a custom encoder to fit with this preparator")
    st.text_input(label="custom_encoder_fit", key="TP-custom_encoder_fit", value=None, label_visibility="visible", disabled=True, placeholder="You could use a custom trained encoder with this preparator")
    
