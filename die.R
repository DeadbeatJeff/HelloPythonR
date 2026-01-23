# compute_tolerances.R

values <- c(1, 1.5, 2, 1, 0.5)
rss_result <- sqrt(sum(values^2, na.rm = TRUE))

cat(round(rss_result, 4))