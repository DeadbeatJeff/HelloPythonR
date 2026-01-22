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
r_script = get_resource_path("analysis.R")

def run_stats():
    user_input = entry.get()
    
    try:
        # Call Rscript.exe and pass the user input as an argument
        # Shell=True is often needed on Windows to find Rscript in PATH
        result = subprocess.run(
    [r_engine, r_script, user_input], # Interpreter first, then script, then input
    capture_output=True, 
    text=True, 
    check=True
)
        
        # Display the output from R (captured from stdout)
        output_label.configure(text=f"R Probability Result: {result.stdout.strip()}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Could not run R script: {str(e)}")

# --- UI Setup ---
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x240")
app.title("GE HealthCare - CT Bay Analytics")

label = ctk.CTkLabel(app, text="Enter Z-Score for Analysis:")
label.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="e.g. 1.96")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Calculate in R", command=run_stats)
button.pack(pady=10)

output_label = ctk.CTkLabel(app, text="Result will appear here")
output_label.pack(pady=10)

app.mainloop()