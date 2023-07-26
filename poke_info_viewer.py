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

# TODO: Create the frames
frame_input = ttk.Frame(root)
frame_input.grid(row=1, column=0, columnspan=2, pady=(20,10))

frame_info = ttk.LabelFrame(root, text = "Info")
frame_info.grid(row=1, column=0, padx=(20,10), pady=(10,20), sticky=N)

frame_stats = ttk.LabelFrame(root, text = "stats")
frame_stats.grid(row=1, column=1, padx=(10,20), pady=(10,10), sticky=N)

label_name = ttk.Entry(root, text = "Pokemon Name")
label_name.grid(row=0, column=0, padx=(10,5), pady=(10))

enter_name=ttk.Entry(frame_input)
enter_name.insert(0,'Pikachu')
enter_name.grid(row=0, column=1)

def handle_button_get_info():
    poke_name = enter_name.get().strip()
    if poke_name == '':
        return
    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        labe_height_value = [text] = str(poke_info['height']) + 'dm'
        labe_weight_value = [text] = str(poke_info['weight']) + 'hg'
        type_list = [t['Type']['name'].capatalize() for t in poke_info[type]]


# TODO: Populate the user input frame with widgets


# TODO: Define button click event handler function

root.mainloop()