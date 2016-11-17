/*
*  PREN 1 - TEAM 30
* Ultrasonic Controller
*
* Steuert 3 HC SR04 Ultrasonic Sensoren an. Die Messwerte werden permanent über eine Serielle
* Schnittstelle mit folgendem Datenformat ausgegeben: 
*
* ("\n""<sensor01>"","<sensor02>","<sensor03>""\0")   
*/

//Defines for SENSOR 1
#define echoPin01 7 // Echo Pin
#define trigPin01 8 // Trigger Pin

//Defines for SENSOR 2
#define echoPin02 6 // Echo Pin
#define trigPin02 5 // Trigger Pin

//Defines for SENSOR 3
#define echoPin03 4 // Echo Pin
#define trigPin03 3 // Trigger Pin

//Defines for Data-Protocoll
#define STX 2
#define ETX 3

//Variables
int maximumRange = 200;             // Maximum range needed
int minimumRange = 0;             // Minimum range needed
float duration, distance1, distance2, distance3; // Duration used to calculate distance

/*
* Setup 
* Sets Pin Modes and Serial Interface
*/
void setup() {
 //Setup UART1 (Tx -> PIN 21, Rx -> PIN 20)
 //Baudrate 9600
 Serial1.begin (9600);
 Serial.begin(9600);
 
 //Set Pin Modes
 pinMode(trigPin01, OUTPUT);
 pinMode(echoPin01, INPUT);
 pinMode(trigPin02, OUTPUT);
 pinMode(echoPin02, INPUT);
 pinMode(trigPin03, OUTPUT);
 pinMode(echoPin03, INPUT);
}

void loop() {
 //SENSOR 1

 digitalWrite(trigPin01, LOW); 
 delayMicroseconds(2); 

 digitalWrite(trigPin01, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPin01, LOW);
 duration = pulseIn(echoPin01, HIGH);
 
 //Calculate the distance (in cm) based on the speed of sound.
 distance1 = duration/58.2;

 if (distance1 >= maximumRange || distance1 <= minimumRange){
 /* Send a negative number to computer and Turn LED ON 
 to indicate "out of range" */
 distance1 = -1;
 //Serial.println("-1"); 
 }
 
 //Delay 50ms before next reading.
 delay(50);

 //SENSOR 2
 duration = 0;

 digitalWrite(trigPin02, LOW); 
 delayMicroseconds(2); 

 digitalWrite(trigPin02, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPin02, LOW);
 duration = pulseIn(echoPin02, HIGH);
 
 //Calculate the distance (in cm) based on the speed of sound.
 distance2 = duration/58.2;
 
 if (distance2 >= maximumRange || distance2 <= minimumRange){
 /* Send a negative number to computer and Turn LED ON 
 to indicate "out of range" */
 distance2 = -1;
 //Serial.println("-1");
 }
 
 //Delay 50ms before next reading.
 delay(50);
 
 
 //SENSOR 3
 duration = 0;

 digitalWrite(trigPin03, LOW); 
 delayMicroseconds(2); 

 digitalWrite(trigPin03, HIGH);
 delayMicroseconds(10); 
 
 digitalWrite(trigPin03, LOW);
 duration = pulseIn(echoPin03, HIGH);
 
 //Calculate the distance (in cm) based on the speed of sound.
 distance3 = duration/58.2;
 
 if (distance3 >= maximumRange || distance3 <= minimumRange){
 /* Send a negative number to computer and Turn LED ON 
 to indicate "out of range" */
 distance3 = -1;
 //Serial.println("-1"); 
 }
 
 //Delay 50ms before next reading.
 delay(50);
 
 //send Data over UART
 Serial1.print("\n");
 Serial1.print(distance1);
 Serial1.print(",");
 Serial1.print(distance2);
 Serial1.print(",");
 Serial1.print(distance3);
 Serial1.print("\0");
 
 Serial.print("\n");
 Serial.print(distance1);
 Serial.print(",");
 Serial.print(distance2);
 Serial.print(",");
 Serial.print(distance3);
 Serial.print("\0");
}
