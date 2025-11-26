from pygame import Event
from Entities.Player import Player
from settings import *

class Game ():

	def __init__( self, text: str ) -> None:
		pygame.init()
		pygame.display.set_caption(text)

		self.clock = pygame.time.Clock()
		self.screen_image = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		self.all_sprites = pygame.sprite.Group()

		self.player = Player(self.all_sprites, center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

		self.running = True

	def __set_background_color ( self, color: tuple ) -> None:
			self.screen_image.fill(color)

	def __time_to_quit ( self, event: Event ):
		return event.type == pygame.QUIT

	def __event_loop ( self ) -> None:
		for event in pygame.event.get():
			self.running = not self.__time_to_quit(event)

	def run ( self ):
		while self.running:
			dt = self.clock.tick(60) / 1000

			self.__event_loop()

			self.__set_background_color((0, 0, 0))

			self.all_sprites.update(dt)

			self.all_sprites.draw(self.screen_image)

			pygame.display.update()

		pygame.quit()


if __name__ == '__main__':
	new_game = Game('Vampire Survivor II: Back for Blood!')
	new_game.run()