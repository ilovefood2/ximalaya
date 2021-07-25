###############################################
# Created by Kelvin J. 
# Steps: 
#	1. get item ID from ximalay website (inside of url)
#       2. copy item id and replace the number in the first line
#       3. run this script in terminal to download all mp3 files
# Prerequisite: 
#		jp has to be installed before hand  
#		on macOS, do brew install jq 
###############################################


json=`curl -s -X GET http://www.ximalaya.com/sets/5461987.ext.json`
title0=$(echo $json | jq -r '.title')
length=$(echo $json | jq '.tracks' | jq 'length')
uplimit=$(echo $(($length-1)))
mkdir -p $title0
# function download(){
# 	track=$(echo $json | jq --argjson v "$i" '.tracks[$v] | [.title, .play_url]')
# 	#echo $track
# 	title=$(echo $track | jq -r '.[0]')
# 	url=$(echo $track | jq -r '.[1]')

#  	aria2c -d $title0 -o $title.mp3 -j 10  $url 
# }
for ((i=0;i<$uplimit;i++))
do   
	track=$(echo $json | jq --argjson v "$i" '.tracks[$v] | [.title, .play_url]')
	#echo $track
	title=$(echo $track | jq -r '.[0]')
	url=$(echo $track | jq -r '.[1]')

 	aria2c -d $title0 -o $title.mp3 -j 10  $url 
 done
# v=$uplimit; 
# d=${v:(-1)}; 
# c=${v%$d}; 

# for i in `seq 1 $c`; 
# do 
# 	echo "[$(( i * 10 -9))..$(( i * 10 ))]" ; 
# done; 

# echo "[$(( c * 10 + 1 ))..$v]"
