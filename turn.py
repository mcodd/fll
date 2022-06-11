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
    t.reset()
    m.reset_yaw_angle()
    pair.start_tank(30,-30)
    while m.get_yaw_angle() <= deg - 10:
        y = m.get_yaw_angle()
        print("turn is now at:{}".format(y))
    go_stop()
    y = m.get_yaw_angle()
    print("Phase 1 complete...   turn at {}.".format(y))
    pair.start_tank(-15, 15)
    while m.get_yaw_angle() >= deg:
        y = m.get_yaw_angle()
        print("turn_is_now_at:{}".format(y))
    pair.start_tank(7, -7)
    while m.get_yaw_angle() <= deg:
        y = m.get_yaw_angle()
        print("turn is now at:{}".format(y))
    y = m.get_yaw_angle()
    print("Done - turn ended at {}*.took {} seconds. we are off by {} degress".format(y, t.now(), y - deg))

turn(100, 3)
go_stop()
