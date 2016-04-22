
int buttonPin = D0;
int ledPin = D7;
int buttonState = 0;

void setup(){

  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  //  particle serial monitor
  Serial.begin(115200);

  // Lets listen for the hook response
  Particle.subscribe("hook-response/get_weather", orderResponse, MY_DEVICES);

  for(int i=0;i<10;i++) {
    Serial.println("waiting " + String(10-i) + " seconds before we publish");
    // delay(1000);
  }
  for (int i = 0; i < 3; i++) {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  }





}

void loop(){

  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    buttonCallback();
  }
  else {
    digitalWrite(ledPin, LOW);

  }

delay(1000);

}

void buttonCallback(){

  // get function for yemeksepeti will be here.

  digitalWrite(ledPin, HIGH);
  Serial.println("Requesting Order!");
  Particle.publish("get_weather");

}

void orderResponse(const char *name, const char *data) {

  String str = String(data);
  String locationStr = tryExtractString(str, "<location>", "</location>");
  String weatherStr = tryExtractString(str, "<weather>", "</weather>");
  String tempStr = tryExtractString(str, "<temp_f>", "</temp_f>");
  String windStr = tryExtractString(str, "<wind_string>", "</wind_string>");

  if (locationStr != NULL) {
      Serial.println("At location: " + locationStr); }
  if (weatherStr != NULL) {
      Serial.println("The weather is: " + weatherStr); }
  if (tempStr != NULL) {
      Serial.println("The temp is: " + tempStr + String(" *F")); }
  if (windStr != NULL) {
      Serial.println("The wind is: " + windStr); }

}

String tryExtractString(String str, const char* start, const char* end) {
    if (str == NULL) {
        return NULL;
    }

    int idx = str.indexOf(start);
    if (idx < 0) {
        return NULL;
    }

    int endIdx = str.indexOf(end);
    if (endIdx < 0) {
        return NULL;
    }

    return str.substring(idx + strlen(start), endIdx);
}
