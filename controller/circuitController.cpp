#include <iostream>
#include <sstream> 
#include <fstream>
#include <filesystem>
#include <thread>
#include <map>
#include <vector>
#include <FastLED.h>

using namespace std;

#define NUM_LEDS 5
#define DATA_PIN 3

CRGB leds[NUM_LEDS];


map<string, CRGB> colorMap = {
    {"RD", CRGB::Red},
    {"BL", CRGB::Blue},
};

bool isFileLocked(const string& lockFileName) {
    return filesystem::exists(lockFileName);
}

void updateLEDs(const map<string, vector<string>>& stationMap) {
    int ledIndex = 0;
    for (const auto& entry : stationMap) {
        for (const auto& train : entry.second) {
            if (ledIndex < NUM_LEDS) {
                leds[ledIndex] = colorMap.at(train);  // Update LED color based on train ID
                ledIndex++;
            }
        }
    }

    FastLED.show();  // Display the updated colors
}


int updateStationMap() {
    while (true) {
        if (!isFileLocked("C:/Users/sjdun/dc-metro-tracker/trainLocations.lock")) {
            ifstream file("C:/Users/sjdun/dc-metro-tracker/trainLocations.txt");
            string line, stationNumber, trainIds;
            if (file.is_open()) {
                map<string, vector<string>> stationMap;
                int station = 0;
                while (getline(file, stationNumber)) {
                    if (getline(file, trainIds)) {
                        vector<string> trains;
                        stringstream ss(trainIds);
                        string trainId;

                        while (getline(ss, trainId, ',')) {
                            trains.push_back(trainId);
                        }

                        stationMap[stationNumber] = trains;
                    }
                }
                file.close();
            }
        }
        
    }

}


void setup() {
    FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
}

void loop() {
    map<string, vector<string>> stationMap;

    while (true) {  // Infinite loop to keep updating
        updateStationMap(stationMap);  // Read file and update map
        updateLEDs(stationMap);  // Update LEDs based on the latest data
        this_thread::sleep_for(chrono::seconds(3));  // Wait for 3 seconds before next update
    }
}