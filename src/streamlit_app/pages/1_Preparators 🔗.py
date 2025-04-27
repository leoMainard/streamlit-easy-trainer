import streamlit as st

from services.preparator_service import createTextualPreparator

st.markdown("# Preparators 🔗")

tab1, tab2, tab3 = st.tabs(["Text", "Numeric", "Image"])
col1, col2, col3 = st.columns(3)

with tab1:
    st.write("**Configure your textual Preparator**")
    st.text_input(label="to_lower", key="TP-to_lower", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="to_upper", key="TP-to_upper", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_stopwords", key="TP-drop_stopwords", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_digits", key="TP-drop_digits", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="lemmatize", key="TP-lemmatize", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_special_characters", key="TP-drop_special_characters", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_accents", key="TP-drop_accents", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
    st.text_input(label="drop_words_less_than_N_letters", key="TP-drop_words_less_than_N_letters", value=None, label_visibility="visible", placeholder="Order, Minimum number of letters, Filter only alphabetic words : Optional[Union[int, Tuple[int, int, bool]]]")

    if st.button(label="Create Preparator", key="create-preparator", use_container_width=True, type="primary", on_click=createTextualPreparator, args=(st.session_state,)):
        if "created_preparator" in st.session_state:
            st.write("Résultat de createTextualPreparator :")
            st.json(st.session_state["created_preparator"])
    st.divider()

    st.write("**Add some text**")
    st.text_input(label="text", key="text-input", label_visibility="collapsed", placeholder="Add text here...")

    st.divider()

    st.write("**Resuls**")
with tab2:
    st.info("Coming soon!")
with tab3:
    st.info("Coming soon!")