from pygame import *
from random import *
from pprint import *

screen = display.set_mode((1000,1000))

running = True
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False

    display.flip()

quit()
