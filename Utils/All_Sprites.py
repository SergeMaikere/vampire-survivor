from settings import *

class All_Sprites ( pygame.sprite.Group ):
	def __init__(self ):
		super().__init__()

		self.display_surface = pygame.display.get_surface()
		self.offset = pygame.Vector2()

	def __set_offset ( self, player_pos: tuple[float, float] ):
		self.offset.x = - (player_pos[0] - WINDOW_WIDTH/2)
		self.offset.y = - (player_pos[1] - WINDOW_HEIGHT/2)

	def __make_camera_follow_player ( self ):
		grounds_tiles = [ sprite for sprite in self if hasattr(sprite, 'ground') ]
		game_objects = [ sprite for sprite in self if not hasattr(sprite, 'ground') ]

		for layer in [ grounds_tiles, game_objects ]:
			for sprite in sorted(layer, key= lambda sprite: sprite.rect.centery):
				self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)


	def draw ( self, player_pos: tuple[float, float] ):
		self.__set_offset(player_pos)
		self.__make_camera_follow_player()

