import streamlit as st
import time

from services.preparator_service import createTextualPreparator

@st.dialog("⚙️ Configure your textual Preparator", width="large")
def textualPreparatorConfigDialog():
    st.write("**Parameters**")
    st.text_input(label="to_lower", key="TP_config-to_lower", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]", help="Order in which to apply lowercase transformation.")
    st.text_input(label="to_upper", key="TP_config-to_upper", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]", help="Order in which to apply uppercase transformation.")
    st.text_input(label="drop_stopwords", key="TP_config-drop_stopwords", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]", help="Order in which to remove stopwords.")
    st.text_input(label="drop_big_spaces", key="TP_config-drop_big_spaces", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]", help="Order in which to remove multiple spaces.")
    st.text_input(label="drop_digits", key="TP_config-drop_digits", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]", help="Order in which to remove digits.")
    st.text_input(label="lemmatize", key="TP_config-lemmatize", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]", help="Order in which to apply lemmatization using spaCy.")
    st.text_input(label="drop_special_characters", key="TP_config-drop_special_characters", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]", help="Order to remove special characters (punctuation etc.).")
    st.text_input(label="drop_accents", key="TP_config-drop_accents", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]", help="Order in which to remove accents from characters.")
    st.text_input(label="drop_words_less_than_N_letters", key="TP_config-drop_words_less_than_N_letters", value=None, label_visibility="visible", placeholder="Order, Minimum number of letters, Filter only alphabetic words : Optional[Tuple[int, int, bool]]", help="Either the order (int), or a tuple (order, n_letters, isalpha_flag) indicating the order, minimum number of letters, and whether to filter only alphabetic words.")

    if st.button(label="Create Preparator", key="create-preparator", use_container_width=True, type="primary"):
        createTextualPreparator(st.session_state)
        st.rerun()

@st.dialog("⚙️ How to prepare your data ?", width="large")
def prepareConfigDialog():
    st.write("**Parameters**")
    st.checkbox(label="all", key="TP-all", value=False, help="If True and data is a DataFrame, apply transformations to all columns (converted to str). If False, apply only to object/string columns.")
    st.selectbox(label="encoder_name_to_fit", index=None, key="TP-encoder_name", options=["tfidf"], placeholder="Choose an option", label_visibility="visible", help="If specified, encode the processed data using this method ('tfidf', 'word2vec').")
    st.text_input(label="custom_encoder_to_fit", key="TP-custom_encoder_to_fit", value=None, label_visibility="visible", disabled=True, placeholder="You could use a custom encoder to fit with this preparator", help="A user-provided encoder with a `fit_transform()` method.")
    st.text_input(label="custom_encoder_fit", key="TP-custom_encoder_fit", value=None, label_visibility="visible", disabled=True, placeholder="You could use a custom trained encoder with this preparator", help="A user-provided fitted encoder with a `transform()` method.")
    
    if st.button(label="Valid config", key="create-preparator-prepare", use_container_width=True, type="primary"):
        st.session_state['textual_preparator_prepare'] = {"all" : st.session_state.get("TP-all", False), "encoder_name_to_fit": st.session_state.get("TP-encoder_name", None)}
        st.rerun()