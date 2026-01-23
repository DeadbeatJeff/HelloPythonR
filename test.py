import subprocess
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk # pip install customtkinter
import os
import sys

def get_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Use this to find your R engine
r_engine = get_resource_path(os.path.join("R-Portable", "App", "R-Portable", "bin", "Rscript.exe"))
r_script = get_resource_path("compute_tolerances.R")

print(r_engine)
print(r_script)

def run_stats():
    # user_input = "Junk"
    
    # Call Rscript.exe and pass the user input as an argument
        # Shell=True is often needed on Windows to find Rscript in PATH
    result = subprocess.run(
        [f'"{r_engine}"', f'"{r_script}"'], # Interpreter first, then script, then input
        capture_output=True, 
        text=True, 
        check=True,
        shell=True # Necessary to process the internal quotes
        )        
    print(result.stdout.strip())
        

run_stats()