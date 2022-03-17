radio.set_group(69)
pocatek=False
ukonceni=False
konec=0
zacatek=0
cas=0

def on_button_pressed_a():
    global pocatek
    pocatek=True
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    RunComp.set_light_level() 
    music.play_tone(Note.C, music.beat(500))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_event_pressed():
    global pocatek, ukonceni, konec, zacatek, cas
    radio.send_number(3)
    pocatek=False
    ukonceni=False
    konec=0
    zacatek=0
    cas=0
    basic.clear_screen()
    music.play_tone(Note.C, music.beat(500))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def on_light_drop():
    global pocatek, ukonceni
    if pocatek==True:
        radio.send_number(1)
        pocatek=False
        music.play_tone(Note.D, music.beat(500))
    elif ukonceni==True:
        global konec, cas, zacatek, ukonceni
        ukonceni=False
        konec=control.millis()
        cas=konec-zacatek
        music.play_tone(Note.C, music.beat(500))
        while pocatek==False:
            basic.show_number(cas/1000)
RunComp.on_light_drop(on_light_drop)

def on_received_number(receivedNumber):

    global zacatek, ukonceni, konec, cas, pocatek
    if receivedNumber==1:
        ukonceni=True
        zacatek=control.millis()
        music.play_tone(Note.C, music.beat(500))
       
    elif receivedNumber==3:
        pocatek=False
        ukonceni=False
        konec=0
        zacatek=0
        cas=0
        basic.clear_screen()
        music.play_tone(Note.C, music.beat(500))
radio.on_received_number(on_received_number)

def on_forever():
    console.log_value("pocatek", pocatek)
basic.forever(on_forever)
