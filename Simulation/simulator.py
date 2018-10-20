import random
import collections
from random import randint
from itertools import combinations
import numpy as np
import numpy.ma as ma
from itertools import zip_longest

def decision(probability):
    return random.random() < probability

def chooseHotel(noHotels):
    return randint(0, noHotels - 1)

def makeKeyPair(p1, p2):
    if(p1 < p2):
        return str(p1) + " " + str(p2)
    else:
        return str(p2) + " " + str(p1)

def histMean(a):
    result = [np.ma.average(ma.masked_values(temp_list, None)) for temp_list in zip_longest(*a)]
    dict = {}
    i = 1
    for nr in result:
        dict[i] = round(nr)
        i += 1
    return dict

def generator(noPeople, probability, noHotels, noDays):
    #dictionary of every pair and count
    peoplePairs = {}
    uniquePeople = set()

    for day in range(noDays):
        #every hotel is empty list
        hotelsList = [[] for _ in range(noHotels)]
        
        #fill each hotel with random people
        for person in range(noPeople):
            if(decision(probability)):
                hotel = chooseHotel(noHotels)
                hotelsList[hotel].append(person)
        
        #count pairs in every hotel & add it to dictionary
        for hotelList in hotelsList:
            if hotelList:
                for p1 in range(len(hotelList)):
                    for p2 in range(p1 + 1, len(hotelList)):
                        pair = makeKeyPair(hotelList[p1], hotelList[p2])
                        if pair not in peoplePairs:
                            peoplePairs[pair] = 1
                        else:
                            uniquePeople.add(hotelList[p1])
                            uniquePeople.add(hotelList[p2])
                            peoplePairs[pair] += 1

    histList = []
    suspectPairs = 0
    suspectPairsDays = 0
    for k, v in peoplePairs.items():
        histList.append(v)
        if(v > 1):  
            suspectPairs += 1
            suspectPairsDays += len(list(combinations(range(v), 2)))          
    histogram = list(dict(collections.Counter(histList)).values())
    # print(suspectPairsDays)
    # print(suspectPairs)
    print(histogram)
    # print(len(uniquePeople))
    return [suspectPairsDays, suspectPairs, histogram, len(uniquePeople)]

def makeStats(n, p, h, d, noIterations):
    pairsDayPeople = []
    pairsPeople = []
    histogram = []
    people = []
    print("[INFO] Make stats")
    for i in range(noIterations):
        print("[INFO] " + str(i + 1) + " iteration")    
        pairDay, pair, hist, person = generator(n, p, h, d)
        pairsDayPeople.append(pairDay)
        pairsPeople.append(pair)
        histogram.append(hist)
        people.append(person)

    print("[RESULTS] *************")
    print(np.mean(pairsDayPeople), "    pary osób i dni")
    print(np.mean(pairsPeople), "    pary osób")
    print(histMean(histogram), "    histogram")
    print(np.mean(people), "    osób")


if __name__ == '__main__':
    n = 10000
    p = 0.16
    h = 100
    d = 100
    noIteration = 10

    makeStats(n, p, h, d, noIteration)