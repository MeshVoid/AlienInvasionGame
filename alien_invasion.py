import sys
import pygame

from settings import Settings
from player import PlayerShip


class AlienInvasionGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        #self._set_full_screen_mode()
        self._set_windowed_mode()

        pygame.display.set_caption('Alien Invasion Game')

        self.player = PlayerShip(self)

        # Set the background color.
        self.bg_color = (0, 0, 120)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.player.update()

    def _check_events(self):
        """Check for keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        # press q to quit
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        # Redraw the screen during each pass throug the loop.
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _set_full_screen_mode(self):
        """Run the game in a fullscreen mode"""
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

    def _set_windowed_mode(self):
        """Run the game in a window"""
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height))


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasionGame()
    ai.run_game()
