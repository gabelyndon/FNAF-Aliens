import sys
import pygame
from pygame.sprite import Group 
from settings import Settings 
from game_stats import GameStats 
from ship import Ship 
from alien import Alien 
import game_functions as gf 


def run_game():
	#intialize pygame, settings, and screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	screen = pygame.display.set_mode((1200,800))

	pygame.display.set_caption("FIVE NIGHTS AT FREDDY'S INVASION")

	#create an instance to store game statistics
	stats = GameStats(ai_settings)

	#make a ship,bullets, and group of aliens
	ship = Ship(ai_settings,screen)
	bullets = Group() 
	aliens = Group() 

	#create the fleet of aliens
	gf.create_fleet(ai_settings,screen,ship,aliens)

	#start the main loop for the game     
	while True:

		gf.check_events(ai_settings,screen,ship,aliens,bullets)

		if stats.game_active:	
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings,stats,screen,ship, aliens,bullets)
		
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
 
run_game()
