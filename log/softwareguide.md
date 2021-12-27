Kerbal Controller Software Guide

Raspberry Pi:

Switch Program: We first set the input and output. Then, for toggle switches, we simply set the variable we are controlling in KRPC to equal the output of the toggle switches. For the push buttons, it’s a bit more complicated. We flip the value of the variable, but in order to make sure that we don’t flip it over and over due to a prolonged press, we have an internal variable that stores whether the button has been pressed. This variable is reset when the button is released, and only if the variable is false do we switch the value. The LEDs are simply driven by the state of the various values they are connected to.

Analog Program: We read the message sent by the Arduino, and then map that value to a number between -1 and 1. We then use that number to set the value of the respective controls.

Arduino:

The Arduino simply sends analog data from the joysticks via a serial link to the raspberry pi, adjusting some values to account for noise. Nothing special here.
