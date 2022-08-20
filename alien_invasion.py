import sys
import pygame

from settings import Settings
from player import PlayerShip
from bullet import Bullet
from alien import Alien


class AlienInvasionGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        # self._set_full_screen_mode()
        self._set_windowed_mode()
        # window label text
        pygame.display.set_caption('Alien Invasion Game')
        self.player = PlayerShip(self)
        # group to manage bullets
        self.bullets = pygame.sprite.Group()
        # Set the background color.
        self.bg_color = self.settings.bg_color
        # Spawn aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.player.update()
            self._update_screen()
            self._update_bullets()

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
        if event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        # press q to quit
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        # space to fire bullets
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it tot the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""

        # Redraw the screen during each pass throug the loop.
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Draw aliens
        self.aliens.draw(self.screen)
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

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = int(available_space_x // (1.5 * alien_width))

        # Determine the number of rows of aliens that fit on the screen.
        player_height = self.player.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - player_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

        # Create the first row of aliens.
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasionGame()
    ai.run_game()