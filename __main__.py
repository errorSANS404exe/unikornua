import pygame, time, pomosh
from pygame import display, event, draw


def event_processing():
    log = event.get()
    for cat in log:
        if cat.type == pygame.QUIT:
            exit()
        if cat.type == pygame.KEYDOWN:
            if cat.key == pygame.K_RIGHT:
                rect.right += 30
                if rect.right >= 500:
                    rect.right = 500
            if cat.key == pygame.K_LEFT:
                rect.left -= 30
                if rect.left <= 0:
                    rect.left = 0


def drawing():
    window.blit(k, [0, 0])
    window.blit(pushka, rect)
    draw.rect(window, [255, 0, 0], rect, 2)
    risui_karik()
    display.flip()


def risui_karik():
    draw.rect(window, [255, 0, 0], karik)


def dvigai_karik():
    global karik, karik_speedy, karik_speedx
    karik.bottom += karik_speedy
    karik_speedy += (10 / 60) * 0.16  # ускоряем шарик вниз
    if karik.bottom >= 500:
        karik_speedy = -karik_speedy * 0.8
        karik.bottom = 500
    karik.right += karik_speedx  # двигаем шарик вправо и влево
    if karik.right >= 500:
        karik.right = 500
        karik_speedx = -karik_speedx
    if karik.left <= 0:
        karik.left = 0
        karik_speedx = -karik_speedx


pygame.init()
window = display.set_mode([500, 500])
pushkax = 200
rect = pygame.Rect(0, 400, 100, 100)
rect.centerx = 250
karik = pygame.Rect(30, 40, 30, 30)
karik_speedy = 0
karik_speedx = 1

# AXMED.EXE starting

k = pygame.image.load("kartinki/fon.jpg")
pushka = pygame.image.load("kartinki/pushka dla programmi axmeda.png")
pushka = pomosh.izmeni_kartinku(pushka, 100, 100, [255, 255, 255], 50)
# pushka = pomosh.izmeni_kartinku(pushka, 100, 100, [0, 255, 255], 50)

while 1 == 1:
    event_processing()
    dvigai_karik()
    drawing()
    time.sleep(1 / 100)
