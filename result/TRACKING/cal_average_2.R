# 我有十个格式相同的数据集，分别在文件夹data_1/, data_2/, ..., data_10/中，文件名为FLAD_curve-linear-eff-0.00-tracking.csv，假设它们都是m行n列。我希望得到一个新的数据集，也是m行n列，其中每个位置的数据都是这两个数据集中对应位置的平均值。请问要怎么做？

# Create an empty data frame to store the average values

average_data_4 <- data.frame()

# Loop through each data file
for (i in 1:20) {
    # Read the data file
    
    file_path_4 <- paste0("dataset/FLAD_curve-linear-eff-1.00-tracking_",i,"_copy.csv")


    data_4 <- read.csv(file_path_4)
    
    # Calculate the average and append it to the average_data data frame
    if (i == 1) {
        
        average_data_4 <- data_4
    } else {
        
        average_data_4 <- average_data_4 + data_4
    }
}

# Divide the sum by the number of data files to get the average


average_data_4 <- average_data_4 / 20

# output the data in csv format

write.csv(average_data_4, "average_data_1.00.csv", row.names = FALSE)









