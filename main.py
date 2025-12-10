def on_button_pressed_a():
    global OFF, ON
    basic.show_string("TURNED ON")
    OFF = 0
    ON += 1
    if ON >= 2:
        ON = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global ON, OFF
    basic.show_string("RESET")
    ON = 0
    OFF = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global ON, OFF
    basic.show_string("TURNED OFF")
    ON = 0
    OFF += 1
    if OFF >= 2:
        OFF = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

OFF = 0
ON = 0
OLED.init(128, 64)
ON = 0
OFF = 0

def on_forever():
    if pins.digital_read_pin(DigitalPin.P1) == 1 and (OFF and ON) == 0:
        pins.digital_write_pin(DigitalPin.P2, 1)
basic.forever(on_forever)

def on_forever2():
    if pins.digital_read_pin(DigitalPin.P1) == 0 and (OFF and ON) == 0:
        pins.digital_write_pin(DigitalPin.P2, 0)
basic.forever(on_forever2)

def on_forever3():
    basic.pause(100)
    OLED.clear()
    if pins.digital_read_pin(DigitalPin.P1) == 1:
        OLED.write_string("motion detected")
    else:
        OLED.write_string("motion not detected")
basic.forever(on_forever3)

def on_forever4():
    if OFF == 1:
        pins.digital_write_pin(DigitalPin.P2, 0)
    if ON == 1:
        pins.digital_write_pin(DigitalPin.P2, 1)
basic.forever(on_forever4)
