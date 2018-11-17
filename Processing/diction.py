import time

#Song table **************************************
#songId: 'title'
songIdTitle = {}
#songId: 'Artist'
songIdArtist = {}

#songId: noListened - HELPER
songIdCount = {}
#Artist: noSongs    - HELPER
ArtistCount = {}
#songId's of Queen  - HELPER
Queen = []

#User table **************************************
#dict of key userId and values are dict of songId: count and there is couter c: n
#userId: {song1: 3, song2: 8,.....}
userSongId = {}

#Date table **************************************
monthCount = {}

def prepareData(triplets, unique):
    with open(triplets,'r') as fp:
        for line in fp:
            #IdUser, IdSong, timestamp
            values = line.strip().split('<SEP>')
            
            #songIdCount
            if values[1] not in songIdCount:
                songIdCount[values[1]] = 1
            else:
                songIdCount[values[1]] += 1
            
            #userSongId
            if values[0] not in userSongId:
                userSongId[values[0]] = { values[1]: 1, 1: 1 }
            elif values[1] not in userSongId[values[0]]:
                userSongId[values[0]][values[1]] = 1
                userSongId[values[0]][1] += 1
            else:
                userSongId[values[0]][values[1]] += 1

            #monthCount
            month = time.gmtime(int(values[2]))[1]
            if month not in monthCount:
                monthCount[month] = 1
            else:
                monthCount[month] += 1
            

    with open(unique, 'r', encoding = "ISO-8859-1") as fp:
        for line in fp:
            #trackId, songId, Artist, title
            values = line.strip().split('<SEP>')
            
            #songIdTitle
            if values[1] not in songIdTitle:
                songIdTitle[values[1]] = values[3]

            #songIdArtist
            if values[1] not in songIdArtist:
                songIdArtist[values[1]] = values[2]
            
            #ArtistCount
            if values[2] not in ArtistCount:
                ArtistCount[values[2]] = 0

            #Queen
            if values[2] == 'Queen':
                Queen.append(values[1])


def zad1():
    sorted_by_value = sorted(songIdCount.items(), key=lambda kv: kv[1], reverse = True)[:10]
    for song in sorted_by_value:
        print(songIdTitle[song[0]] + ' ' + songIdArtist[song[0]] + ' ' + str(song[1]))

def zad2():
    sorted_by_value = sorted(userSongId.items(), key=lambda x: x[1][1], reverse = True)[:10]
    for song in sorted_by_value:
        print(song[0] + ' ' + str(song[1][1]))

def zad3():
    for songId, counter in songIdCount.items():
        ArtistCount[songIdArtist[songId]] += counter
    artist = sorted(ArtistCount.items(), key=lambda kv: kv[1], reverse = True)[0]
    print(artist[0] + ' ' + str(artist[1]))

def zad4():
    sorted_by_value = sorted(monthCount.items(), key=lambda kv: kv[0])
    for month in sorted_by_value:
        print(str(month[0]) + ' ' + str(month[1]))

def zad5():
    QueenDict = {}
    for song in Queen:
        if song in songIdCount:
            QueenDict[song] = songIdCount[song]
    sorted_by_value = sorted(QueenDict.items(), key=lambda kv: kv[1], reverse = True)[:3]
    indexesOfQueen = [idx[0] for idx in sorted_by_value]
    
    queenFans = []
    for userId, songs in userSongId.items():
        songsOfUser = list(songs.keys())
        if (all(elem in songsOfUser  for elem in indexesOfQueen)):
            queenFans.append(userId)
    queenFans.sort()
    for ele in queenFans[:10]:
        print(ele)


if __name__ == '__main__':
    triplets = "triplets_sample_20p.txt"
    unique = "unique_tracks.txt"

    prepareData(triplets, unique)

    #EXECRICES
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()