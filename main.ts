radio.setGroup(69)
let pocatek = false
let konec = 0
let zacatek = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    pocatek = true
})
RunComp.SetLightLevel()
RunComp.OnLightDrop(function on_light_drop() {
    
    if (pocatek == true) {
        pocatek = false
        radio.sendNumber(1)
    }
    
})
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    let zacatek = control.millis()
    RunComp.OnLightDrop(function on_light_drop2() {
        let konec = control.millis()
        let cas = konec - zacatek
        console.logValue("recieved", receivedNumber)
        console.logValue("konec", konec)
        console.logValue("cas", cas)
        basic.showNumber(cas / 1000)
    })
})
