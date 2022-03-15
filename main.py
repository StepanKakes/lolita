radio.set_group(69)
pocatek=False
konec=0
zacatek=0
def on_button_pressed_a():
    global pocatek
    pocatek=True
input.on_button_pressed(Button.A, on_button_pressed_a)
RunComp.set_light_level()
def on_light_drop():
    global pocatek
    if pocatek==True:
        pocatek=False
        radio.send_number(1)
RunComp.on_light_drop(on_light_drop)

def on_received_number(receivedNumber):
    zacatek=control.millis()
    def on_light_drop2():
        konec=control.millis()
        cas=konec-zacatek
        console.log_value("recieved", receivedNumber)
        console.log_value("konec", konec)
        console.log_value("cas", cas)
        basic.show_number(cas/1000)
    RunComp.on_light_drop(on_light_drop2)
radio.on_received_number(on_received_number)

