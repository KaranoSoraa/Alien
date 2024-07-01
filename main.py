import pygame
from pygame.sprite import Group
from settings import Setting
from ship import Ship
from Lib import game_functions as gf


def run_game():
    # Инициализация pygame
    pygame.init()
    # Создал экземпляр настроек.
    ai_settings = Setting()
    # Создание игрового окна 1200 ширина - 800 - высота
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Создал экземпляр корабля.
    ship = Ship(ai_settings, screen)
    # Создаем группу для хранения пуль
    bullets = Group()
    aliens = Group()
    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Даем название игре.
    pygame.display.set_caption("Alien Invasion")

    while True:
        # Проверка действий пользователя
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
