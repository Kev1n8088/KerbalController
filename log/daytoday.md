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

Pt3. Soldered all analog connections, added VCC and GND to a breadboard for easier routing. Nov 21-22:

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
