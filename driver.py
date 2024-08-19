from util.metroUtil import *
from clients.wmataClient import *
from util.mathUtil import *
import time

def main(displayColor):

    circuitMap = loadCircuitMap()

    mainLineDict = getMainLineDict()
    arrivalPredictionDict = getArrivalPredictions(mainLineDict) 
    stationLocationDict = getStationInfo()
    trainPositionDict = getTrainPositions(mainLineDict, circuitMap)

    for line in mainLineDict:
        
        lineArrivalPredictions = arrivalPredictionDict[line]
        lineTrainPositionDict = trainPositionDict[line]
        locationDict = getLocationDict(mainLineDict[line])

        for train in lineTrainPositionDict:
            stationA, stationB = findClosestStations(lineTrainPositionDict[train], mainLineDict[line], stationLocationDict)

            distanceFromA = haversine(lineTrainPositionDict[train][0][0], lineTrainPositionDict[train][0][1], stationLocationDict[stationA][0], stationLocationDict[stationA][1])
            distanceFromB = haversine(lineTrainPositionDict[train][0][0], lineTrainPositionDict[train][0][1], stationLocationDict[stationB][0], stationLocationDict[stationB][1])

            
            if(lineTrainPositionDict[train][1] == 1):
                if distanceFromA < 0.06: 
                    locationDict[stationA].append(train)
                elif distanceFromB < 0.06: 
                    locationDict[stationB].append(train)
                else:
                    middleLoc = stationA + "->" + stationB
                    locationDict[middleLoc].append(train)
        

        if line == displayColor:
            line = ""
            for loc in locationDict:

                if len(locationDict[loc]) == 0:
                    line = line + f'{"-": ^4}' + "|"
                else:
                    for train in locationDict[loc]:
                        line = line + f'{train: ^4}' + "|"

            print(line)

displayColor = "GR"

printHeaders(displayColor)

while True:
    main(displayColor)
    time.sleep(3)