import textwrap
import pandas as pd
import streamlit as st

from easytrainer.data.text import TextualPreparator
from services.utils import parse_input, popup


def createTextualPreparator(session_state):
   params = {}
   for key, input_value in session_state.items():
         if key.startswith("TP_config-"):
            _, method_name = key.split("-")
            value, is_error = parse_input(input_value)
            if is_error:
               st.session_state["textual_preparator"] = TextualPreparator()
               popup(f"Invalid input for {method_name}. Please enter a valid value (int or tuple).", icon="🚨")
               break

            if isinstance(value, int) or isinstance(value, tuple):
               params[method_name] = value

   st.session_state["textual_preparator"] = TextualPreparator(**params)
   popup(f"Preparator ready !", icon="✅")


def getTextualPreparation(session_state):
    if "textual_preparator" not in session_state:
        popup("Configure your Preparator first", icon="🫦")
        return

    preparator = session_state["textual_preparator"]
    last_df = session_state["TP-df"]
    edited_df = session_state.get("textual_df", None)

    # Suppression des lignes supprimées
    row_to_delete = edited_df.get("deleted_rows", [])
    if row_to_delete:
        last_df = last_df.drop(row_to_delete, errors="ignore")

    # Mise à jour des lignes éditées
    for index, row in edited_df.get("edited_rows", {}).items():
        for col_name, value in row.items():
            last_df.loc[index, col_name] = value
    
    # Ajout des nouvelles lignes
    for row in edited_df.get("added_rows", []):
        for col_name, value in row.items():
            last_df.loc[-1, col_name] = value

    try:
        result = preparator.prepare(last_df, all=session_state.get("TP-all", False), encoder_name_to_fit=session_state.get("TP-encoder_name", None), custom_encoder_to_fit=None, custom_encoder_fit=None)
        last_df = result["data"]
    except Exception as e:
        popup(f"Error during preparation : {e}", icon="🚨")

    # Mise à jour du session_state final
    session_state["TP-df"] = last_df.reset_index(drop=True)

def loadTextualPreparatorCode(session_state):
    order = getattr(session_state.get("textual_preparator", {}), "order", {})
    n_letters = getattr(session_state.get("textual_preparator", None), "n_letters", None)
    n_letters_isalpha = getattr(session_state.get("textual_preparator", None), "n_letters_isalpha", None)
    
    prepare_all = session_state.get("textual_preparator_prepare", {}).get("all", None)
    prepare_encoder_name = session_state.get("textual_preparator_prepare", {}).get("encoder_name_to_fit", None)

    if isinstance(prepare_encoder_name, str):
        prepare_encoder_name = f'"{prepare_encoder_name}"'

    return textwrap.dedent(f"""
        from easytrainer.data.text import TextualPreparator

        preparator = TextualPreparator(
            to_lower={order.get("txt_to_lower", None)},
            to_upper={order.get("txt_to_upper", None)},
            drop_stopwords={order.get("drop_stopwords", None)},
            drop_big_spaces={order.get("drop_big_spaces", None)},
            drop_digits={order.get("drop_digits", None)},
            lemmatize={order.get("lemmatize", None)},
            drop_special_characters={order.get("drop_special_characters", None)},
            drop_accents={order.get("drop_accents", None)},
            drop_words_less_than_N_letters=({order.get("drop_words_less_than_N_letters", None)},{n_letters},{n_letters_isalpha})
        )

        results = preparator.prepare(
            data=your_data,
            all={prepare_all},
            encoder_name_to_fit={prepare_encoder_name},
            custom_encoder_to_fit=None,
            custom_encoder_fit=None
        )
    """)

def readExcelorCSVFile(sesssion_state):
    df = pd.DataFrame(columns=["add_your_text", "prepared_text", "encoded_text"])
    uploaded_file = sesssion_state.get("container_data_file", None)

    if uploaded_file is None:
        st.error("Please upload a file.")
    else:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format.")
        
        df["prepared_text"] = ""
        df["encoded_text"] = ""
    
    st.session_state["TP-df"] = df