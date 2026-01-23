import subprocess
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from tkinter import filedialog
import threading
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
    raw_path = filedialog.askopenfilename(
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )
    if not raw_path:
        return
    
    # 1. Normalize the slashes to Windows standard
    # normalized_path = os.path.normpath(raw_path) # Automatically fixes slash direction
    normalized_path = f"C:/Users/jeff/OneDrive - AirAd194/OneDrive/Documents/GitHub/ZB - Data/python/HelloPythonR/Tolerances.xlsx"

    # 2. Add literal double quotes for shell safety
    # file_path = f'"{normalized_path}"'
    # file_path = normalized_path
    file_path = os.path.normpath(f"C:/Users/jeff/OneDrive - AirAd194/OneDrive/Documents/GitHub/ZB - Data/python/HelloPythonR/Tolerances.xlsx")

    # 2. Read Excel headers to let user choose a column
    # df = pd.read_excel(file_path, nrows=0) 
    df = pd.read_excel(file_path, nrows=0) 
    columns = df.columns.tolist()
    
    # 3. Create a simple popup to pick the column (simplified for now)
    # For this demo, let's assume we take the first column or a specific name
    column_name = columns[0] 
    
    # 4. Pass the file path and column name to R
    # run_r_analysis(file_path, column_name)
    run_r_analysis()

# def run_r_analysis(file_path, column_name):
def run_r_analysis():
    # # 1. Grab the latest values from the UI
    # current_file = browse_btn.get()
    # current_col = column_dropdown.get()

    # if not current_file or current_col == "None Detected":
    #     messagebox.showwarning("Input Error", "Please select a file and a data column.")
    #     return

    # 2. Pass them BOTH into the background thread
    thread = threading.Thread(
        # target=execute_r_task, 
        # args=(file_path, column_name)
        target=execute_r_task
    )
    thread.start()

# def execute_r_task(file_path, column_name):
def execute_r_task():
    try:
        # Normalize slashes for Windows
        # clean_path = os.path.normpath(file_path)
        
        # Build the command list with explicit quotes for spaces
        # result = [R_Executable, R_Script, Argument1, Argument2]
        result = subprocess.run(
            [
                f'"{r_engine}"', 
                f'"{r_script}"'
                # f'"{file_path}"', 
                # f'"{column_name}"'
            ],
            capture_output=True, 
            text=True, 
            check=True,
            shell=True # Required to handle the quotes on Windows
        )
        
        # Display the output from R
        app.after(0, lambda: output_label.configure(text=f"RSS Result: {result.stdout.strip()}"))

    except subprocess.CalledProcessError as e:
        error_info = e.stderr if e.stderr else e.stdout
        app.after(0, lambda: messagebox.showerror("R Error", f"Logic Error in R:\n{error_info}"))

# --- UI Setup ---
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("400x320")
app.title("GE HealthCare - CT Bay Analytics")

# UI Layout
label = ctk.CTkLabel(app, text="CT Gantry Alignment - Tolerance Analysis", font=("Arial", 16, "bold"))
label.pack(pady=(20, 5))

sub_label = ctk.CTkLabel(app, text="Select Tolerance Excel File:")
sub_label.pack(pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Select a file...", width=400)
entry.pack(pady=5)

# Button to trigger the file dialog
# browse_btn = ctk.CTkButton(app, text="Browse Files", command=select_file, fg_color="gray")
browse_btn = ctk.CTkButton(app, text="Browse Files", command=select_and_process_excel)
browse_btn.pack(pady=5)

# # Add this in your UI Setup section
# column_label = ctk.CTkLabel(app, text="Select Data Column:")
# column_label.pack(pady=(10, 0))

# # Initialize with a dummy value
# column_dropdown = ctk.CTkOptionMenu(app, values=["None Detected"], width=200)
# column_dropdown.pack(pady=5)

# Primary action button
# calculate_button = ctk.CTkButton(app, text="Calculate RSS Tolerance", command=run_r_analysis)
# calculate_button.pack(pady=20)

output_label = ctk.CTkLabel(app, text="RSS Statistical Tolerance will be shown here.")
output_label.pack(pady=10)

app.mainloop()