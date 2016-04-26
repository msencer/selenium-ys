
int buttonPin = D0;
int ledPin = D7;
int buttonState = 0;

void setup(){

  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  //  particle serial monitor
  Serial.begin(115200);

  // Lets listen for the hook response
  Particle.subscribe("hook-response/order_0001", orderResponse, MY_DEVICES);
  //
  // for(int i=0;i<10;i++) {
  //   Serial.println("waiting " + String(10-i) + " seconds before we publish");
  //   // delay(1000);
  // }
  //

  delay(500);

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
  Particle.publish("order_0001");

}

void orderResponse(const char *name, const char *data) {

String str = String(data);

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
