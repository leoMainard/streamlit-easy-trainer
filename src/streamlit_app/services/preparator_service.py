import pandas as pd
import streamlit as st

from easytrainer.data.text import TextualPreparator
from services.utils import parse_input, popup


def createTextualPreparator(session_state):
   params = {}
   for key, input_value in session_state.items():
         if key.startswith("TP-"):
            _, method_name = key.split("-")
            value, is_error = parse_input(input_value)
            if is_error:
               popup(f"Invalid input for {key}. Please enter a valid value (int or tuple).", icon="🚨")
               st.session_state["textual_preparator"] = TextualPreparator()
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
    last_df = session_state["TP_df"]
    print("last_df", last_df)
    edited_df = session_state.get("textual_df", None)

    # Suppression des lignes supprimées
    row_to_delete = edited_df.get("deleted_rows", [])
    if row_to_delete:
        last_df = last_df.drop(row_to_delete, errors="ignore")

    # Mise à jour des lignes éditées
    edited_text = [(index, row.get("add_your_text", "")) for index, row in edited_df.get("edited_rows", {}).items()]
    for index, new_text in edited_text:
        try:
            new_prepared = preparator.prepare([new_text])["data"][0]
        except Exception as e:
            popup(f"Error during preparation (edited row {index}): {e}", icon="🚨")
            new_prepared = None
        last_df.loc[index, "add_your_text"] = new_text
        last_df.loc[index, "prepared_text"] = new_prepared
        last_df.loc[index, "encoded_text"] = None

    # Ajout des nouvelles lignes
    text_to_prepare = [row.get("add_your_text", "") for row in edited_df["added_rows"]]
    try:
        result = preparator.prepare(text_to_prepare)
        new_df = pd.DataFrame({
            "add_your_text": text_to_prepare,
            "prepared_text": result["data"],
            "encoded_text": [None] * len(text_to_prepare)
        })
        last_df = pd.concat([last_df, new_df], ignore_index=True)
        print("last_df", last_df)
    except Exception as e:
        popup(f"Error during preparation (new rows): {e}", icon="🚨")

    # Mise à jour du session_state final
    session_state["TP_df"] = last_df.reset_index(drop=True)

