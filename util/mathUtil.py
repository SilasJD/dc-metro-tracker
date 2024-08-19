import math
from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


def minDistanceOfSegment(trainPos, stopAPos, stopBPos):

    # Step 1: Calculate the vectors
    AB = [stopBPos[0] - stopAPos[0], stopBPos[1] - stopAPos[1]]
    AP = [trainPos[0] - stopAPos[0], trainPos[1] - stopAPos[1]]
    
    # Step 2: Calculate the dot products and the parameter t
    AB_dot_AB = AB[0]**2 + AB[1]**2
    AP_dot_AB = AP[0] * AB[0] + AP[1] * AB[1]
    
    t = AP_dot_AB / AB_dot_AB
    
    # Step 3: Find the closest point on the segment
    if t < 0:
        closest_point = [stopAPos[0], stopAPos[1]]
    elif t > 1:
        closest_point = [stopBPos[0], stopBPos[1]]
    else:
        closest_point = [stopAPos[0] + t * AB[0], stopAPos[1] + t * AB[1]]
    
    # Step 4: Calculate the distance from the point to the closest point on the segment
    distance = math.sqrt((trainPos[0] - closest_point[0])**2 + (trainPos[1] - closest_point[1])**2)
    
    return distance


def findClosestStations(trainCoords, orderedStationList, stationLocationDict):

    minDistance =100000000
    stationA = ""
    stationB = ""

    for i in range(0, len(orderedStationList)):
        if i >= len(orderedStationList) - 1:
            break
        
        distanceFromStations = minDistanceOfSegment(trainCoords[0], stationLocationDict[orderedStationList[i]], stationLocationDict[orderedStationList[i+1]])

        if distanceFromStations < minDistance:
            minDistance = distanceFromStations
            stationA = orderedStationList[i]
            stationB = orderedStationList[i+1]

        i += 1

    return stationA, stationB