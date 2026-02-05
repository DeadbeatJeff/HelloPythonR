# HelloPythonR
This Hello, World-type program demonstrates the possibility of running an R application with Python instead of R Shiny. It is just proof-of-concept currently. It reads in an MS Excel file, selects a column of tolerances data, and computes the root-sum-square (RSS) tolerance.

Quick Start: Download & Run
If you are an engineer looking to use this tool, you do not need to install Python or R. The application is distributed as a self-contained Windows executable.

    * Go to the Releases Page: On the right-hand side of this GitHub repository, click on Releases.
    * Download the Binary: Under the "Assets" section of the latest release, click on RSSCalculator.exe to download it.
    * Run the App: Double-click main.exe.
        * Note: If Windows Defender shows a "SmartScreen" warning, click More Info and then Run Anyway.
    * A sample data file is here: https://deadbeatjeff.sdf.org/data/Tolerances.xlsx
    * Load a data file, select a column of tolerances, and click Calculate RSS Tolerance.
       * This first time one tries to run it, it might crash as it tries to installs an R library to allow it to read MS Excel files.
       * The second time one tries to run it, it might take a while to do the first calculation after one clicks Calculate RSS Tolerance as it installs the R library.
       * The program should function properly after that.
