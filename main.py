radio.set_group(69)
pocatek=False
konec=0
zacatek=0
RunComp.set_light_level()
def on_button_pressed_a():
    global pocatek
    pocatek=True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_light_drop():
    global pocatek
    if pocatek==True:
        radio.send_number(1)
        pocatek=False
RunComp.on_light_drop(on_light_drop)

def on_received_number(receivedNumber):
    zacatek=control.millis()
    def on_light_drop2():
        konec=control.millis()
        cas=konec-zacatek
        console.log_value("recieved", receivedNumber)
        console.log_value("konec", konec)
        console.log_value("cas", cas)
        while pocatek==False:
            basic.show_number(cas/1000)
    RunComp.on_light_drop(on_light_drop2)
radio.on_received_number(on_received_number)

def onIn_background():
    def on_forever():
        console.log_value("pocatek", pocatek)
    basic.forever(on_forever)
control.in_background(onIn_background)
