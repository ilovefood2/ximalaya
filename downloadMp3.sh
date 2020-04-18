while read line
do

title=$(echo -ne $line|cut -d"," -f1) 
url=$(echo -ne $line|cut -d"," -f2)
#echo $title $url
 wget -O /Users/kelvin/Dropbox/Python_study/Ximalaya/mp3/$title.mp3 $url
done < '/Users/kelvin/Dropbox/Python_study/Ximalaya/mp3.txt'
