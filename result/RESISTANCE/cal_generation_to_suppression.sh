#!/bin/bash

files=`cat checkerRes/full_file_name_without_suffix.txt`

cd dataset

# Check suppression rate

echo "resistance_rate,drop_ratio,drive_efficiency,low_density_growth_rate,density_growth_curve,generation_to_suppression,type"

for file in $files
do
    #  在 raw_data/ 中找到相应的 file
    #  按最后一行判断是否抑制了
    # generation,size,female_size,fertile_female_size,rate_dr,rate_has_drive,drive_efficiency,germline_resistance,drop_ratio,embryo_resistance,low_density_growth_rate,density_growth_curve
    ##! csv 表头：
    # 1 generation, 2 size,           3 female_size,      4 fertile_female_size,
    # 5 rate_dr,    6 rate_has_drive, 7 drive_efficiency, 8 germline_resistance,
    # 9 drop_ratio,      10 embryo_resistance,     11 low_density_growth_rate, 12 density_growth_curve
    ##! 文件名中有 fitness 取值信息
    # 文件名：`FLAD_curve-linear-fit-<value>-drop-<value>-ldgr-<value>.csv`
    # echo $filename | cut -f 4 -d '-'
    ##! A - 最后一行为抑制：
    ##   rate_wt = 0.0
    ##   rate_dr = 1.0
    ##   female_size = 0
    ##   size = 0
    ##! B - 最后一行为drive丢失：
    ##   rate_wt = 1.0
    ##   rate_dr = 0.0
    ##! C - 最后一行为long：
    ##   else

    # 记录数据
    last_rows=`tail -n 2 ${file}* | grep -v "==>" | grep -v "^$"`
    # rate_wt=`echo $last_rows | cut -f 1 -d ',' | head -n 1`
    # rate_drive=`echo $last_rows | cut -f 2 -d ',' | head -n 1`
    type=`echo $file | cut -f 6 -d '_'`
    drive_efficiency=`echo $last_rows | cut -f 9 -d ',' | head -n 1`
    resistance_rate=`echo $file | cut -f 3 -d '_'`
    drop_ratio=`echo $last_rows | cut -f 10 -d ',' | head -n 1`
    low_density_growth_rate=`echo $last_rows | cut -f 11 -d ',' | head -n 1`
    density_growth_curve=`echo $last_rows | cut -f 12 -d ',' | head -n 1 | cut -f 1 -d ' '`

    suppression_times=0
    total_times=0
    sum_generation=0

    for row in $last_rows
    do
        rate_drive=`echo $row | cut -f 6 -d ','`
        generation=`echo $row | cut -f 1 -d ','`
        female_size=`echo $row | cut -f 3 -d ','`

        # 判断是否抑制
        if [[ $rate_drive == "1.0" ]] || [[ $female_size == "0" ]]; then
            let sum_generation=sum_generation+generation
            let total_times++
        fi

    done

    # echo $total_times

    if [[ $sum_generation == 0 ]]; then
        generation="NAN"
    else
        generation=`echo "scale=3; ($sum_generation/$total_times) - 10" | bc`
    fi

    # Output format:
    # method, drive_efficiency, drop_ratio, suppression_rate
    # FLAD, 1.0, 0.3, 1.0
    # SIT, 0.0, 0.5, 1.0

    # echo "drive_fitness,drop_ratio,drive_efficiency,low_density_growth_rate,generation_to_suppression,density_growth_curve"
    # echo "resistance_rate,drop_ratio,drive_efficiency,low_density_growth_rate,density_growth_curve,generation_to_suppression,type"
    echo "$resistance_rate,$drop_ratio,$drive_efficiency,$low_density_growth_rate,$density_growth_curve,$generation,$type"

done

cd ..