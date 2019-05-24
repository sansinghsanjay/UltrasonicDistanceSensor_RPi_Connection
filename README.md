# Raspberry Pi - Ultrasonic Distance Sensor Connection
Its a basic project, demonstrating connection of Ultrasonic Distance Sensor with Raspberry Pi - 3 Model B.

## Ultrasonic Distance Sensor
Following is a picture of this sensor, easily available on Amazon:

[PICTURE LINK]

This sensor performs two operations to measure distance:
1. It transmits ultrasonic waves.
2. It receives these waves. 

Based on the transmitting and receiving time of ultrasonic waves, distance can be measured.

Some important features of this sensor:
1. Detection Distance: 2 to 450 cm, blind spot of 2 cm.
2. Precision: up to 0.3 cm
3. This module sends eight 40KHz square wave.

Controlling module (Raspberry Pi, in this case), triggers this module to transmit waves, upon receiving, this module will signal to Raspberry Pi by its echo pin. Since, the echo pin generates the signal of 5V and the tolerance of GPIO pin is only 3.5 V, so we have to use few resistors, otherwise it may burn our GPIO pin.

In this entire connection, voltage divider is created by using resistors.

## Voltage Divider

## Required Items
Following are the required items:
1. Raspberry Pi 3 Model B is used in this project. Most of the advanced models of Raspberry Pi will work with it, but it is suggested to do a compatibility study.
2. Jumping cables: Connections are slightly complicated, so too many jumping cables (female to female, male to female) are required.
3. Breadboard: As it requires too many connections, so breadboard is also required.
4. Resistor: In this project, it is recommended to use 330 Ohm and 470 Ohm resistors, but because of unavailability of resistors, I have used two 150 Ohms resistor (forming 300 Ohms), and one 150 Ohms and two 100 Ohms resistor (forming 350 Ohms).

## Connections
Ultrasonic Distance Sensor has four pins, and following is the connections of these pins:
1. VCC of Ultrasonic Sensor -> Pin 2 of RPi
2. Trig of Ultrasonic Sensor -> Pin 12 of RPi
3. Echo of Ultrasonic Sensor -> At one terminal of 300 Ohm resistor in breadboard
4. Gnd of Ultrasonice Sensor -> Pin 6 of RPi
5. For rest of the details, check the below picture:

[CONNECTION PICTURE]
