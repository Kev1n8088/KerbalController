import krpc
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#brake gear light
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

#chute
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT)

#solar cargo rad
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#1 2 3
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)


conn = krpc.connect(name='controlpanel',address='192.168.0.103',rpc_port=50000,stream_port=50001)
vessel = conn.space_center.active_vessel

SeAlt = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')

con = vessel.control

staged = False
geared = False
braked = False
lighted = False

solared = False
anted = False
raded = False
chuted = False

one = False
two = False
three = False

while True:

    GPIO.output(12, con.gear)
    GPIO.output(7, con.brakes)
    GPIO.output(16, con.lights)
    GPIO.output(14, con.solar_panels)
    GPIO.output(15, con.radiators)
    GPIO.output(18, con.antennas)
    GPIO.output(8, con.parachutes)

    GPIO.output(23, con.get_action_group(1))
    GPIO.output(24, con.get_action_group(2))
    GPIO.output(25, con.get_action_group(3))
    

    if GPIO.input(26) == GPIO.LOW:
        staged = True
        
    if GPIO.input(20) == GPIO.HIGH:
        if staged == False:
            staged = True
            con.activate_next_stage()
    else:
        staged = False
    if GPIO.input(17) == GPIO.HIGH:
        con.sas = True
    else:
        con.sas = False
        
    if GPIO.input(27) == GPIO.HIGH:
        con.rcs = True
    else:
        con.rcs = False
        
    if GPIO.input(21) == GPIO.HIGH:
        con.abort = True
    else:
        con.abort = False

    if GPIO.input(6) == GPIO.HIGH:
        if geared == False:
            geared = True
            con.gear = not con.gear
    else:
        geared = False

    if GPIO.input(5) == GPIO.HIGH:
        if braked == False:
            braked = True
            con.brakes = not con.brakes
    else:
        braked = False

    if GPIO.input(13) == GPIO.HIGH:
        if lighted == False:
            lighted = True
            con.lights = not con.lights
    else:
        lighted = False

        

    if GPIO.input(2) == GPIO.HIGH:
        if solared == False:
            solared = True
            con.solar_panels = not con.solar_paneled
    else:
        solared = False

    if GPIO.input(4) == GPIO.HIGH:
        if anted == False:
            anted = True
            con.antennas = not con.antennas
    else:
        anted = False

    if GPIO.input(3) == GPIO.HIGH:
        if raded == False:
            raded = True
            con.radiators = not con.radiators
    else:
        raded = False

    if GPIO.input(11) == GPIO.HIGH:
        if chuted == False:
            chuted = True
            con.paracutes = not con.parachutes
    else:
        chuted = False


    if GPIO.input(22) == GPIO.HIGH:
        if one == False:
            one = True
            con.set_action_group(1, not con.get_action_group(1))
    else:
        one = False

    if GPIO.input(10) == GPIO.HIGH:
        if two == False:
            two = True
            con.set_action_group(2, not con.get_action_group(2))
    else:
        two = False

    if GPIO.input(9) == GPIO.HIGH:
        if three == False:
            three = True
            con.set_action_group(3, not con.get_action_group(3))
    else:
        three = False
