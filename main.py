def on_button_pressed_a():
    global danceFlag
    danceFlag = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def Driveback():
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.REVERSE,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.REVERSE,
        100)
    basic.pause(800)
def Turnleft():
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.REVERSE,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    basic.pause(400)

def on_button_pressed_b():
    global danceFlag
    danceFlag = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def DriveForward():
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    basic.pause(800)
def Turnrigth():
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR1,
        kitronik_klip_motor.MotorDirection.FORWARD,
        100)
    kitronik_klip_motor.motor_on(kitronik_klip_motor.Motors.MOTOR2,
        kitronik_klip_motor.MotorDirection.REVERSE,
        100)
    basic.pause(400)
def Stop():
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR1)
    kitronik_klip_motor.motor_off(kitronik_klip_motor.Motors.MOTOR2)
danceFlag = False
danceFlag = False

def on_forever():
    if danceFlag:
        DriveForward()
        Turnleft()
        Driveback()
        Turnrigth()
        Turnrigth()
        Driveback()
        Turnrigth()
        Driveback()
        DriveForward()
        Turnleft()
        Turnrigth()
        Turnrigth()
        Turnrigth()
    else:
        Stop()
basic.forever(on_forever)
