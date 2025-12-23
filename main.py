from typing import Any
from pygame import Event
from settings import *
from pytmx import TiledMap
from Entities.Player import Player
from Entities.Enemy import Enemy
from Utils.All_Sprites import All_Sprites
from Utils.Sprite import Sprite
from Utils.Ground import Ground
from Utils.Gun import Gun
from Utils.Helper import pipe
from Utils.Loader import load_map, load_frames
from random import randint

class Game ():

	def __init__( self ) -> None:
		pygame.init()
		pygame.display.set_caption('Vampire Survivor II: Back for Blood!')
     
		self.clock = pygame.time.Clock()
		self.screen_image = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		
		self.all_sprites = All_Sprites()
		self.collision_sprites = pygame.sprite.Group()
		self.enemy_sprites = pygame.sprite.Group()
		
		self.enemy_frames = load_frames('assets', 'images', 'enemies')
		self.spawn_enemy = pygame.event.custom_type()
		self.enemy_type = [ 'bat', 'blob', 'skeleton' ]

		self.give_me: dict[str, Any] = { 
			'groups': {
				'all_sprites': self.all_sprites, 
				'collision_sprites': self.collision_sprites
			}
		}

		self.running = True


	def __time_to_quit ( self, event: Event ):
		return event.type == pygame.QUIT

	def __make_enemy ( self ):
		type = self.enemy_type[ randint(0, len(self.enemy_type) - 1) ]
		return Enemy((self.all_sprites, self.enemy_sprites), self.player, self.map, type, self.enemy_frames[type])

	def __event_loop ( self ) -> None:
		for event in pygame.event.get():
			self.running = not self.__time_to_quit(event)
			if event.type == self.spawn_enemy: self.__make_enemy()

	def __set_map_dimensions ( self, maps: TiledMap ):
		self.map = ( maps.width * TILE_SIZE, maps.height * TILE_SIZE )
		return maps

	def __make_ground ( self, maps: TiledMap ):
		for x, y, image in maps.get_layer_by_name('Ground').tiles():
			Ground( self.all_sprites, image, topleft=(x * TILE_SIZE, y * TILE_SIZE) )
		return maps

	def __make_objects ( self, maps: TiledMap):
		for obj in maps.get_layer_by_name('Objects'):
			Sprite( (self.all_sprites, self.collision_sprites), obj.image, topleft=(obj.x, obj.y) )
		return maps

	def __make_invisible_walls ( self, maps: TiledMap ):
		for obj in maps.get_layer_by_name('Collisions'):
			Sprite( self.collision_sprites, pygame.Surface((obj.width, obj.height)), topleft=(obj.x, obj.y) )
		return maps

	def __make_player ( self, maps: TiledMap ):
		for obj in maps.get_layer_by_name('Entities'): 
			if not obj.name == 'Player': return obj
			self.player = Player(self.all_sprites, (obj.x, obj.y))
		return maps

	def __setup_map ( self ):
		return pipe(
			self.__set_map_dimensions,
			self.__make_ground,
			self.__make_objects,
			self.__make_invisible_walls,
			self.__make_player,
		)(load_map())

	def __make_gun ( self ):
		self.gun = Gun( self.all_sprites, self.player )

	def __set_enemy_spawn_event ( self ):
		pygame.time.set_timer(self.spawn_enemy, 500)

	def run ( self ):
		self.__setup_map()
		self.__make_gun()
		self.__set_enemy_spawn_event()
		
		while self.running:
			self.give_me['dt'] = self.clock.tick() / 1000

			self.__event_loop()

			self.all_sprites.update(self.give_me)

			self.all_sprites.draw(self.player.rect.center)

			pygame.display.update()

		pygame.quit()


if __name__ == '__main__':
	new_game = Game()
	new_game.run()