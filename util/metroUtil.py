import json
from re import L

def loadCircuitMap():
    
    circuitIdMap = {}

    with open('C:/Users/sjdun/dc-metro-tracker/dc-metro-tracker/track-circuit-gps-coords.json') as f:
        d = json.load(f)
        for circuit in d:
            circuitIdMap[circuit.get("track_circuit_id")] = []
            circuitIdMap[circuit.get("track_circuit_id")].append(circuit.get("lat"))
            circuitIdMap[circuit.get("track_circuit_id")].append(circuit.get("lon"))

    return circuitIdMap

def printHeaders(color):

    mld = getMainLineDict()
    ld = getLocationDict(mld[color])
    header = ""
    for loc in ld:
        if len(loc) == 3:
            header = header + f'{loc: ^4}' + "|"
        else:
            header = header + f'{"-->": ^4}' + "|" 

    print(header)
    return 

def getMainLineDict():

    mainLineDict = {}

    #red
    mainLineDict["RD"] = ["A15", "A14", "A13", "A12", "A11", "A10", "A09", "A08", "A07", "A06", "A05", "A04", 'A03', 'A02', 'A01', 'B01', 'B02','B03','B35','B04','B05','B06','B07']

    #blue
    mainLineDict["BL"] = ['J03','J02','C13','C12','C11','C10','C09','C08','C07','C06','C05','C04','C03','C02','C01','D01','D02','D03','D04','D05','D06','D07','D08','G01','G02','G03','G04','G05']

    #yellow
    mainLineDict["YL"] = ['C15','C14','C13','C12','C11','C10','C09','C08','C07','F03','F02','F01','E01','E02','E03','E04','E05','E06']

    #silver
    mainLineDict["SV"] = ['N12','N11','N10','N09','N08','N07','N06','N04','N03','N02','N01','K05','K04','K03','K02','K01','C05','C04','C03','C02','C01','D01','D02','D03','D04','D05','D06','D07','D08','G01','G02','G03','G04','G05']

    #green
    mainLineDict["GR"] = ['E10','E09','E08','E07','E06','E05','E04','E03','E01','F01','F02','F03','F04','F05','F06','F07','F08','F09','F10','F11']

    #orange
    mainLineDict["OR"] = ['K08','K07','K06', 'K05','K04','K03','K02','K01', 'C05','C04','C03','C02','C01','D01','D02','D03','D04','D05','D06','D07','D08','D09', 'D10', 'D11','D12','D13']

    return mainLineDict

#returns a dict of all possible line locations (leds) with a value of an empty list for populating with trains
def getLocationDict(lineList):
    
    locationDict = {}
    
    for i in range(0, len(lineList)):
        if i > len(lineList) - 1:
            break
        locationDict[lineList[i]] = []
        if i < len(lineList)-1:
            middleLoc = str(lineList[i]) + "->" + str(lineList[i+1])
            locationDict[middleLoc] = []

    return locationDict


