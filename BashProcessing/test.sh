#!/bin/bash
#Which start files to use?
unique_tracks="unique_tracks.txt"
triplets_sample="triplets_sample_20p.txt"

#Set timezone for ex4
TZ=GMT0;
export TZ;

# PREPARING DATA - STAR SCHEMA
#**************************************************************
# 1) Change encoding to ISO - readable form
iconv -t UTF-8 -f ISO-8859-2 $unique_tracks > unique_formatted.txt

# 2) Remove duplicated song_id & sort (track_id,SONG_ID,artist,title)
#change <SEP> to ','
sed -i -e $'s/<SEP>/,/g' unique_formatted.txt
#sed -i -e $'s/<SEP>/,/g' $triplets_sample
#rm track_id
cut -d $',' -f 2- unique_formatted.txt > tracks.txt
rm unique_formatted.txt
#sort tracks
sort --output=tracksFormatt.txt tracks.txt
rm tracks.txt
#rm duplicates
awk -F ',' '!NF || !seen[$1]++' tracksFormatt.txt > ./out/tracksFormatted.txt
rm tracksFormatt.txt
# OUT: ./out/tracksFormatted.txt

# 3) Create dates.txt (%Y,%m,%d) & prepare ZAD1
gawk -F '<SEP>' '{
  year_month_day = strftime("%Y,%m,%d", $3);
  print year_month_day > "./out/dates.txt";
  listen[$2]++;
}
END {
  for (key in listen) {
    print key "," listen[key] > "./out/exercise1.txt"
  }
}' $triplets_sample
#*************************************************************************
#EXERCISES:

#ZAD 1
#sortowanie odsłuchań i sortowanie wyniku
sort --numeric-sort -t $',' -k 2 -r ./out/exercise1.txt | head -n 10 | sort -t $',' -k 1 > exercise1_sort.txt
#połączenie z tytułami i autorami
join -1 1 -t $',' exercise1_sort.txt ./out/tracksFormatted.txt > exercise1_join.txt
#sortowanie od nowa względem odsłuchań
sort --numeric-sort -t $',' -k 2 -r exercise1_join.txt > exercise1_result.txt
#pokazanie wyniku
gawk -F $',' '{
  print $4 " " $3 " " $2
}' exercise1_result.txt
#usunięcie pomocniczych plików
rm exercise1_sort.txt exercise1_join.txt exercise1_result.txt
#------------------------------------------------------

#ZAD 2
gawk -F '<SEP>' '{
  usersongs[$1][$2] = 1
}
END {
  for (key in usersongs) {
    print key " " length(usersongs[key])
  }
}' $triplets_sample | sort --numeric-sort -k2 -r | head -n 10
#------------------------------------------------------

# ZAD 4
gawk -F ',' '{
  months[$2]++;
}
END {
  n = asorti(months, indexes);
  for (i = 1; i <= n; i++) {
    print indexes[i] " " months[indexes[i]];
  }
}' ./out/dates.txt
#------------------------------------------------------
