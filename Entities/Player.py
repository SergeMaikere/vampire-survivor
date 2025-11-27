from settings import *
from pygame.sprite import Group
from Utils.Sprite import Sprite
from Utils.Loader import image_loader

class Player ( Sprite ):
	def __init__( self, group: Group, **anchor ):
		super().__init__(group, image_loader('0.png'), **anchor)

		self.direction = pygame.Vector2()
		self.speed = 500

	def __collision_handler ( self, collision_sprites: Group, direction: str ):
		for sprite in collision_sprites:
			if sprite.rect.colliderect(self.rect):
				if direction == 'horizontal':
					if self.direction.x > 0: self.rect.right = sprite.rect.left
					if self.direction.x < 0: self.rect.left = sprite.rect.right
				if direction == 'vertical':
					if self.direction.y > 0: self.rect.bottom = sprite.rect.top
					if self.direction.y < 0: self.rect.top = sprite.rect.bottom


	def __set_direction( self, keys: list[bool] ):
		self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
		self.direction = self.direction.normalize() if self.direction else self.direction

	def __move ( self, dt: float, collision_sprites: Group ):
		self.rect.x += self.direction.x * self.speed * dt
		self.__collision_handler(collision_sprites, 'horizontal')
		self.rect.y += self.direction.y * self.speed * dt
		self.__collision_handler(collision_sprites, 'vertical')

	def update ( self, give_me: dict ):
		keys = pygame.key.get_pressed()
		self.__set_direction(keys)
		self.__move(give_me['dt'], give_me['collision_sprites'])