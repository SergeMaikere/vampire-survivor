from typing import Any
from pygame.sprite import Group
from Entities.Player import Player
from settings import *
from Utils.Sprite import Sprite
from Utils.Loader import image_loader
from Utils.Helper import get_random_pos

class Enemy ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], player: Player, dimensions: tuple[float, float], type: str):
		super().__init__(
			group, 
			image_loader(join('assets', 'images', 'enemies', type), '0.png'), 
			center = get_random_pos(dimensions[0], dimensions[1])
		)

		self.player = player
		self.speed = 100
		self.direction = pygame.Vector2()

	def __get_direction ( self ):
		self.direction = (pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center)).normalize()

	def __move ( self, dt: float ):
		self.rect.center += self.direction * self.speed * dt

	def update ( self, give: dict[str, Any] ):
		self.__get_direction()
		self.__move(give['dt'])