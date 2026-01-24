# compute_tolerances.R

# Define required packages
required_packages <- c("readxl")

# Set a reliable CRAN mirror to avoid a popup selection window
options(repos = c(CRAN = "https://cloud.r-project.org"))

# Self-healing library check
for (pkg in required_packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    # type="binary" ensures it doesn't try to compile from source
    # dependencies=TRUE ensures all sub-libraries like 'cellranger' are included
    install.packages(pkg, type = "binary", dependencies = TRUE)
  }
}

library(readxl)

args <- commandArgs(trailingOnly = TRUE)
file_path <- args[1]
col_name <- args[2]

# Read the data
data <- read_excel(file_path)

# Extract the specific column into a vector
values <- data[[col_name]]

# Perform Actuarial/Statistical Analysis (e.g., RSS of the column)
result <- sqrt(sum(values^2, na.rm = TRUE))

cat(paste(round(result, 3)))