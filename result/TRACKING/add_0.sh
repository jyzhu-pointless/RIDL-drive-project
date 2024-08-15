#!/bin/bash
files=$(ls dataset/*eff-1.00*)

for file in $files; do
    last_row=$(tail -n 2 $file | head -n 1)
    generation=$(echo $last_row | cut -d ',' -f 1)
    new_file=$(echo $file | sed 's/.csv/_copy.csv/')
    cp $file $new_file
    sed -i '' '/^$/d' $new_file
    
    if [ $generation -eq 317 ]; then
        continue
    fi
    for i in $(seq $(expr $generation + 1) 317); do
        echo $i,0,0,0,0.5,0.5,1.0 >> $new_file
    done
done