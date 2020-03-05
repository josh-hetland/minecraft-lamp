#!/usr/bin/env python
import unicornhat as ore
import time

ore.set_layout(ore.AUTO)
ore.rotation(0)
ore.brightness(1.0)

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
ore.clear()

for color in colors:
    ore.set_all(color)
    ore.show()
    time.sleep(10)

