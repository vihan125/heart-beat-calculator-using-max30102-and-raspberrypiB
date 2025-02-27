## heart-beat-calculator-using-max30102-and-raspberrypiB<br/>
a simple heart beat calculator using raspberrypi B model and max30102 sensor.<br/>
# Files
Includes max30102.py file which set ups the sensor and I took it from (https://github.com/vrano714/max30102-tutorial-raspberrypi).<br/>
It had some issues and I corrected them.<br/>
Includes a heart_beat_calc.py file which calculates the heart beat.<br/>
main file is heart.py which combines supporting files.<br/>
This code will  take some time to get a reading because I follwed a method of taking mean from several readings.<br/>
since this sensor is very sensitive you have to keep your finger steady while taking readings.<br/>
# Connecting sensor to the raspberry pi :<br/>
|Pins in raspberrypi | pins in sensor max30102|
|--------------------|-------------------------|
|3.3v (pin 1)  | VIN/n| 
|GPIO2 (pin3)  | SDA /n|
|GPIO3 (pin5)  | SCL|
|GPIO4 (pin7)  | INT|
|GND   (pin6)  | IRD|
|GND   (pin9)  | GND|
|_| RD pin no connection|
# Executing the files<br/>
import heart<br/>
heart.heart_beat()
