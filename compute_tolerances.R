# compute_tolerances.R

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