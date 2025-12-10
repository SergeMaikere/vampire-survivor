from typing import Any
from settings import *
from pygame.sprite import Group
from Utils.Sprite import Sprite
from Entities.Player import Player
from Utils.Loader import image_loader


class Gun ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], player: Player):

		self.player = player
		self.player_distance = 140
		self.player_direction = pygame.Vector2(1,0)

		super().__init__(
			group, 
			image_loader(join('assets', 'images', 'gun'), 'gun.png'), 
			center= self.player.rect.center + self.player_direction * self.player_distance
		)

	def __get_direction ( self ):
		mouse_position = pygame.Vector2( pygame.mouse.get_pos() )
		player_position = pygame.Vector2( (WINDOW_WIDTH/2, WINDOW_HEIGHT/2) )
		self.player_direction = (mouse_position - player_position).normalize()

	def __move ( self ):
		self.rect.center = self.player.rect.center + self.player_direction * self.player_distance

	def update ( self, give: dict[str, Any] ):
		self.__get_direction()
		self.__move()