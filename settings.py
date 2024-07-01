# Создали класс настроек игры.
class Setting():
    def __init__(self):
        self.screen_width = 1540
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 влево.
        self.fleet_direction = 1
        self.bullet_wight = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

