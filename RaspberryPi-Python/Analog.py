import serial, krpc

ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)

conn = krpc.connect(name='controlpaneljoysticks',address='169.254.1.239',rpc_port=50000,stream_port=50001)
vessel = conn.space_center.active_vessel
con = vessel.control


values = []

while True:
    if ser.in_waiting > 0:
        
        line = ser.readline().decode('utf-8').rstrip()
        if '/' in line:
            line1 = line.replace('/', '')
            values = line1.split(' ')
            con.throttle = float(values[0])
            con.roll = float(values[1])
            con.pitch = float(values[2])
            con.yaw = float(values[3])
            
            con.right = float(values[4])
            con.up = float(values[5])
            con.forward = float(values[6])
            


        
        
