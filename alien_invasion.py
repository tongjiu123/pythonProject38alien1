import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings .screen_width ,ai_settings .screen_hight ))
    pygame.display.set_caption("Alien_Invasion!")
    ship = Ship(ai_settings ,screen)
    bullets=Group()

     #creat a airship
    while True:
        #supervise
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings ,screen,ship,bullets)

    #see screen
run_game()

