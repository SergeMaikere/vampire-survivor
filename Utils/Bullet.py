from typing import Any
from pygame import Vector2
from pygame.sprite import Group
from settings import *
from Utils.Sprite import Sprite
from Utils.Loader import image_loader

class Bullet ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], pos: tuple[float, float], direction: Vector2):
		super().__init__(group, image_loader(join('assets', 'images', 'gun'), 'bullet.png'), center=pos)
		
		self.direction = direction
		self.speed = 1200
		self.time_of_birth = pygame.time.get_ticks()
		self.expiration_time = 1000

	def __move ( self, dt: float ):
		self.rect.center += self.direction * self.speed * dt

	def __die_of_screen ( self ):
		current = pygame.time.get_ticks()
		if current - self.time_of_birth >= self.expiration_time : self.kill()

	def update ( self, give: dict[str, Any] ):
		self.__move(give['dt'])
		self.__die_of_screen()