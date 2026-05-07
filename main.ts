input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    danceFlag = true
})
function Driveback() {
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Reverse, 100)
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Reverse, 100)
    basic.pause(800)
}

function Turnleft() {
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Reverse, 100)
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Forward, 100)
    basic.pause(400)
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    danceFlag = false
})
function DriveForward() {
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Forward, 100)
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Forward, 100)
    basic.pause(800)
}

function Turnrigth() {
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor1, kitronik_klip_motor.MotorDirection.Forward, 100)
    kitronik_klip_motor.motorOn(kitronik_klip_motor.Motors.Motor2, kitronik_klip_motor.MotorDirection.Reverse, 100)
    basic.pause(400)
}

function Stop() {
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor1)
    kitronik_klip_motor.motorOff(kitronik_klip_motor.Motors.Motor2)
}

let danceFlag = false
danceFlag = true
basic.forever(function on_forever() {
    if (danceFlag) {
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
    } else {
        Stop()
    }
    
})
