#!/usr/bin/env python
import unicornhat as ore
import time
import signal
import buttonshim


@buttonshim.on_press(buttonshim.BUTTON_B)
def button_a(button, pressed):
    global current_index
    current_index = current_index + 1
    print(" Button press detected [{}][{}]".format(current_index,len(colors)))
    if current_index >= len(colors):
        #print(" end reached, reset to off")
        current_index = -1

    if current_index == -1:
        #print("  off")
        ore.off()
    else:
        #print("  selecting color for display")
        current_color = colors[current_index]
        ore.set_all(current_color)
        ore.show()


print "Starting Minecraft Ore Lamp - Button Mode"
ore.set_layout(ore.AUTO)
ore.rotation(0)
ore.brightness(0.4)

DIAMOND = (69, 172, 165)
GOLD = (254, 254, 63)
REDSTONE = (170, 0, 0 )
EMERALD = (85, 255, 85)
LAVA = (255, 170,0)
LAPIS_LAZUL = (0, 0, 190)
IRON = (217, 163,52)

colors = [
    DIAMOND, # diamond
    GOLD,  # gold
    REDSTONE  , # redstone
    EMERALD , # emerald
    LAVA  , # lava
    LAPIS_LAZUL  , # lapis lazul
    IRON  # iron   
] 

current_index = -1

ore.clear()
signal.pause()

ore.off()

