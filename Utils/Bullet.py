from typing import Any
from pygame import Sound, Vector2
from pygame.sprite import Group
from settings import *
from Utils.Sprite import Sprite
from Entities.Enemy import Enemy
from Utils.Loader import image_loader

class Bullet ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], pos: tuple[float, float], direction: Vector2, impact_sound: Sound):
		super().__init__(group, image_loader(join('assets', 'images', 'gun'), 'bullet.png'), center=pos)
		
		self.direction = direction
		self.speed = 1200

		self.time_of_birth = pygame.time.get_ticks()
		self.expiration_time = 1000

		self.impact_sound = impact_sound

	def __move ( self, dt: float ):
		self.rect.center += self.direction * self.speed * dt

	def __die_of_screen ( self ):
		current = pygame.time.get_ticks()
		if current - self.time_of_birth >= self.expiration_time : self.kill()

	def __make_impact_sound ( self ):
		self.impact_sound.play()
		self.impact_sound.set_volume(0.8)


	def __kill_enemy ( self, sprite: Enemy ):
		self.kill()
		sprite.die()
		self.__make_impact_sound()


	def __on_collide_with_enemy ( self, enemy_sprites: Group ):
		sprites = pygame.sprite.spritecollide(self, enemy_sprites, True)
		for sprite in sprites: 
			self.__kill_enemy(sprite)


	def update ( self, give: dict[str, Any] ):
		self.__die_of_screen()
		self.__on_collide_with_enemy(give['groups']['enemy_sprites'])
		self.__move(give['dt'])