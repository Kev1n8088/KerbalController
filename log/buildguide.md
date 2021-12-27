Build Guide:

Adjust front panel files to the dimensions of the parts purchased

Cut out all wooden panels. Top uses the 2mm thick panel, while all other sides use the 5mm thick panel

Install all switches, joysticks, and displays.

Connect the red 18 gauge cable to the NO pin of the toggle switches, the safety switches, and the big button

Connect the black 18 gauge cable to the NC pin of the toggle switches and the big button, and the GND pin of the safety switches, and the - Pin of the big button LED

Connect the red 22 gauge cable to the NO pin of one of the toggle switches, and also to all the NO pins of the pushbuttons

Connect the black 22 gauge cable to the NC pin of one of the toggle switches, and also to all the NC pins of the pushbuttons and the - Pin of the pushbutton LEDs.

Solder jumper cables to the signal pin of all the switches

Solder the signal pin of the big button and the pushbuttons to the + pin of their own LED

Solder jumper cables to all the pins of the joysticks

Connect jumper cables to the pins of the slider potentiometer

Connect the GND and VCC pins of each joystick axis and slider to a different GND and VCC pin of the Arduino. This prevents interference

Connect the NC pin of one of the toggle switches to the GND pin of the raspberry pi

Connect the NO pin of one of the toggle switches to the VCC pin of the raspberry pi

Connect all other cables (should only have signal wires) to their designated pin. Potentiometer cables should go to the Arduino, and switch cables should go to the raspberry pi

Tie cables together using zip ties and tape.

Load program onto Arduino and Pi. Start Arduino program, then unplug from the computer.

Connect HDMI cable of the display to the Raspberry Pi. Connect the USB hub. Connect Arduino to the USB hub. Connect power to the display and the USB hub.

Test switch functionality.

Glue all panels in their respective positions

Tape top panel onto bottom panels, making sure all cables go where they should go.
