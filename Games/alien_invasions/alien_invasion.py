from settings import Settings
import pygame
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from stars import Star
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ship and a group of bullets and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stars = Group()

    # Create the fleet of aliens and stars.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    gf.create_star(ai_settings, screen, stars)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb,
                        play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats,
                             sb, ship, aliens, bullets)
            gf.update_stars(ai_settings, stars)

        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, stars, play_button)


run_game()
