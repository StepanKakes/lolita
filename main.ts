radio.setGroup(69)
let pocatek = false
let konec = 0
let vypinac = false
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    pocatek = true
    vypinac = false
})
RunComp.SetLightLevel()
RunComp.OnLightDrop(function on_light_drop() {
    let zacatek: number;
    let vypinac: boolean;
    
    if (pocatek == true) {
        zacatek = control.millis()
        radio.sendNumber(zacatek)
        pocatek = false
    } else if (pocatek == false) {
        konec = control.millis()
        pocatek = true
        vypinac = true
    }
    
})
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    let cas: number;
    
    if (vypinac == true) {
        cas = receivedNumber - konec
        basic.showString("Hello!")
    }
    
})
