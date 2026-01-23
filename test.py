import os
import subprocess

# Use a raw string for the base path to avoid escape character issues
r_engine = r"C://Users//jeff//OneDrive - AirAd194//OneDrive//Documents//GitHub//ZB - Data//python//HelloPythonR//R-Portable//App//R-Portable//bin//Rscript.exe"
r_script = r"C://Users//jeff//OneDrive - AirAd194//OneDrive//Documents//GitHub//ZB - Data//python//HelloPythonR//compute_tolerances.R"

def execute_r_task():
    # Normalize the paths for Windows
    # engine_safe = os.path.normpath(r_engine)
    # script_safe = os.path.normpath(r_script)

    print(r_engine)
    print(r_script)

    try:
        # Wrap the paths in literal double quotes inside the list
        result = subprocess.run(
            [f'"{r_engine}"', f'"{r_script}"'],
            capture_output=True,
            text=True,
            check=True,
            shell=True # This allows the shell to interpret the quotes
        )
        print("R Output:", result.stdout.strip())

    except subprocess.CalledProcessError as e:
        # This catches errors that happen INSIDE the R script
        print("R Script Error Output:", e.stderr)
    except Exception as e:
        # This catches errors where Python can't even launch R
        print("System Launch Error:", str(e))

execute_r_task()