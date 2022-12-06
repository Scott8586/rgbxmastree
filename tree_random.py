# A little program for the PiHut 3D RGB Xmas Tree by Dave Christian
# Assumes tree library code has been setup (see https://github.com/ThePiHut/rgbxmastree#getting-started)
# Provide colours from colorzero library as parameters ie "python tree_random.py red green"

from tree import RGBXmasTree
from colorzero import Color
import random
import sys

tree = RGBXmasTree()
tree.brightness = 0.05  # Setting to > 0.6 has caused some instability on my Pi
tree[3].color = Color('gold')  # Set the star to gold
lights = []

# Get a list of colours from command line arguments (need to provide at least one!)
for i in range(1, len(sys.argv)):
    lights.append(Color(sys.argv[i]))

try:
    while True:
        id = random.randint(0,24)        
        # Don't change the star (GPIO #3)
        if (id != 3):
            tree[id].color = random.choice(lights)
            
except KeyboardInterrupt:
    tree.close()
