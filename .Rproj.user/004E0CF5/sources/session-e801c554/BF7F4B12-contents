# analysis.R
# Fetch arguments passed from Python
args <- commandArgs(trailingOnly = TRUE)

if (length(args) == 0) {
  cat("Error: No data provided")
  quit(status = 1)
}

# Perform your PhD-level math here
input_val <- as.numeric(args[1])
result <- pnorm(input_val, mean = 0, sd = 1) # Standard Normal CDF

# 'cat' sends the result back to Python's stdout pipe
cat(result)