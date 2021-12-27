**Abstract:**

The goal is to create a controller that can be used to play a space game/simulation known as Kerbal Space Program. This particular plan details the third iteration of the project.

Significant differences from previous iterations include the switch from Arduino to Raspberry Pi as the processor (although we do still have an Arduino for Analog Input), the inclusion of a configurable 13 inch 1080P touchscreen, and the relatively large size of the controller. The software integration of the touchscreen is still under development.

We use a plugin to the game called KRPC. Originally designed to allow external programs to control the game via various different scripts, we used it’s networking features to allow the controller to wirelessly connect to the game via LAN. The digital buttons are directly connected to the RPI, while the analog throttle and joysticks are connected via an Arduino that interprets the signals and relays it to the RPI via serial link, as the RPI does not have analog inputs. To lower latency, the digital and analog scripts on the RPI are two different programs that are connected to the same game, another feature of KRPC. An external USB hub allows the connection of a keyboard and mouse, and the touchscreen allows for debugging without opening up the controller.
