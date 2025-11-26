from settings import *
from pygame.sprite import Group
from Utils.Sprite import Sprite
from Utils.Loader import image_loader

class Player ( Sprite ):
	def __init__( self, group: Group, **anchor ):
		super().__init__(group, image_loader('0.png'), **anchor)

		self.direction = pygame.Vector2()
		self.speed = 500

	def __set_direction( self, keys ):
		self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
		self.direction = self.direction.normalize() if self.direction else self.direction

	def __move ( self, dt ):
		self.rect.center += self.direction * self.speed * dt

	def update ( self, dt: int ):
		keys = pygame.key.get_pressed()
		self.__set_direction(keys)
		self.__move(dt)