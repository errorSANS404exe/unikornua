import pygame, time, pomosh
from pygame import display, event


def event_processing():
    global pushkax
    log = event.get()
    for cat in log:
        if cat.type == pygame.QUIT:
            exit()
        if cat.type == pygame.KEYDOWN:
            if cat.key == pygame.K_RIGHT:
                pushkax += 30
                if pushkax >= 400:
                    pushkax = 400
            if cat.key == pygame.K_LEFT:
                pushkax -= 30
                if pushkax <= 0:
                    pushkax = 0


def drawing():
    window.blit(k, [0, 0])
    window.blit(pushka, [pushkax, 400])
    display.flip()


pygame.init()
window = display.set_mode([500, 500])
pushkax = 200

k = pygame.image.load("kartinki/fon.jpg")
pushka = pygame.image.load("kartinki/pushka dla programmi axmeda.png")
pushka = pomosh.izmeni_kartinku(pushka, 100, 100, [255, 255, 255], 50)

while 1 == 1:
    event_processing()
    drawing()
    time.sleep(1 / 60)
