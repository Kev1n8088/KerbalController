Kerbal Controller Project Log

Abstract:

The goal is to create a controller that can be used to play a space game/simulation known as Kerbal Space Program. This particular plan details the third iteration of the project. 

Significant differences from previous iterations include the switch from Arduino to Raspberry Pi as the processor (although we do still have an Arduino for Analog Input), the inclusion of a configurable 13 inch 1080P touchscreen, and the relatively large size of the controller. The software integration of the touchscreen is still under development. 

We use a plugin to the game called KRPC. Originally designed to allow external programs to control the game via various different scripts, we used it’s networking features to allow the controller to wirelessly connect to the game via LAN. The digital buttons are directly connected to the RPI, while the analog throttle and joysticks are connected via an Arduino that interprets the signals and relays it to the RPI via serial link, as the RPI does not have analog inputs. To lower latency, the digital and analog scripts on the RPI are two different programs that are connected to the same game, another feature of KRPC. An external USB hub allows the connection of a keyboard and mouse, and the touchscreen allows for debugging without opening up the controller. 



Day to Day Log


Nov 14 (2020):

Pt1. Reobtained items, convened with a Python tutor about UI design. Turns out the UI software that we were planning on using doesn’t work, so we decided to use PyGame, a simple but capable UI design library.

Pt2. Reviewed old solder work, and tested switch connections. Realized that our soldering was wrong because of the possibility of shorting when pulling down switches, and we were forced to rewired the entire GND wire network.


Nov 15: 

Pt1. Finished wiring digital switches and did preliminary testing on switches. Due to some power issues, some switches failed. Reconfigured it, and switches worked. Applied hot glue to small switch connections to prevent shorting.
	
Pt2. Did preliminary testing on connection with KSP. Downlink is perfect, uplink shows promise.


Nov 16-Nov 18:

Did KSP uplink testing. Adjusted and is now mostly perfect. Stage, abort, arm, RCS, and SAS now working. RCS switch is intermittent, doing testing to find the problem. 


Nov 19:

Pt1. RCS switch’s VCC connection broke, resoldered, and applied hot glue to all connections. Shouldn’t break anymore.

Pt2. Tested analog throttle and joystick connections with Arduino. Throttle and the two Pitch and Yaws are nominal, but the roll is odd. Did testing, mapped out the pattern. 0 is 40, -1 is 0, +1 is 400. Programmed adaptation into Arduino. 

Pt3. Soldered all analog connections, added VCC and GND to a breadboard for easier routing.
Nov 21-22:

Pt1. Research on comms between Arduino and RPI yield some results. The easiest way seems to be either I2C or Serial.

Pt2. Serial over USB seems the most viable, due to it not requiring and GPIO ports and is the simplest for 2-way comms.
	
	
Nov 24:
	
Pt1. Was able to finish programming most switches on the RPI, but due to the lack of a computer at this moment, I was not able to get a comms protocol started, as I am unable to program an Arduino with just an RPI


Nov 28:
	
Pt1: Was able to troubleshoot the comms protocol, the issue is the delay between the input and the output in the game. 
	
Pt2: Counterintuitively, by slowing down the output from the Arduino, it allowed the RPI to catch up. A good middle ground seems to be 200ms. Currently, 3 axes and the throttle are connected. 
	
Pt3: Oddly, there doesn’t seem to be enough power to supply the joysticks, they are showing erratic results when many axes are connected together. I have Connected each axis to a separate power and ground pin on the Arduino. That seems to have fixed the problem. Still unsure why this is, it could have been caused by the low throughput of an individual breadboard strip. 


Nov 29:
	
Pt1: Connected 3 other axes. Lag is back. Adjusted delay to be 400ms. Fixed the issue
	
Pt2: Connected all wires for all buttons, now need programming.


Dec 5: 
	
Pt1: Finished connections and programming for ALL switches. All confirmed to be working. A slight change in the switch layout was made due to personal preference.
	
Pt2: UI complete, all connected to KRPC module. Software and switches officially finished. Need to order wood boards to finish enclosure.


Dec 6:
	
Pt1: Ordered wood boards. 60 yuan each, for a total of 180 yuan. Awaiting delivery


Dec 9:
	
Pt1: Wood boards arrived. In pristine condition.


Dec 12:
	
Pt1: Planned to go to the workshop, due to short notice Lee is unavailable.


Dec 13: 
	
Pt1: Forgot wood boards, remembered halfway to the workshop. OOOOOOPS
	
Pt2: Cables are “managed” with the use of duct tape and zip ties to secure connections and bundle the cables together. 
	
