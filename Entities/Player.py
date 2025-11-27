from typing import Any
from pygame.key import ScancodeWrapper
from settings import *
from pygame.sprite import Group
from Utils.Sprite import Sprite
from Utils.Loader import image_loader

class Player ( Sprite ):
	def __init__( self, group: Group ):
		super().__init__(group, image_loader('0.png'), center=(200, 200))

		self.hitbox_rect = self.rect.inflate(-80, 0)
		self.direction = pygame.Vector2()
		self.speed = 500

	def __collision_handler ( self, collision_sprites: Group, direction: str ):
		for sprite in collision_sprites:
			if sprite.rect.colliderect(self.hitbox_rect):

				if direction == 'horizontal':
					if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
					if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right

				if direction == 'vertical':
					if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
					if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom


	def __set_direction( self, keys: ScancodeWrapper ):
		self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
		self.direction = self.direction.normalize() if self.direction else self.direction

	def __move ( self, dt: float, collision_sprites: Group ):
		self.hitbox_rect.x += self.direction.x * self.speed * dt
		self.__collision_handler(collision_sprites, 'horizontal')

		self.hitbox_rect.y += self.direction.y * self.speed * dt
		self.__collision_handler(collision_sprites, 'vertical')

		self.rect.center = self.hitbox_rect.center

	def update ( self, give_me: dict[str, Any] ):
		keys = pygame.key.get_pressed()
		self.__set_direction(keys)
		self.__move(give_me['dt'], give_me['collision_sprites'])