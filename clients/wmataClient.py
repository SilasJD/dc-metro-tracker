from clients.clientUtil import *
import json


def getArrivalPredictions(mainLineDict):

    conn, headersList, payload = getBaseClientVars()
    conn.request("GET", "/StationPrediction.svc/json/GetPrediction/All", payload, headersList)
    response = conn.getresponse()
    result = response.read()

    result_json = json.loads(result)

    predictionDict = {}


    for train in result_json.get("Trains"):
                
        if train.get("Line") in mainLineDict:
            if train.get("Line") not in predictionDict:
                predictionDict[train.get("Line")] = []
                predictionDict[train.get("Line")].append(train)

            else:
                predictionDict[train.get("Line")].append(train)

    return predictionDict



def getStationInfo():
    conn, headersList, payload = getBaseClientVars()

    conn.request("GET", f"/Rail.svc/json/jStations", payload, headersList)
    stop_response = conn.getresponse()
    stop_result = stop_response.read()

    stop_json = json.loads(stop_result)

    stationDict = {}

    for station in stop_json.get("Stations"):
        stationDict[station.get("Code")] = [station.get("Lat"), station.get("Lon")]

    return stationDict


def getTrainPositions(mainLineDict, circuitIdMap):
    conn, headersList, payload = getBaseClientVars()

    conn.request("GET", "/TrainPositions/TrainPositions?contentType=json", payload, headersList)
    position_response = conn.getresponse()
    position_result = position_response.read()

    position_json = json.loads(position_result)

    trainDict = {}

    for train in position_json.get("TrainPositions"):
        if train.get("LineCode") in mainLineDict:
            if train.get("CircuitId") in circuitIdMap:
                
                if train.get("LineCode") not in trainDict.keys():
                    trainDict[train.get("LineCode")] = {}
                trainDict[train.get("LineCode")][train.get("TrainId")] = [circuitIdMap[train.get("CircuitId")], train.get("DirectionNum")]
                
    return trainDict