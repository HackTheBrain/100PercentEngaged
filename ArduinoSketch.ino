// person1 leds\
const int p1r = 13;
const int p1g = 12;
const int p1b = 11;
//person2 leds\
const int p2r = 10;
const int p2g = 9;
const int p2b = 8;
// person3 leds\
const int p3r = 7;
const int p3g = 6;
const int p3b = 5;
// group leds\
const int grr = 4;
const int grg = 3;
const int grb = 2

//uncomment this line if using a Common Anode LED\
#define COMMON_ANODE

// code for timer
int incomingByte; // a variable to read incoming serial data into\

void setup() 
{
// initialize serial communication:
Serial.begin(9600);
// initialize the LED pins as an output:
pinMode(13, OUTPUT);
pinMode(12, OUTPUT);
pinMode(11, OUTPUT);
pinMode(10, OUTPUT);
pinMode(9, OUTPUT);
pinMode(8, OUTPUT);
pinMode(7, OUTPUT);
pinMode(6, OUTPUT);
pinMode(5, OUTPUT);
pinMode(4, OUTPUT);
pinMode(3, OUTPUT);
pinMode(2, OUTPUT);
}

void loop() 
{
  (Serial.available() > 0); 
  { // read the oldest byte in the serial buffer:\
incomingByte = Serial.read();

if (incomingByte == 'a')  //person 1 is engaged\
Color1 (30, 30, 30);\}\
if (incomingByte == 'b') //person 1 is engaged\
Color1 (255, 0, 0);\}\

if (incomingByte == 'c') //person 2 is engaged\
Color2 (30, 30, 30);
}
if (incomingByte == 'd') //person 2 is engaged\
Color2 (255, 0, 0);
}

if (incomingByte == 'e') //person 3 is engaged\
(30, 30, 30);}
if (incomingByte == 'f') //person 3 is engaged\
Color1 (255, 0, 0);
}

if (incomingByte == 'g') //person g is engaged\
Color1 (30, 30, 30);
}
if (incomingByte == 'h') //person g is engaged\
Color1 (80, 0, 80);
}

} 
}

void Color1(int red, int green, int blue)\
{
#ifdef COMMON_ANODE
red = 255 - red;
green = 255 - green;
blue = 255 - blue;
#endif
analogWrite(p1r, red);
analogWrite(p1g, green);
analogWrite(p1b, blue);
}
void Color2(int red, int green, int blue)
{
#ifdef COMMON_ANODE
red = 255 - red;
green = 255 - green;
blue = 255 - blue;
#endif
analogWrite(p2r, red);
analogWrite(p2g, green);
analogWrite(p2b, blue);
}
void Color3(int red, int green, int blue)
{
#ifdef COMMON_ANODE
red = 255 - red;
green = 255 - green;
blue = 255 - blue;
#endif
analogWrite(p3r, red);
analogWrite(p3g, green);
analogWrite(p3b, blue);
}
void ColorG(int red, int green, int blue)
{
#ifdef COMMON_ANODE
red = 255 - red;
green = 255 - green;
blue = 255 - blue;
#endif
analogWrite(grr, red);
analogWrite(grg, green);
analogWrite(grb, blue);
}}
