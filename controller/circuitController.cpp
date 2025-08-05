/// @file    ColorTemperature.ino
/// @brief   Demonstrates how to use @ref ColorTemperature based color correction
/// @example ColorTemperature.ino
#include <map>
#include <vector>
#include <FastLED.h>

#define LED_PIN     8

// Information about the LED strip itself
#define NUM_LEDS    256
#define CHIPSET     WS2811
#define COLOR_ORDER GRB
CRGB leds[NUM_LEDS];

#define BRIGHTNESS  30

#define TEMPERATURE_1 Tungsten100W
#define TEMPERATURE_2 OvercastSky

// How many seconds to show each temperature before switching
#define DISPLAYTIME 20
// How many seconds to show black between switches
#define BLACKTIME   3



void loop()
{
  
  String inputString = Serial.readString();

    
    // Infinite loop to keep updating
    std::map<String, CRGB> colorMap = {
        {"RD", CRGB::Red},
        {"BL", CRGB::Blue},
        {"YL", CRGB::Yellow},
        {"OR", CRGB::Orange},
        {"GR", CRGB::Green},
        {"SV", CRGB::Silver}
    };

  inputString.trim();
  inputString.replace("'", "");  // clean outer quotes if needed

  // Split the string into tokens using '|' as the delimiter
  std::vector<String> tokens;
  int start = 0;
  while (start < inputString.length()) {
    int end = inputString.indexOf('|', start);
    if (end == -1) {
      tokens.push_back(inputString.substring(start));
      break;
    } else {
      tokens.push_back(inputString.substring(start, end));
      start = end + 1;
    }
  }

  // Process each slot as one LED
  for (int i = 0; i < NUM_LEDS; i++) {
    String token = (i < tokens.size()) ? tokens[i] : "";
    token.trim();

    int row = i / 16;
    int col = i % 16;
    int ledIndex = (row % 2 == 1) ? (row * 16 + col) : ((row + 1) * 16 - 1 - col);

    String key = token.c_str();

    if (key.isEmpty()) {
      leds[ledIndex] = CRGB::Black;
    } else if (colorMap.count(key)) {
      leds[ledIndex] = colorMap[key];
    } else {
      leds[ledIndex] = CRGB::Black;
    }
  }

  FastLED.show();
  delay(1000);
  
}



void setup() {
  // It's important to set the color correction for your LED strip here,
  // so that colors can be more accurately rendered through the 'temperature' profiles
  Serial.begin(9600);
  FastLED.addLeds<CHIPSET, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalSMD5050 );
  FastLED.setBrightness( BRIGHTNESS );
}

