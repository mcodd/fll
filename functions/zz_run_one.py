### FUNCTION START
def zz_run_one():
    # #start fast, arrive slow -> expo-in-out!
    gyro_straight(degrees = 750, start_power = 60, end_power = 30, easing=ExponentialEaseInOut, motor_stop_mode = brake, kp=2)
    gyro_straight(degrees = -150, start_power = 30, end_power = 25, kp=0)
    # #arm up quick, hit final position gently -> expo-in-out!
    control_attachments(start_speed=70, end_speed=70, degrees_wanted=-55, ease=ExponentialEaseInOut, motor_letter = 'F')
    # #orient the robot towards windmill T
    turn_function(degrees = -45, easing = ExponentialEaseInOut, stoptype = 'brake', startspeed = 30, endspeed = 30, turntype = 'right')

    # #move toward the windmill
    gyro_straight(degrees = 720, start_power = 100, end_power = 30, kp=0.5, easing=ExponentialEaseInOut)


    sensorR = ColorSensor ( 'C' )
    sensorL = ColorSensor ( 'D' ) 
    def hit_color_white():
        return sensorL.get_color() == 'white' and sensorR.get_color() == "white"
    turn_function(degrees=90, easing=ExponentialEaseOut, stoptype=None, startspeed=25, endspeed=25, turntype = 'both')
    #turn_function(degrees=40,stoptype='brake',startspeed=25,endspeed=25,turntype='both', also_end_if = hit_color_white)
    gyro_straight(degrees = 370, start_power = 30, end_power = 30, kp=1)
    ### this attachment can only go to about 1300 because otherwise it will break and the function will never return
    control_attachments(start_speed=80, end_speed=80, degrees_wanted=1300, motor_letter = 'E')
    control_attachments(start_speed=80, end_speed=80, degrees_wanted= -1300, motor_letter = 'E')
    control_attachments(start_speed=80, end_speed=80, degrees_wanted=1300, motor_letter = 'E')
    control_attachments(start_speed=80, end_speed=80, degrees_wanted= -1300, motor_letter = 'E')
### FUNCTION END
