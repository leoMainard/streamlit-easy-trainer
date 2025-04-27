import ast
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
   if "textual_preparator" in session_state:
      preparator = session_state["textual_preparator"]
      text = session_state.get("text-input", None)
      result = preparator.prepare([text])
      st.session_state["text-output"] = result["data"]
      # if text:
      #    try:
      #       result = preparator(text)
      #       st.session_state["text-output"] = result["data"]
      #    except Exception as e:
      #       popup(f"Error during preparation: {e}", icon="🚨")
      # else:
      #    popup(f"Please add some text to prepare", icon="🫦")
   else:
      popup(f"Configure your Preparator first", icon="🫦")