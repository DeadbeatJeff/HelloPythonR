file_path <- "C:/Users/jeff/OneDrive - AirAd194/OneDrive/Documents/GitHub/ZB - Data/python/HelloPythonR/Tolerances.xlsx"
col_name <- "Tolerances"
data <- readxl::read_excel(file_path)
values <- data[[col_name]]
rss_result <- sqrt(sum(values^2, na.rm = TRUE))
print(rss_result)
cat(round(rss_result, 4))