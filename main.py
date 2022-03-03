radio.set_group(69)
pocatek=False
konec=0
vypinac=False
def on_button_pressed_a():
    global pocatek, vypinac
    pocatek=True
    vypinac=False
input.on_button_pressed(Button.A, on_button_pressed_a)
RunComp.set_light_level()
def on_light_drop():
    global konec, pocatek
    if pocatek==True:
        zacatek=control.millis()
        radio.send_number(zacatek)
        pocatek=False
    elif pocatek==False:
        konec=control.millis()
        pocatek=True
        vypinac=True
RunComp.on_light_drop(on_light_drop)

 
def on_received_number(receivedNumber):
    global konec, vypinac
    if vypinac==True:
        cas=receivedNumber-konec
        basic.show_string("Hello!")
radio.on_received_number(on_received_number)

