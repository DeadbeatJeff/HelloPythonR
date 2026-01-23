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
    
    if raw_path:
        # 2. Process it (e.g., using get_resource_path)
        file_path = get_resource_path(raw_path)
        
        # 3. Physically put it in the Entry widget
        entry.delete(0, "end")      # Clear previous text
        entry.insert(0, file_path)  # Now entry.get() will return THIS string

    # 3. Use pandas to read only the header row
    try:
        df = pd.read_excel(file_path, nrows=0)
        headers = df.columns.tolist()
        
        # Update the dropdown with the actual Excel headers
        column_dropdown.configure(values=headers)
        column_dropdown.set(headers[0]) # Default to the first column
    except Exception as e:
        messagebox.showerror("File Error", f"Could not read headers: {e}")

    # 4. GET THE COLUMN NAME FROM THE DROPDOWN
    column_name = column_dropdown.get()
    
    # 5. Validation: Don't run if no column is selected
    if column_name == "None Detected":
        messagebox.showwarning("Selection Required", "Please select a data column first.")

def run_r_analysis():
    # 1. Grab the latest values from the entry box and dropdown
    file_path = entry.get()
    column_name = column_dropdown.get()

    # 2. Validation: Ensure we don't send "None Detected" to R
    if (not file_path) or (column_name == "None Detected"):
        messagebox.showwarning("Input Error", "Please select a file and a data column.")
        return

    # 3. Pass BOTH into the background thread as args
    thread = threading.Thread(
        target=execute_r_task, 
        args=(file_path, column_name)
    )
    thread.start()

# def execute_r_task(file_path, column_name):
def execute_r_task(file_path, column_name):
    try:
        # Run the R script
        result = subprocess.run(
    [r_engine, r_script,file_path, column_name],
    capture_output=True, 
    text=True, 
    check=True,
    shell=True # Required to handle the quotes on Windows
)
        
        # Display the output from R
        app.after(0, lambda: output_label.configure(text=f"RSS Tolerance: {result.stdout.strip()}"))

    except subprocess.CalledProcessError as e:
        error_info = e.stderr if e.stderr else e.stdout
        app.after(0, lambda: messagebox.showerror("R Error", f"Logic Error in R:\n{error_info}"))

# --- UI Setup ---
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("1000x360")
app.title("GE HealthCare - CT Bay Analytics")

# UI Layout
label = ctk.CTkLabel(app, text="CT Gantry Alignment - Tolerance Analysis", font=("Arial", 16, "bold"))
label.pack(pady=(20, 5))

sub_label = ctk.CTkLabel(app, text="Select Tolerance Excel File:")
sub_label.pack(pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Select a file...", width=800)
entry.pack(pady=5)

# Button to trigger the file dialog
browse_btn = ctk.CTkButton(app, text="Browse Files", command=select_and_process_excel)
browse_btn.pack(pady=5)

# Add this in your UI Setup section
column_label = ctk.CTkLabel(app, text="Select Data Column:")
column_label.pack(pady=(10, 0))

# Initialize with a dummy value
column_dropdown = ctk.CTkOptionMenu(app, values=["None Detected"], width=200)
column_dropdown.pack(pady=5)

# Primary action button
calculate_button = ctk.CTkButton(app, text="Calculate RSS Tolerance", command=run_r_analysis)
calculate_button.pack(pady=20)

output_label = ctk.CTkLabel(app, text="RSS Statistical Tolerance will be shown here.")
output_label.pack(pady=10)

app.mainloop()