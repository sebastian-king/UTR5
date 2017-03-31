import motors
import map_data
import Servo
import time


def move_pickup(distance, direction):
    if distance > 0:
        # constant for ratio of the distance per rotation, in <unit of measurement>, that a wheel travels when wheel is straight
        wheel_diameter = 60.0  # 60mm
        # number of rotations needed to travel distance when wheels are at a 45 degree angle
        num_rotations_diagonal = distance / (1.414214 * wheel_diameter * 3.1415)  # 1.414214=sqrt(2)
        # angle = num_rotations_diagonal * 360
        num_pulses = num_rotations_diagonal * 90.0  # multiply by 90, the number of phase counts per revolution of the motor

        # figure out which wheels are clockwise(1) vs counter_clockwise(0)
        if direction == map_data.RIGHT:  # right
            FL = 0
            FR = 0
            BL = 1
            BR = 1
        elif direction == map_data.UP:  # fwd
            FL = 0
            FR = 1
            BL = 0
            BR = 1
        elif direction == map_data.LEFT:  # left
            FL = 1
            FR = 1
            BL = 0
            BR = 0
        elif direction == map_data.DOWN:  # back
            FL = 1
            FR = 0
            BL = 1
            BR = 0

        #I measured the distance from cache to cache to be 12 inches
        # I measured the distance from side of robot to cach to be around 3.5 inches
        # 3.5 / 12 = 29

        speed = 29  # rpm
        motors.runMotors(num_pulses, speed, FL, FR, BL, BR)

        Servo.arm_lower
        Servo.arm_raise

        # I just flipped the 1's and 0's

        if direction == map_data.RIGHT:  # right
            FL = 1
            FR = 1
            BL = 0
            BR = 0
        elif direction == map_data.UP:  # fwd
            FL = 1
            FR = 0
            BL = 1
            BR = 0
        elif direction == map_data.LEFT:  # left
            FL = 0
            FR = 0
            BL = 1
            BR = 1
        elif direction == map_data.DOWN:  # back
            FL = 0
            FR = 1
            BL = 0
            BR = 1

        speed = 29  # rpm
        motors.runMotors(num_pulses, speed, FL, FR, BL, BR)


