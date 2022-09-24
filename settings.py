class Settings:
    """A class to store all settigns for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 120)

        # Ship settings
        self.ship_speed = 1.1

        # Bullet settingss
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 1
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

