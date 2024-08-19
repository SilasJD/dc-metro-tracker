import http.client


def getBaseClientVars():
    conn = http.client.HTTPSConnection("api.wmata.com")
 
    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "api_key": "f315fc569a854b00b3e0f3fd36ada7de" 
    }

    payload = ""

    return conn, headersList, payload
