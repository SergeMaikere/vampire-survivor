from settings import *

class All_Sprites ( pygame.sprite.Group ):
	def __init__(self ):
		super().__init__()

		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.Vector2()


	def draw ( self, player_pos: tuple[float, float] ):
		self.offset.x = - (player_pos[0] - WINDOW_WIDTH/2)
		self.offset.y = - (player_pos[1] - WINDOW_HEIGHT/2)
		for sprite in self:
			self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)
