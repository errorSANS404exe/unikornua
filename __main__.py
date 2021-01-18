import pygame, time
from pygame import display, event


def event_processing():
    log = event.get()
    for cat in log:
        if cat.type == pygame.QUIT:
            exit()


pygame.init()
window = display.set_mode([500, 500])
while 1 == 1:
    event_processing()
    time.sleep(1 / 60)
