import pygame, time, pomosh
from pygame import display, event


def event_processing():
    log = event.get()
    for cat in log:
        if cat.type == pygame.QUIT:
            exit()
        if cat.type==pygame.KEYDOWN:
            if cat.key==pygame.K_RIGHT:
                print("vpravo")
            if cat.key==pygame.K_LEFT:
                print("vlevo")


def drawing():
    window.blit(k, [0, 0])
    window.blit(pushka, [200,400])
    display.flip()


pygame.init()
window = display.set_mode([500, 500])

k = pygame.image.load("kartinki/fon.jpg")
pushka = pygame.image.load("kartinki/pushka dla programmi axmeda.png")
pushka = pomosh.izmeni_kartinku(pushka, 100, 100, [255, 255, 255], 50)

while 1 == 1:
    event_processing()
    drawing()
    time.sleep(1 / 60)
