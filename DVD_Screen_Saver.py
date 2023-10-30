import random

import pygame, time, sys, random, os
import pygame.locals

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

windowSurface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

WINDOWWIDTH, WINDOWHEIGHT = windowSurface.get_size()

IMAGEWIDTH = 250

DVD_Image = pygame.image.load("DVD_Image.png").convert_alpha()
IMAGEHEIGHT = (DVD_Image.get_size()[1]/DVD_Image.get_size()[0])*IMAGEWIDTH
DVD_Image = pygame.transform.scale(DVD_Image, (IMAGEWIDTH, IMAGEHEIGHT))
DVD_Rect = DVD_Image.get_rect()
DVD_Rect.left = random.randint(0, WINDOWWIDTH - IMAGEWIDTH)
DVD_Rect.top = random.randint(0, WINDOWHEIGHT - IMAGEHEIGHT)

DVD_colors = [pygame.Color(37, 150, 190), pygame.Color(85, 206, 121), pygame.Color(255, 0, 0), pygame.Color(233, 255, 90), pygame.Color(116, 215, 255)]

MOVESPEED = 1

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

dir = UPRIGHT

pygame.mouse.set_visible(False)

def fill(surface: pygame.Surface, color: pygame.Color) -> pygame.Surface:
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color.r, color.g, color.b, color.a
    newSurface = pygame.Surface((IMAGEWIDTH, IMAGEHEIGHT)).convert_alpha()
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            newSurface.set_at((x, y), pygame.Color(r, g, b, a))
    return newSurface

DVD_surfaces = [fill(DVD_Image, i) for i in DVD_colors]

active_surface = DVD_Image

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if dir == DOWNLEFT:
        DVD_Rect.left -= MOVESPEED
        DVD_Rect.top += MOVESPEED
    if dir == DOWNRIGHT:
        DVD_Rect.left += MOVESPEED
        DVD_Rect.top += MOVESPEED
    if dir == UPLEFT:
        DVD_Rect.left -= MOVESPEED
        DVD_Rect.top -= MOVESPEED
    if dir == UPRIGHT:
        DVD_Rect.left += MOVESPEED
        DVD_Rect.top -= MOVESPEED

    if DVD_Rect.top < 0:
        if dir == UPLEFT:
            dir = DOWNLEFT
        if dir == UPRIGHT:
            dir = DOWNRIGHT
        active_surface = random.choice(DVD_surfaces)
    
    if DVD_Rect.bottom > WINDOWHEIGHT:
        if dir == DOWNLEFT:
            dir = UPLEFT
        if dir == DOWNRIGHT:
            dir = UPRIGHT
        active_surface = random.choice(DVD_surfaces)

    if DVD_Rect.left < 0:
        if dir == DOWNLEFT:
            dir = DOWNRIGHT
        if dir == UPLEFT:
            dir = UPRIGHT
        active_surface = random.choice(DVD_surfaces)

    if DVD_Rect.right > WINDOWWIDTH:
        if dir == DOWNRIGHT:
            dir = DOWNLEFT
        if dir == UPRIGHT:
            dir = UPLEFT
        active_surface = random.choice(DVD_surfaces)

    windowSurface.fill((0, 0, 0))
    windowSurface.blit(active_surface, DVD_Rect)
    pygame.display.update()
    time.sleep(0.016)

