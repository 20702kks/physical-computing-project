input.onButtonPressed(Button.A, function () {
    basic.showString("TURNED ON")
    OFF = 0
    ON += 1
    if (ON >= 2) {
        ON = 1
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("RESET")
    ON = 0
    OFF = 0
})
input.onButtonPressed(Button.B, function () {
    basic.showString("TURNED OFF")
    ON = 0
    OFF += 1
    if (OFF >= 2) {
        OFF = 1
    }
})
let OFF = 0
let ON = 0
OLED.init(128, 64)
ON = 0
OFF = 0
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P1) == 1 && (OFF && ON) == 0) {
        pins.digitalWritePin(DigitalPin.P2, 1)
    }
})
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P1) == 0 && (OFF && ON) == 0) {
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
})
basic.forever(function () {
    basic.pause(100)
    OLED.clear()
    if (pins.digitalReadPin(DigitalPin.P1) == 1) {
        OLED.writeString("motion detected")
    } else {
        OLED.writeString("motion not detected")
    }
})
basic.forever(function () {
    if (OFF == 1) {
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
    if (ON == 1) {
        pins.digitalWritePin(DigitalPin.P2, 1)
    }
})
