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
		self.hitbox_rect = self.rect.inflate(-50, -50)
		self.player = player
		self.speed = 100
		self.direction = pygame.Vector2()

	def __get_direction ( self ):
		self.direction = (pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center)).normalize()

	
	def __collision_handler ( self, collision_sprites: Group, direction: str ):
		for sprite in collision_sprites:
			if sprite.rect.colliderect(self.hitbox_rect):

				if direction == 'horizontal':
					if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
					if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right

				if direction == 'vertical':
					if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
					if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom


	def __on_collide ( self, dt: float, collision_sprites: Group ):
		self.hitbox_rect.x += self.direction.x * self.speed * dt
		self.__collision_handler(collision_sprites, 'horizontal')

		self.hitbox_rect.y += self.direction.y * self.speed * dt
		self.__collision_handler(collision_sprites, 'vertical')


	def __move ( self ):
		self.rect.center = self.hitbox_rect.center

	
	def update ( self, give: dict[str, Any] ):
		self.__get_direction()
		self.__on_collide(give['dt'], give['groups']['collision_sprites'])
		self.__move()