radio.setGroup(69)
let pocatek = false
let ukonceni = false
let konec = 0
let zacatek = 0
let cas = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    pocatek = true
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    RunComp.SetLightLevel()
    music.playTone(Note.C, music.beat(500))
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    
    radio.sendNumber(3)
    pocatek = false
    ukonceni = false
    konec = 0
    zacatek = 0
    cas = 0
    basic.clearScreen()
    music.playTone(Note.C, music.beat(500))
})
RunComp.OnLightDrop(function on_light_drop() {
    
    if (pocatek == true) {
        radio.sendNumber(1)
        pocatek = false
        music.playTone(Note.D, music.beat(500))
    } else if (ukonceni == true) {
        
        ukonceni = false
        konec = control.millis()
        cas = konec - zacatek
        music.playTone(Note.C, music.beat(500))
        while (pocatek == false) {
            basic.showNumber(cas / 1000)
        }
    }
    
})
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    if (receivedNumber == 1) {
        ukonceni = true
        zacatek = control.millis()
        music.playTone(Note.C, music.beat(500))
    } else if (receivedNumber == 3) {
        pocatek = false
        ukonceni = false
        konec = 0
        zacatek = 0
        cas = 0
        basic.clearScreen()
        music.playTone(Note.C, music.beat(500))
    }
    
})
basic.forever(function on_forever() {
    console.logValue("pocatek", pocatek)
})
