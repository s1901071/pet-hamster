def on_sound_quiet():
    global LightOn
    LightOn = not (LightOn)
    if LightOn:
        basic.show_icon(IconNames.FABULOUS)
        music.play_melody("B G A F D G E F ", 120)
        music.set_volume(40)
    else:
        basic.show_icon(IconNames.ASLEEP)
input.on_sound(DetectedSound.QUIET, on_sound_quiet)

def on_button_pressed_a():
    basic.show_icon(IconNames.MEH)
    basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_icon(IconNames.SURPRISED)
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
    music.set_volume(40)
    basic.show_icon(IconNames.ASLEEP)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_icon(IconNames.HAPPY)
    basic.show_icon(IconNames.ASLEEP)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_gesture_screen_up():
    for index in range(4):
        basic.show_icon(IconNames.DIAMOND)
        basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_string("Game Over")
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_button_pressed_ab():
    for index2 in range(4):
        basic.show_leds("""
            . . . . .
                        # . # . .
                        . . . . .
                        # . . . #
                        . # # # .
        """)
        music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
        music.set_volume(40)
        basic.show_leds("""
            . . . . .
                        . . # . #
                        . . . . .
                        # . . . #
                        . # # # .
        """)
    basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.SILLY)
    basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.B, on_button_pressed_b)

LightOn = False
basic.show_icon(IconNames.ASLEEP)