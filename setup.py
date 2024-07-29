from terminaltexteffects.effects.effect_expand import Expand
from terminaltexteffects.utils.graphics import Color, Gradient
import time
import os

def logo():
    effect = Expand("""
        ████████████████████████████████
        █─▄▄▄▄█▄─▄▄─█─▄─▄─█▄─██─▄█▄─▄▄─█
        █▄▄▄▄─██─▄█▀███─████─██─███─▄▄▄█
        ▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▀▀
    """)
    effect.effect_config.final_gradient_direction = Gradient.Direction.HORIZONTAL
    effect.effect_config.final_gradient_stops = (Color("55e6d7"), Color("5577e6"))
    effect.effect_config.final_gradient_steps = 60


    with effect.terminal_output() as terminal:

        for frame in effect:

            terminal.print(frame)      

from terminaltexteffects.effects.effect_beams import Beams

def logo2():

    effect = Beams("""
    This program is distributed by Ubub0x,
     protected by the Apache 2.0 license.
          Therefore any illegal use,
         it is completely prohibited!
    """)

    effect.effect_config.final_gradient_direction = Gradient.Direction.HORIZONTAL
    effect.effect_config.final_gradient_stops = (Color("55e6d7"), Color("5577e6"))
    effect.effect_config.final_gradient_steps = 60


    with effect.terminal_output() as terminal:

        for frame in effect:

            terminal.print(frame)

def loading():

    effect = Beams("Loadinig...")

    effect.effect_config.final_gradient_direction = Gradient.Direction.HORIZONTAL
    effect.effect_config.final_gradient_stops = (Color("55e6d7"), Color("5577e6"))
    effect.effect_config.final_gradient_steps = 60


    with effect.terminal_output() as terminal:

        for frame in effect:

            terminal.print(frame)            

           
def clear():
    if os.name == 'nt': 
        os.system('cls')
    else:  
        os.system('clear')

if __name__ == "__main__":
    clear()
    logo()
    time.sleep(1)
    logo2()
    clear()
    loading()
    time.sleep(2)
    clear()
    loading()
    time.sleep(2)
    clear()
    loading()
    time.sleep(2)
    clear()
    os.system("python main.py")