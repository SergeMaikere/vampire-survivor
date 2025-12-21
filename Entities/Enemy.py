from typing import Any
from pygame.sprite import Group
from Entities.Player import Player
from Entities.Entity import Entity
from settings import *
from Utils.Loader import image_loader
from Utils.Helper import get_random_pos

class Enemy ( Entity ):
	def __init__(self, group: Group | tuple[Group, ...], player: Player, dimensions: tuple[float, float], type: str):
		super().__init__(
			group, 
			image_loader(join('assets', 'images', 'enemies', type), '0.png'), 
			center = get_random_pos(dimensions[0], dimensions[1])
		)
		self.player = player
		self.path = [ 'assets', 'images', 'enemies', type ]
		self.state = type

	def __get_direction ( self ):
		self.direction = (pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center)).normalize()

	
	def update ( self, give: dict[str, Any] ):
		self.__get_direction()
		self._animate(give['dt'])
		self._on_collide(give['dt'], give['groups']['collision_sprites'])
		self._move()