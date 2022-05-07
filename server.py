radio.set_group(1)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)
serial_list = [0]
odpovedi = [0]
start = 0


def on_button_pressed_ab():
    for i in range(65, 91):
        print(String.from_char_code(i) + (odpovedi.count(i)))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global serial_list, odpovedi
    serial_list = [0]
    odpovedi = [0]
input.on_button_pressed(Button.B, on_button_pressed_b)



def on_button_pressed_a():
    global start
    if start == 1:
        start = 0
        basic.show_icon(IconNames.NO, 0)
    else:
        start = 1
        basic.show_icon(IconNames.YES, 0)
    radio.send_value("start", start)#name start posílá zda může klient hlasovat nebo ne
input.on_button_pressed(Button.A, on_button_pressed_a)



def on_received_value(name, value):
    if name == "hlas":#name hlas přijímá hlasované písmeno
        serial1 = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        if serial1 in serial_list:
            list_index = serial_list.index(serial1)
            odpovedi[list_index] = value + 64
        else:
            serial_list.append(serial1)
            odpovedi.append(value + 64)
        print(String.from_char_code(value + 64) + " od " + serial1)
        music.play_tone(Note.C, 300)
radio.on_received_value(on_received_value)