Pt3: To accommodate for the UI of the display and the Raspberry Pi, the right side needs to be modified. A 110mm x 30mm rectangular hole is designed into the top side of the board for the display UI, and an 80mm x 30mm is designed into the bottom side of the board for the Raspberry Pi UI. Due to the size of the top board, an internal support brace is needed. A copy of the left side is created, and 2 30mm x 30mm holes are designed into the top side of the board for cable routing.
	
Pt4: Everything is cut out. More than enough material. The 1st cut is perfect, no need for recutting. Used glue gun to secure the bottom, back, front, left, right, and internal supports. Securely fixed.
	
Pt5: Everything is placed in their respective positions. We needed a USB hub, so Lee ran and grabbed one from the local electronics shop. 50 yuan. The top is taped down for easy maintenance. 
	
Pt6: Arrived home, opened top. 2 cables that were under tension have been dislodged. Connected extension cable to relieve stress. Also connected Arduino to the USB hub instead of directly to the RPI for easy access.



Kerbal Controller Build Guide


Parts List: 

Raspberry PI 3B+ with enclosure, cooling fan, and power cable

Arduino Mega with USB cable

Big button with LED

10x SPDT (Single pole double throw) pushbuttons with LED

2x SPDT (Single pole double throw) toggle switches

2x SPST (Single pole single throw) Safety switches with LED

10K Ω sliding potentiometer

2x 3 axis 10K Ω joystick style potentiometer

13-inch 1080p touchscreen display with HDMI and power cables

Breadboard

Assorted screws, nuts, and spacers (M1, M2, and M3)

Assorted Male to Female jumper cables

1 meter of 18 gauge red and black cables 

2 meters of 22 gauge red and black cables
 USB hub

800mm x 800mm of 2mm thick laser cutter grade plywood panel

2x 800 x 800 mm of 5mm thick laser cutter grade plywood panel

Cellar tape or duct tape 

Zip ties
	
Total: ~1400 Yuan


Tools List:

Multimeter

Soldering Iron + Soldering Kit

Glue gun + Glue sticks

Screwdriver

Laser cutter

Computer


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



Kerbal Controller Software Guide


Raspberry Pi: 
	
Switch Program: We first set the input and output. Then, for toggle switches, we simply set the variable we are controlling in KRPC to equal the output of the toggle switches. For the push buttons, it’s a bit more complicated. We flip the value of the variable, but in order to make sure that we don’t flip it over and over due to a prolonged press, we have an internal variable that stores whether the button has been pressed. This variable is reset when the button is released, and only if the variable is false do we switch the value. The LEDs are simply driven by the state of the various values they are connected to.

Analog Program: We read the message sent by the Arduino, and then map that value to a number between -1 and 1. We then use that number to set the value of the respective controls. 


Arduino: 
	
The Arduino simply sends analog data from the joysticks via a serial link to the raspberry pi, adjusting some values to account for noise. Nothing special here. 



Kerbal Controller: Issues


Hardware: 

Raspberry Pi doesn’t have analog inputs. Solution: Used Arduino to act as a ADC

Joystick roll axis is acting strange and gives out odd but consistent results. Solution: Used software to map it to the desired value

Joystick appears to consume too much power for a single strip on the breadboard. Solution: Switched all axes to individual power pins on the Arduino

Top panel sags when supported on 4 sides. Solution: Internal support panel with cable routing gaps fabricated

High stress on Throttle signal cable. Solution: Added extension cable

No extra mouse and keyboard available, as I would need to seal up the Raspberry Pi. Solution: Bought a USB hub to route the cables outside


Software: 

Have to communicate with an Arduino from a Raspberry Pi. Solution: Used Serial link

Takes too long for Raspberry Pi to communicate with KSP. Solution: Increased delay between Arduino and Raspberry Pi

Kerbal Controller: Summary

After 3 years of development and 3 iterations, covering 7 versions of KSP, the Kerbal Controller is finally completed. This iteration of the controller uses KRPC, a python plugin for KSP, to remotely control the game via a Raspberry Pi, instead of using the slow and unreliable KSPSerialIO which uses a serial link from an Arduino. Digital signals from switches are directly handled by the Pi, while analog signals are handled by an Arduino Mega connected to the Pi via serial link. The Raspberry Pi can run multiple clients at once, allowing rapid communication between the game and the control panel. 3 clients are used: One for a digital uplink, one for an analog uplink, and one for a telemetry downlink. The result is a reliable and low-latency system that is infinitely expandable and customizable. Development on this project is certainly not stopping here, with autopilot, map visualization, and more in the works. 
