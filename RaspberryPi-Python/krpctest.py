import math, krpc, time
conn = krpc.connect(name = "KERBALCONTROLLER_ALPHA", address = '192.168.0.31', rpc_port = 50000, stream_port = 50001)

vessel = conn.space_center.active_vessel
print(vessel.name)

srf_frame = vessel.orbit.body.reference_frame
orb_frame = vessel.orbit.body.non_rotating_reference_frame

altitude = conn.add_stream(getattr, vessel.flight(), 'surface_altitude')
asl = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')

con = vessel.control
throt = con.throttle

while True:
    print(altitude())

     
