import streamlit as st

from services.preparator_service import createTextualPreparator, getTextualPreparation

# ----- session state -----


st.markdown("# Preparators 🔗")

tab1, tab2, tab3 = st.tabs(["Text", "Numeric", "Image"])
col1, col2 = st.columns((5,1))

with tab1:
    with st.expander("**Configure your textual Preparator**", expanded=False, icon="⚙️"):
        st.write("**Parameters**")
        st.text_input(label="to_lower", key="TP-to_lower", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
        st.text_input(label="to_upper", key="TP-to_upper", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
        st.text_input(label="drop_stopwords", key="TP-drop_stopwords", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
        st.text_input(label="drop_digits", key="TP-drop_digits", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
        st.text_input(label="lemmatize", key="TP-lemmatize", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
        st.text_input(label="drop_special_characters", key="TP-drop_special_characters", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
        st.text_input(label="drop_accents", key="TP-drop_accents", value=None, label_visibility="visible", placeholder="Order : Optionnal[int]")
        st.text_input(label="drop_words_less_than_N_letters", key="TP-drop_words_less_than_N_letters", value=None, label_visibility="visible", placeholder="Order, Minimum number of letters, Filter only alphabetic words : Optional[Tuple[int, int, bool]]")

        st.button(label="Create Preparator", key="create-preparator", use_container_width=True, type="primary", on_click=createTextualPreparator, args=(st.session_state,))
        if "textual_preparator" in st.session_state:
            st.write(st.session_state["textual_preparator"])

    st.write("**Add some text**")
    st.text_input(label="text-input", key="text-input", label_visibility="collapsed", placeholder="Add text here...", on_change=getTextualPreparation, args=(st.session_state,))

    st.divider()

    st.write("**Results**")
    if "text-output" in st.session_state:
        st.text_input(label="text-output", key="text-output-display", value=st.session_state["text-output"], label_visibility="collapsed", disabled=True)
with tab2:
    st.info("Coming soon!")
with tab3:
    st.info("Coming soon!")