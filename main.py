def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)

def on_forever():
    pass
basic.forever(on_forever)
