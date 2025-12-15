from typing import Any
from pygame import Vector2
from pygame.sprite import Group
from settings import *
from Utils.Sprite import Sprite
from Utils.Loader import image_loader

class Bullet ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], pos: tuple[float, float], direction: Vector2):
		super().__init__(group, image_loader(join('assets', 'images', 'gun'), 'bullet.png'), midbottom=pos)
		self.direction = direction
		self.speed = 600
		self.timer = 0
		self.clock = pygame.time.Clock()
		self.expiration_time = 2000

	def __move ( self, dt: float ):
		self.rect.center += self.direction * self.speed * dt

	def __die_of_screen ( self ):
		self.timer += self.clock.tick()
		if self.timer >= self.expiration_time: self.kill()

	def update ( self, give: dict[str, Any] ):
		self.__move(give['dt'])
		self.__die_of_screen()