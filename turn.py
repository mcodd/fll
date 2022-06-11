from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
right = Motor('A')
left = Motor('B')
sound = App()

t = Timer()
m = hub.motion_sensor
pair = MotorPair('A', 'B')

def go_forward():
    pair.set_default_speed(100)
    pair.start()

def go_backward():
    pair.set_default_speed(-100)
    pair.start()

def go_stop():
    pair.stop()
    right.stop()
    left.stop()

def speed(speed):
    pair.set_default_speed(speed)

def turn(deg, kerbal_factor = 3):
    m.reset_yaw_angle()
    pair.start_tank(30,-30)
    while m.get_yaw_angle() <= deg - 5:
        y = m.get_yaw_angle()
        print("turn is now at:{}".format(y))
    go_stop()
    wait_for_seconds(0.1)
    y = m.get_yaw_angle()
    if y >= deg - kerbal_factor and y <= deg + kerbal_factor:
        print("phase 1 success: {}".format(y))
        return 
    print("Phase 1 complete...   turn at {}.".format(y))
    pair.start_tank(-10, 10)
    while m.get_yaw_angle() >= deg:
        y = m.get_yaw_angle()
        print("turn_is_now_at:{}".format(y))
    go_stop()
    wait_for_seconds(0.1)
    y = m.get_yaw_angle()
    if y >= deg - kerbal_factor and y <= deg + kerbal_factor:
        print("phase 2 success: {}".format(y))
        return
    print("Phase 2 complete...turn at {}.".format(y))
    pair.start_tank(5, -5)
    while m.get_yaw_angle() <= deg:
        y = m.get_yaw_angle()
        print("turn is now at:{}".format(y))
    y = m.get_yaw_angle()
    if y >= deg - kerbal_factor and y <= deg + kerbal_factor:
        print("phase 2 success: {}".format(y))
        return
    print("Phase 2 complete...turn at {}.".format(y))
    print("Done - turn ended at {}*. we are off by {} degress".format(y, y - deg))

t.reset()
turn(100, 4)
print("took {} seconds".format(t.now()))
go_stop()
