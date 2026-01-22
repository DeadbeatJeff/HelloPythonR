import subprocess
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from tkinter import filedialog
import pandas as pd
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

def select_and_process_excel():
    # 1. Open File Dialog
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if not file_path:
        return

    # 2. Read Excel headers to let user choose a column
    df = pd.read_excel(file_path, nrows=0) 
    columns = df.columns.tolist()
    
    # 3. Create a simple popup to pick the column (simplified for now)
    # For this demo, let's assume we take the first column or a specific name
    target_column = columns[0] 
    
    # 4. Pass the file path and column name to R
    run_r_analysis(file_path, target_column)
    
def run_r_analysis(file_path, column_name):
    # Pass the path and column name as arguments to Rscript
    # Note: Use shlex.quote or similar if paths have spaces
    result = subprocess.run(
        [r_engine, r_script, file_path, column_name],
        capture_output=True, text=True, check=True
    )
    output_label.configure(text=result.stdout)
        
    # Display the output from R (captured from stdout)
    output_label.configure(text=f"RSS Statistical Tolerance: {result.stdout.strip()}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Could not run R script: {str(e)}")

# --- UI Setup ---
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x240")
app.title("GE HealthCare - CT Bay Analytics")

label = ctk.CTkLabel(app, text="Upload the tolerances (in an MS Excel file with a header):")
label.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Tolerances.xlsx")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Calculate in R", command=run_stats)
button.pack(pady=10)

output_label = ctk.CTkLabel(app, text="RSS Statistical Tolerance will be shown here.")
output_label.pack(pady=10)

app.mainloop()