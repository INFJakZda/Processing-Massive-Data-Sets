#!/bin/bash
#Which start files to use?
unique_tracks="unique_tracks2.txt"
triplets_sample="triplets_sample_20.txt"

#Set timezone for ex4
TZ=GMT0;
export TZ;

# PREPARING DATA - STAR SCHEMA
#**************************************************************
# 1) Change encoding to ISO - readable form
iconv -t UTF-8 -f ISO-8859-2 $unique_tracks > unique_formatted.txt

# 2) Remove duplicated song_id & sort (track_id,SONG_ID,artist,title)
sed -i -e $'s/<SEP>/,/g' unique_formatted.txt
cut -d $',' -f 2- unique_formatted.txt > tracks.txt
rm unique_formatted.txt
sort --output=tracksFormatt.txt tracks.txt
rm tracks.txt
awk -F ',' '!NF || !seen[$2]++' tracksFormatt.txt > ./out/tracksFormatted.txt
rm tracksFormatt.txt
