# Pi - Ultrasonic Distance Sensor Connection
Its a basic project, demonstrating connection of Ultrasonic Distance Sensor with Raspberry Pi - 3 Model B.

## Ultrasonic Distance Sensor
Following is a picture of this sensor, easily available on Amazon:

|![UltrasonicDistanceSensor](https://github.com/sansinghsanjay/UltrasonicDistanceSensor_RPi_Connection/blob/master/images/ultrasonic_distance_sensor.jpg) |
|:--:|
| *Ultrasonic Distance Sensor* |


This sensor performs two operations to measure distance:
1. It transmits ultrasonic waves.
2. It receives these waves. 

Based on the transmitting and receiving time of ultrasonic waves, distance can be measured. Following is the audio frequency spectrum picture, which makes it clear that ultrasonic sounds are beyond the human hearing capability:

|![AudioFrequencySpectrum](https://github.com/sansinghsanjay/UltrasonicDistanceSensor_RPi_Connection/blob/master/images/AudioFrequencySpectrum.gif)|
|:--:|
| *Audio Frequency Spectrum* |

Some important features of this sensor:
1. Detection Distance: 2 to 450 cm, blind spot of 2 cm.
2. Precision: up to 0.3 cm
3. This module sends eight 40KHz square wave.

Controlling module (Raspberry Pi, in this case), triggers this module to transmit waves, upon receiving, this module will signal to Raspberry Pi by its echo pin. Since, the echo pin generates the signal of 5V and the tolerance of GPIO pin is only up to 3.3 V, so we have to use resistors, otherwise it may burn our GPIO pin.

In this entire connection, a voltage divider is created by using two resistors in series.

## Voltage Divider aka Potential Divider
Voltage Divison Rule: The voltage is divided between two series resistors in direct proportion to their resistance.
Following is the equation of Voltage Divison Rule:

|![VoltageDivisonEquation](https://github.com/sansinghsanjay/UltrasonicDistanceSensor_RPi_Connection/blob/master/images/voltage_divider_equation.jpg)|
|:--:|
| *Voltage Divison Equation* |

Purpose of Voltage Divison: A voltage divider is a small circuit which turns a large voltage into a smaller one. Using just two resistors and an input voltage, we can create an output voltage that is fraction of of the input.

|![VoltageDivisonCircuitDiagram](https://github.com/sansinghsanjay/UltrasonicDistanceSensor_RPi_Connection/blob/master/images/voltage_divider_circuit.jpg)|
|:--:|
| *Voltage Divider Circuit Diagram [Ref.](https://learn.sparkfun.com/tutorials/voltage-dividers/all)*|

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
3. Echo of Ultrasonic Sensor -> At one terminal of 300 Ohm resistor in breadboard.
4. One connection from the joint of 300 Ohms and 350 Ohms resistor in breadboard, to Pin 18 of RPi.
5. Gnd of Ultrasonice Sensor -> Horizontal short-circuit row of breadboard, another wire from the same horizontal row will go to Pin 6 of RPi.
6. One connection from the same horizontal row of breadboard (as in step 5) to the another terminal of 350 Ohms resistor.

For more details, check the image below:

|![connection_RPi_UltrasonicDistanceSensor](https://github.com/sansinghsanjay/UltrasonicDistanceSensor_RPi_Connection/blob/master/images/connections.jpg) |
|:--:|
| *Connection of Raspberry Pi with Ultrasound Distance Sensor* |

## How to run
After making all connections, as specified above, run the python script in stored in scripts directory:
```$ python script.py```

This script is developed and tested in Python - 2.7.9 in Raspberry Pi 3 Model B.
