# 我有十个格式相同的数据集，分别在文件夹data_1/, data_2/, ..., data_10/中，文件名为FLAD_curve-linear-eff-0.00-tracking.csv，假设它们都是m行n列。我希望得到一个新的数据集，也是m行n列，其中每个位置的数据都是这两个数据集中对应位置的平均值。请问要怎么做？

# Create an empty data frame to store the average values
average_data_0 <- data.frame()
average_data_1 <- data.frame()
average_data_2 <- data.frame()
average_data_3 <- data.frame()
average_data_4 <- data.frame()

# Loop through each data file
for (i in 1:20) {
    # Read the data file
    file_path_0 <- paste0("dataset/FLAD_curve-linear-eff-0.00-tracking_",i,".csv")
    file_path_1 <- paste0("dataset/FLAD_curve-linear-eff-0.25-tracking_",i,".csv")
    file_path_2 <- paste0("dataset/FLAD_curve-linear-eff-0.50-tracking_",i,".csv")
    file_path_3 <- paste0("dataset/FLAD_curve-linear-eff-0.75-tracking_",i,".csv")
    # file_path_4 <- paste0("dataset/FLAD_curve-linear-eff-1.00-tracking_",i,".csv")

    data_0 <- read.csv(file_path_0)
    data_1 <- read.csv(file_path_1)
    data_2 <- read.csv(file_path_2)
    data_3 <- read.csv(file_path_3)
    # data_4 <- read.csv(file_path_4)

    data_0$adult_female_population_size <- data_0$adult_female_population_size
    data_0$adult_population_size <- data_0$adult_population_size
    data_1$adult_female_population_size <- data_1$adult_female_population_size
    data_1$adult_population_size <- data_1$adult_population_size
    data_2$adult_female_population_size <- data_2$adult_female_population_size
    data_2$adult_population_size <- data_2$adult_population_size
    data_3$adult_female_population_size <- data_3$adult_female_population_size
    data_3$adult_population_size <- data_3$adult_population_size
    # data_4$adult_female_population_size <- data_4$adult_female_population_size * 7 / 5
    # data_4$adult_population_size <- data_4$adult_population_size * 7 / 5
    
    # Calculate the average and append it to the average_data data frame
    if (i == 1) {
        average_data_0 <- data_0
        average_data_1 <- data_1
        average_data_2 <- data_2
        average_data_3 <- data_3
        # average_data_4 <- data_4
    } else {
        average_data_0 <- average_data_0 + data_0
        average_data_1 <- average_data_1 + data_1
        average_data_2 <- average_data_2 + data_2
        average_data_3 <- average_data_3 + data_3
        # average_data_4 <- average_data_4 + data_4
    }
}

# Divide the sum by the number of data files to get the average
average_data_0 <- average_data_0 / 20
average_data_1 <- average_data_1 / 20
average_data_2 <- average_data_2 / 20
average_data_3 <- average_data_3 / 20
# average_data_4 <- average_data_4 / 10

# output the data in csv format
write.csv(average_data_0, "average_data_0.00.csv", row.names = FALSE)
write.csv(average_data_1, "average_data_0.25.csv", row.names = FALSE)
write.csv(average_data_2, "average_data_0.50.csv", row.names = FALSE)
write.csv(average_data_3, "average_data_0.75.csv", row.names = FALSE)
# write.csv(average_data_4, "average_data_1.00.csv", row.names = FALSE)









