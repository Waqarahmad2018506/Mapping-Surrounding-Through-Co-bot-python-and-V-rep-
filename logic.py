# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 21:22:48 2022

@author: Pc
"""

import pygame
from time import sleep

pygame.init()

win = pygame.display.set_mode((100,100))

while True:
    for eve in pygame.event.get():pass
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        print("w")
        sleep(0.01)
    if key[pygame.K_a]:
        print("a")
        sleep(0.01)
    if key[pygame.K_s]:
        print("s")
        sleep(0.01)
    if key[pygame.K_d]:
        print("d")
        sleep(0.01)
    if key[pygame.K_e and pygame.K_r]:
        print("Rotate")
        sleep(0.01)
    pygame.display.update()