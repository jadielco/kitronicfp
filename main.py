from microbit import sleep, button_a, button_b
import kitronik_klip_motor

dance_flag = True

def drive_back():
    kitronik_klip_motor.motor_on(
        kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.REVERSE,
        100
    )
    kitronik_klip_motor.motor_on(
        kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.REVERSE,
        100
    )
    sleep(800)

def turn_left():
    kitronik_klip_motor.motor_on(
        kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.REVERSE,
        100
    )
    kitronik_klip_motor.motor_on(
        kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100
    )
    sleep(400)

def drive_forward():
    kitronik_klip_motor.motor_on(
        kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100
    )
    kitronik_klip_motor.motor_on(
        kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100
    )
    sleep(800)

def turn_right():
    kitronik_klip_motor.motor_on(
        kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100
    )
    kitronik_klip_motor.motor_on(
        kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.REVERSE,
        100
    )
    sleep(400)

def stop():
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)

while True:
    if button_a.was_pressed():
        dance_flag = True
    if button_b.was_pressed():
        dance_flag = False

    if dance_flag:
        drive_forward()
        turn_left()
        drive_back()
        turn_right()
        turn_right()
        drive_back()
        turn_right()
        drive_back()
        drive_forward()
        turn_left()
        turn_right()
        turn_right()
        turn_right()
    else:
        stop()

    sleep(10)