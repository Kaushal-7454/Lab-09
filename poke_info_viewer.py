""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Pokemon Information")

# Create the frames
frame_input = ttk.Frame(root)
frame_input.grid(row=1, column=0, columnspan=2, pady=(20,10))

frame_info = ttk.LabelFrame(root, text = "Info")
frame_info.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

frame_stats = ttk.LabelFrame(root, text = "stats")
frame_stats.grid(row=1, column=1, padx=(10,20), pady=(10,10), sticky=N)



# Define button click event handler function
def handle_button_get_info():
    poke_name = enter_name.get().strip()
    if poke_name == '':
        return
    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        label_height_value = [text] = str(poke_info['height']) + 'dm'
        label_weight_value = [text] = str(poke_info['weight']) + 'hg'
        type_list = [t['Type']['name'].capatalize() for t in poke_info[type]]
        label_types_value.config(text=', '.join(type_list))

# Populate the user input frame with widgets

label_name = ttk.Entry(root, text = "Pokemon Name")
label_name.grid(row=0, column=0, padx=(10,5), pady=(10))


get_info = ttk.Button(frame_input, text="Get Info", command=handle_button_get_info)
get_info.grid(row=0, column=2, padx=(5, 10))

label_height = ttk.Label(frame_info, text="Height:")
label_height.grid(row=0, column=0, padx=5, pady=5)

label_height_value = ttk.Label(frame_info, text="", font=("Helvetica", 12, "bold"))
label_height_value.grid(row=0, column=1, padx=5, pady=5)

label_weight = ttk.Label(frame_info, text="Weight:")
label_weight.grid(row=1, column=0, padx=5, pady=5)

label_wegt_value = ttk.Label(frame_info, text="", font=("Helvetica", 12, "bold"))
label_wegt_value.grid(row=1, column=1, padx=5, pady=5)

label_types = ttk.Label(frame_info, text="Types:")
label_types.grid(row=2, column=0, padx=5, pady=5)

label_types_value = ttk.Label(frame_info, text="", font=("Helvetica", 12, "bold"))
label_types_value.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()