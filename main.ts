input.onSound(DetectedSound.Quiet, function () {
    LightOn = !(LightOn)
    if (LightOn) {
        basic.showIcon(IconNames.Fabulous)
        music.playMelody("B G A F D G E F ", 120)
        music.setVolume(40)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Meh)
    basic.showIcon(IconNames.Asleep)
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Surprised)
    music.playTone(988, music.beat(BeatFraction.Whole))
    music.setVolume(40)
    basic.showIcon(IconNames.Asleep)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showIcon(IconNames.Happy)
    basic.showIcon(IconNames.Asleep)
})
input.onGesture(Gesture.ScreenUp, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Diamond)
        basic.showIcon(IconNames.SmallDiamond)
    }
    basic.showString("Game Over")
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . . . . .
            # . # . .
            . . . . .
            # . . . #
            . # # # .
            `)
        music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
        music.setVolume(40)
        basic.showLeds(`
            . . . . .
            . . # . #
            . . . . .
            # . . . #
            . # # # .
            `)
    }
    basic.showIcon(IconNames.Asleep)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Silly)
    basic.showIcon(IconNames.Asleep)
})
let LightOn = false
basic.showIcon(IconNames.Asleep)
