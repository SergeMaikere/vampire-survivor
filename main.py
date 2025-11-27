from pygame import Event
from Entities.Player import Player
from Utils.Loader import load_map, make_tile, make_obj
from Utils.Helper import curry, foreach, pipe
from settings import *

class Game ():

	def __init__( self ) -> None:
		pygame.init()
		pygame.display.set_caption('Vampire Survivor II: Back for Blood!')

		self.clock = pygame.time.Clock()
		self.screen_image = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.all_sprites = pygame.sprite.Group()
		self.collision_sprites = pygame.sprite.Group()

		self.give_me = { 'collision_sprites': self.collision_sprites }
		self.running = True


	def __time_to_quit ( self, event: Event ):
		return event.type == pygame.QUIT

	def __event_loop ( self ) -> None:
		for event in pygame.event.get():
			self.running = not self.__time_to_quit(event)

	def __setup_map ( self ):
		maps = load_map(join('assets', 'data', 'maps', 'world.tmx'))

		for x, y, image in maps.get_layer_by_name('Ground').tiles():
			make_tile(self.all_sprites, x, y, image)

		for obj in maps.get_layer_by_name('Objects'):
			make_obj((self.all_sprites, self.collision_sprites), obj)

	def run ( self ):

		self.__setup_map()
		self.player = Player(self.all_sprites, center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

		while self.running:
			self.give_me['dt'] = self.clock.tick(60) / 1000

			self.__event_loop()

			self.all_sprites.update(self.give_me)

			self.all_sprites.draw(self.screen_image)

			pygame.display.update()

		pygame.quit()


if __name__ == '__main__':
	new_game = Game()
	new_game.run()