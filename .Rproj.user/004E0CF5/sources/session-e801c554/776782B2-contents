# compute_tolerances.R
# 1. Re-enable arguments so R listens to Python
# args <- commandArgs(trailingOnly = TRUE)
file_path <- "C:\\Users\\jeff\\OneDrive - AirAd194\\OneDrive\\Documents\\GitHub\\ZB - Data\\python\\HelloPythonR\\Tolerances.xlsx"
col_name <- "Tolerances"

# 2. Add a check to see if the file actually exists in this context
if(!file.exists(file_path)) {
  stop(paste("File not found at:", file_path))
}

library(readxl)
data <- readxl::read_excel(file_path)
values <- data[[col_name]]
rss_result <- sqrt(sum(values^2, na.rm = TRUE))

cat(round(rss_result, 4))