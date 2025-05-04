import time
import streamlit as st
from typing import Optional, Union, Tuple

def parse_input(user_input: str) -> Optional[Union[int, Tuple[Union[int, bool], ...]]]:
    """
    Retourne un int ou un tuple d'entiers et de booléens à partir d'une chaîne d'entrée utilisateur.
    Retourne également Erreur : True ou False si l'entrée est invalide.
    """
    if not user_input:
        return None, False
    user_input = user_input.strip()
    # int
    try:
        return int(user_input), False
    except ValueError:
        pass

    # float
    try:
        return float(user_input), False
    except ValueError:
        pass
    
    # tuple
    if user_input.startswith("(") and user_input.endswith(")"):
        try:
            parts = user_input[1:-1].split(",")
            parsed_parts = []
            for part in parts:
                part = part.strip()
                lower_part = part.lower()
                if lower_part == "true":
                    parsed_parts.append(True)
                elif lower_part == "false":
                    parsed_parts.append(False)
                else:
                    try:
                        parsed_parts.append(int(part))
                    except ValueError:
                        try:
                            parsed_parts.append(float(part))
                        except ValueError:
                            parsed_parts.append(part)
            return tuple(parsed_parts), False
        except Exception:
            pass

    return None, True

def popup(message:str, icon:str="", sleep_time:int=4):
    msg = st.toast(message, icon=icon)
    time.sleep(sleep_time)