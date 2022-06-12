from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

def go_forward():
    pair.set_default_speed(100)
    pair.start()

def go_backward():
    pair.set_default_speed(-100)
    pair.start()

def pair_stop():
    pair.stop()

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
    print("Phase 1 failed...trun at {}.".format(y))
    pair.start_tank(-10, 10)
    while m.get_yaw_angle() >= deg:
        y = m.get_yaw_angle()
        print("turn at:{}".format(y))
    pair_stop()
    wait_for_seconds(0.1)
    y = m.get_yaw_angle()
    if y >= deg - kerbal_factor and y <= deg + kerbal_factor:
        print("phase 2 success: {}".format(y))
        return
    print("Phase 2 failed...turn at {}.".format(y))
    pair.start_tank(5, -5)
    while m.get_yaw_angle() <= deg:
        y = m.get_yaw_angle()
        print("turn at:{}".format(y))
    pair_stop()
    wait_for_seconds(0.1)
    y = m.get_yaw_angle()
    if y >= deg - kerbal_factor and y <= deg + kerbal_factor:
        print("phase 3 failed: {}".format(y))
        return
    print("Phase 3 failed...turn at {}.".format(y))
    print("Failure - turn ended at {}*. off by {} degress".format(y, y - deg))

def debug(level, msg):
    if DEBUG_FACTOR >= level:
        print(msg)

hub = PrimeHub()
t = Timer()
m = hub.motion_sensor
DEBUG_FACTOR = 0
# START YOUR CODE HERE - example at https://github.com/FIXME
