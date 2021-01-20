import pygame, time
from pygame import display, event


def event_processing():
    log = event.get()
    for cat in log:
        if cat.type == pygame.QUIT:
            exit()


k =pygame.image.load("kartinki/fon.jpg")


def drawing():
    window.blit(k,[0,0])
    display.flip()


pygame.init()
window = display.set_mode([500, 500])
while 1 == 1:
    event_processing()
    drawing()
    time.sleep(1 / 60)
