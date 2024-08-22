from util.metroUtil import *
from clients.wmataClient import *
from util.mathUtil import *
import time
import os
import copy

def main():

    circuitMap = loadCircuitMap()

    mainLineDict = getMainLineDict()
    stationLocationDict = getStationInfo()
    trainPositionDict = getTrainPositions(mainLineDict, circuitMap)

    allTrainLocationsDict = getEmptyTrainLocationsDict(mainLineDict)

    lineText = ""
    for line in mainLineDict:
        
        lineTrainPositionDict = trainPositionDict[line]
        locationDict1 = getLocationDict(mainLineDict[line], 1)
        locationDict2 = getLocationDict(mainLineDict[line], 2)

        for train in lineTrainPositionDict:
            stationA, stationB = findClosestStations(lineTrainPositionDict[train], mainLineDict[line], stationLocationDict)

            distanceFromA = haversine(lineTrainPositionDict[train][0][0], lineTrainPositionDict[train][0][1], stationLocationDict[stationA][0], stationLocationDict[stationA][1])
            distanceFromB = haversine(lineTrainPositionDict[train][0][0], lineTrainPositionDict[train][0][1], stationLocationDict[stationB][0], stationLocationDict[stationB][1])


            if(lineTrainPositionDict[train][1] == 1):
                if distanceFromA < 0.06: 
                    index = stationA + "->"
                    allTrainLocationsDict[index].append(line)
                    locationDict1[index].append(train)
                elif distanceFromB < 0.06: 
                    index = stationB + "->"
                    allTrainLocationsDict[index].append(line)
                    locationDict1[index].append(train)
                else:
                    middleLoc = stationA + "->" + stationB
                    allTrainLocationsDict[middleLoc].append(line)
                    locationDict1[middleLoc].append(train)

            if(lineTrainPositionDict[train][1] == 2):
                if distanceFromA < 0.06: 
                    index = stationA + "<-"
                    allTrainLocationsDict[index].append(line)
                    locationDict2[index].append(train)
                elif distanceFromB < 0.06:
                    index = stationB + "<-" 
                    allTrainLocationsDict[index].append(line)
                    locationDict2[index].append(train)
                else:
                    middleLoc = stationA + "<-" + stationB
                    allTrainLocationsDict[middleLoc].append(line)
                    locationDict2[middleLoc].append(train)

        for loc in locationDict2:

            if len(locationDict2[loc]) == 0:
                lineText = lineText + f'{"-": ^4}' + "|"
            else:
                for train in locationDict2[loc]:
                    lineText = lineText + f'{train: ^4}' + "|"
        
        lineText =  lineText + '\n' + getHeaders(line, 2) + '\n'
        lineText = lineText + getHeaders(line, 1) + '\n'
        
        for loc in locationDict1:

            if len(locationDict1[loc]) == 0:
                lineText = lineText + f'{"-": ^4}' + "|"
            else:
                for train in locationDict1[loc]:
                    lineText = lineText + f'{train: ^4}' + "|"

        print(lineText + "\n")
        lineText = ""
    

            
# Start the label updates
while True: 
    main()
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

