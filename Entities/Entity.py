from pygame import Surface, Vector2
from pygame.sprite import Group
from settings import *
from Utils.Sprite import Sprite

class Entity ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], image: Surface, **anchor: tuple[float, float] | Vector2):
		super().__init__(group, image, **anchor)

		self.hitbox_rect = self.rect.inflate(-50, -50)
		self.speed = 50
		self.direction = pygame.Vector2()


	def _collision_handler ( self, collision_sprites: Group, direction: str ):
		for sprite in collision_sprites:
			if sprite.rect.colliderect(self.hitbox_rect):

				if direction == 'horizontal':
					if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
					if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right

				if direction == 'vertical':
					if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
					if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom


	def _on_collide ( self, dt: float, collision_sprites: Group ):
		self.hitbox_rect.x += self.direction.x * self.speed * dt
		self._collision_handler(collision_sprites, 'horizontal')

		self.hitbox_rect.y += self.direction.y * self.speed * dt
		self._collision_handler(collision_sprites, 'vertical')


	def _move ( self ):
		self.rect.center = self.hitbox_rect.center
