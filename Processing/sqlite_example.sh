#!/usr/bin/env bash

# Create "tracks" table
sqlite3 example.db \
"CREATE TABLE tracks (
  track_id varchar(18) NOT NULL,
  song_id varchar(18) NOT NULL,
  artist varchar(256) DEFAULT NULL,
  title varchar(256) DEFAULT NULL,
  PRIMARY KEY (track_id)
);"

# Read 1000 first lines of unique_tracks.txt, escape double quotes and insert them into sqlite database
head -n 1000000 unique_tracks.txt |
while read line; do
    sqlite3 example.db "INSERT INTO tracks VALUES (\"$(echo -e $line | sed 's/"/""/g' | sed 's/<SEP>/","/g')\");";
done

# Count unique tracks
# sqlite3 example.db "SELECT COUNT(1) FROM tracks;"
