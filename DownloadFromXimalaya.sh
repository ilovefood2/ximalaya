###############################################
# Created by Kelvin J. 
# Usage: 
#	1. get albumId from ximalay website (inside of url) 
#       2. run this script in terminal as following: 
#		   ./DownloadFromXimalaya.sh ${albumId}  
# Prerequisite: 
#		jp has to be installed before hand   
###############################################
#!/usr/bin/env bash


albumId=${1?Error: no albumId given}

json=`curl -s -X GET http://www.ximalaya.com/sets/${albumId}.ext.json`

title0=$(echo $json | jq -r '.title')
length=$(echo $json | jq '.tracks' | jq 'length')
uplimit=$(echo $(($length-1)))
mkdir -p "$title0"
for ((i=0;i<$uplimit;i++))
do   
	track=$(echo $json | jq --argjson v "$i" '.tracks[$v] | [.title, .play_url]')
	#echo $track
	title=$(echo $track | jq -r '.[0]')
	url=$(echo $track | jq -r '.[1]')
	 
 	aria2c --file-allocation=none -d "$title0" -o "$title.mp3" -x 10 -j 20  "$url" 
done
echo "Finished..."
