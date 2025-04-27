from easytrainer.data.text import TextualPreparator
import ast

def createTextualPreparator(session_state):
   params = {}
   for key, input_value in session_state.items():
         if key.startswith("TP-"):
            _, method_name = key.split("-")
            try:
               value = ast.literal_eval(input_value)
            except:
               value = input_value
            
            if isinstance(value, int):
               value = int(value)
            if (isinstance(value, tuple) and len(value) == 3):
               value = (int(value[0]), int(value[1]), bool(value[2]))
               
            params[method_name] = [value]
   session_state["created_preparator"] = params


