import pygame.image


class Ship():
    # Инициализируем корабль и задаем его начальную позицию.
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        # Загружаем изображение корабля.
        self.image = pygame.image.load("../images/ship.bmp")
        # Получаем прямоугольник.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый экземпляр корабля появляется снизу экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Обновляет rect на основе center
        self.rect.centerx = self.center

    def blitme(self):
        # Рисует корабль в его текущей позиции.
        self.screen.blit(self.image, self.rect)
