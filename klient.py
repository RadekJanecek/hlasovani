radio.set_group(1)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)
pismeno = 65
start = 0
basic.show_string(String.from_char_code(pismeno), 0)

def on_button_pressed_a():
    global pismeno
    if pismeno == 65:
        pismeno = 90
    else:
        pismeno -= 1
    basic.show_string(String.from_char_code(pismeno), 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global pismeno
    if pismeno == 90:
        pismeno = 65
    else:
        pismeno += 1
    basic.show_string(String.from_char_code(pismeno), 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global start
    if name == "start":#name start přijímá zda může či nemůže klient hlasovat
        if value == 0:
            basic.show_icon(IconNames.NO)
            start = 0
        else:
            basic.show_icon(IconNames.YES)
            start = 1
radio.on_received_value(on_received_value)

def on_logo_event_pressed():
    if start:
        radio.send_value("hlas", pismeno - 64)#name hlas posílá písmeno
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)
