# fractal.py
# This program creates two different fractal drawings:
#
# 1. Sierpinski's Carpet
# 2. Koch's Snowflake

import picture
from bubbles import call_bubbles
from carpet import call_carpet
from snow_flakes import call_snow_flakes
# Displaying images
print(""" 
Welcome to Fractal Images!
    CHOOSE A FRACTAL IMAGE OF YOUR CHOICE
      1. BUBBLES
      2. CARPET
      3. SNOW FLAKES
    """)

error = 0
while error != 1:
    try:
        choice = int((input(": ")))
        if choice not in [1, 2, 3]:
            choice/0
    except Exception:
        print("Please choose between the choices above(1,2,3)")
    else:
        error = 1
data = {1:"BUBBLES", 2:"CARPET",3:"SNOW FLAKES"}
# Canvas Size
print(f"You choice { data[choice]}")
size = int(input(f"Canvas size for {data[choice]}: "))
depth = int(input(f"Depth for {data[choice]}: "))
if choice == 1 :
    call_bubbles(size,depth)
if choice == 2:
    call_carpet(size,depth)
if choice == 3:
    call_snow_flakes(size,depth)




