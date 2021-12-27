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
