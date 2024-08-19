from __future__ import barry_as_FLUFL
from ast import Break
import code
from pydoc import resolve
import json
from random import randint
import webbrowser
import time
import requests
from datetime import datetime
import http.client
import math
from math import radians, cos, sin, asin, sqrt
import matplotlib
import matplotlib.pyplot as plt
import folium
matplotlib.use('TkAgg')
from metro_predictor import plotTrains
import numpy as np









def main():

    mainLineDict = {"RD"}
    redLineList = ["A15", "A14", "A13", "A12", "A11", "A10", "A09", "A08", "A07", "A06", "A05", "A04", 'A03', 'A02', 'A01', 'B01', 'B02','B03','B35','B04','B05','B06','B07','B08','B09','B10','B11']

    locationDict = {}

    for i in range(0, len(redLineList)):
        if i >= len(redLineList) - 1:
            break
        locationDict[redLineList[i]] = []
        middleLoc = str(redLineList[i]) + "->" + str(redLineList[i+1])
        locationDict[middleLoc] = []


    arrivalPredictionDict = getArrivalPredictions(mainLineDict)

    stationLocationDict = getStationInfo()

    trainPosDict = getTrainPositions(mainLineDict)

    for train in trainPosDict:
        stationA, stationB = findClosestStations(trainPosDict[train], redLineList, stationLocationDict)

        distanceFromA = haversine(trainPosDict[train][0][0], trainPosDict[train][0][1], stationLocationDict[stationA][0], stationLocationDict[stationA][1])
        distanceFromB = haversine(trainPosDict[train][0][0], trainPosDict[train][0][1], stationLocationDict[stationB][0], stationLocationDict[stationB][1])


        if(trainPosDict[train][1] == 1):
            if distanceFromA < 0.06: 
                locationDict[stationA].append(train)
                # print("Train " + train + " is BOARDING from station " + stationA + " heading East")
            elif distanceFromB < 0.06: 
                locationDict[stationB].append(train)
                # print("Train " + train + " is BOARDING from station " + stationB + " heading East")
            else:
                middleLoc = stationA + "->" + stationB
                locationDict[middleLoc].append(train)
                # print("Train " + train + " is heading from station " + stationA + " to station " + stationB + " Eastbound")

        # if(trainPosDict[train][1] == 2):
        #     if distanceFromA < 0.06: 
        #         # print("Train " + train + " is BOARDING from station " + stationA + " heading West")
        #         ledRedLineWest = ledRedLineWest.replace(stationA + "(   )",  stationA + "(" + train + ")")
        #     elif distanceFromB < 0.06: 
        #         # print("Train " + train + " is BOARDING from station " + stationB + " heading West")
        #         ledRedLineWest = ledRedLineWest.replace(stationB + "(   )",  stationA + "(" + train + ")")
        #     else:
        #         # print("Train " + train + " is heading from station " + stationB + " to station " + stationA + " Westbound")
        #         ledRedLineEast = ledRedLineEast.replace(stationA+ "(   )" + "---" + stationB, stationA + "-" + train + "-" + stationB)

            # else: 
            #     print("Train " + train + " is " + str(distanceFromA) + " from station " + stationA + " and " + str(distanceFromB) + " from station " + stationB)





        # if distanceFromA < 0.06: 
        #     print("Train " + train + " is BOARDING from station " + stationA)
        # elif distanceFromB < 0.06: 
        #     print("Train " + train + " is BOARDING from station " + stationB)
        # else: 
        #     print("Train " + train + " is " + str(distanceFromA) + " from station " + stationA + " and " + str(distanceFromB) + " from station " + stationB)




    # for redLineTrain in arrivalPredictionDict["RD"]:
    #     if(redLineTrain.get("Group")) == '1':
    #         if redLineTrain.get("Min") == "ARR" or redLineTrain.get("Min") == "BRD":
    #             ledRedLineEast = ledRedLineEast.replace(redLineTrain.get("LocationCode"), "XXX")



    #     if(redLineTrain.get("Group")) == '2':
    #         if redLineTrain.get("Min") == "ARR" or redLineTrain.get("Min") == "BRD":
    #             ledRedLineWest = ledRedLineWest.replace(redLineTrain.get("LocationCode"), "XXX")

    header = ""
    for loc in locationDict:
        if len(loc) == 3:
            header = header + f'{loc: ^4}' + "|"
        else:
            header = header + f'{"-->": ^4}' + "|" 

    line = ""
    for loc in locationDict:

        if len(locationDict[loc]) == 0:
            line = line + f'{"-": ^4}' + "|"
        else:
            for train in locationDict[loc]:
                line = line + f'{train: ^4}' + "|"
    # print("Red Line West Bound: " + ledRedLineWest)


   
    print(line)



header = ""
for loc in redLineList:
    if loc == "B11":
        break
    header = header + f'{loc: ^4}' + "|" + f'{"-->": ^4}' + "|"
    
print(header)
while True:
    main()
    # plotTrains()
    time.sleep(3)