import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import Gamestats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make a group to store aliens in.
    aliens = Group()
    # Make a stats of game and creat a scoreboard
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a button of play
    play_button = Button(ai_settings, screen, "Play")

    # Creat alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
run_game()
