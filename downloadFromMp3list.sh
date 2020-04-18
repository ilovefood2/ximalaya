#!/bin/bash
filename='mp3.txt'
cat $filename | while read line
do  
    name=$(echo $line|cut -d "|" -f 1)
    url=$(echo $line|cut -d "|" -f 2)
    axel -a -n 10 $url -o "$name"
done  