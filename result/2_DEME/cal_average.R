# Create an empty data frame to store the average values

# 选择：
# migration rate 为 0.2，0.4，0.6，0.8，1.0
# drive fitness 为 0.5，0.75，1.0

average_data_fit_100 <- vector("list", 5)
for (i in 1:5) {
    average_data_fit_100[[i]] <- data.frame()
}

mig <- c("0.020", "0.040", "0.060", "0.080", "0.100")

# Loop through each data file
for (i in 1:20) {
    # Read the data file
    for (j in 1:5) {
        file_path_100 <- paste0("dataset/FLAD_curve-linear-mig-", mig[j], "-2deme_",i,".csv")
        
        data_100 <- read.csv(file_path_100)

        data_100 <- data_100[1:100,]

        data_100$migration_rate <- as.numeric(mig[j])
        
        # Calculate the average and append it to the average_data data frame
        if (i == 1) {
            average_data_fit_100[[j]] <- data_100
        } else {
            average_data_fit_100[[j]] <- average_data_fit_100[[j]] + data_100
        }
    }
}
# Divide the sum by the number of data files to get the average
average_data_fit_100 <- lapply(average_data_fit_100, function(x) x / 20)

output <- data.frame()

# output the data in csv format
for (i in 1:5) {
    output <- rbind(output, average_data_fit_100[[i]])
}

write.csv(output, "average_data.csv", row.names = FALSE)


