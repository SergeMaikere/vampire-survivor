from typing import Any
from pygame import Event
from pytmx import TiledMap
from Entities.Player import Player
from Utils.All_Sprites import All_Sprites
from Utils.Sprite import Sprite
from Utils.Helper import pipe
from Utils.Loader import load_map
from settings import *

class Game ():

	def __init__( self ) -> None:
		pygame.init()
		pygame.display.set_caption('Vampire Survivor II: Back for Blood!')
     
		self.clock = pygame.time.Clock()
		self.screen_image = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.all_sprites = All_Sprites()
		self.collision_sprites = pygame.sprite.Group()

		self.give_me: dict[str, Any] = { 
			'groups': {
				'all_sprites': self.all_sprites, 
				'collision_sprites': self.collision_sprites
			}
		}
		self.running = True


	def __time_to_quit ( self, event: Event ):
		return event.type == pygame.QUIT

	def __event_loop ( self ) -> None:
		for event in pygame.event.get():
			self.running = not self.__time_to_quit(event)

	def __make_ground ( self, maps: TiledMap ):
		for x, y, image in maps.get_layer_by_name('Ground').tiles():
			Sprite( self.all_sprites, image, topleft=(x * TILE_SIZE, y * TILE_SIZE) )
		return maps

	def __make_objects ( self, maps: TiledMap):
		for obj in maps.get_layer_by_name('Objects'):
			Sprite( (self.all_sprites, self.collision_sprites), obj.image, topleft=(obj.x, obj.y) )
		return maps

	def __make_invisible_walls ( self, maps: TiledMap ):
		for obj in maps.get_layer_by_name('Collisions'):
			Sprite( self.collision_sprites, pygame.Surface((obj.width, obj.height)), topleft=(obj.x, obj.y) )
		return maps

	def __make_player ( self, obj ):
		if not obj.name == 'Player': return obj
		self.player = Player(self.all_sprites, (obj.x, obj.y))

	def __make_entitites ( self, maps: TiledMap ):
		for obj in maps.get_layer_by_name('Entities'): 
			self.__make_player(obj)
		return maps


	def __setup_map ( self ):
		return pipe(
			self.__make_ground,
			self.__make_objects,
			self.__make_invisible_walls,
			self.__make_entitites
		)(load_map(join('assets', 'data', 'maps', 'world.tmx')))


	def run ( self ):
		self.__setup_map()

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