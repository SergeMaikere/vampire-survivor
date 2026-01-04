from typing import Any
from pygame import Surface
from pygame.sprite import Group
from Entities.Player import Player
from Entities.Entity import Entity
from settings import *
from Utils.Loader import image_loader

class Enemy ( Entity ):
	def __init__(self, group: Group | tuple[Group, ...], player: Player, pos: tuple[float, float], type: str, frames: list[Surface]):
		super().__init__(
			group, 
			image_loader(join('assets', 'images', 'enemies', type), '0.png'), 
			center = pos
		)
		self.is_shot = False
		
		self.player = player

		self.frames, self.frames_i = frames, 0

		self.death_delay = 400
		self.time_of_death = 0

	def __get_direction ( self ):
		self.direction = (pygame.Vector2(self.player.rect.center) - pygame.Vector2(self.rect.center)).normalize()

	def _animate ( self, dt: float ):
		self.frames_i += dt * 5 
		self.image = self.frames[int(self.frames_i) % len(self.frames)]

	def __update_death_properties ( self ):
		self.is_shot = True
		self.time_of_death = pygame.time.get_ticks()


	def __set_death_frame ( self ):
		mask = pygame.mask.from_surface(self.image)
		self.image = mask.to_surface(setcolor=(255,255,255,255), unsetcolor=(0,0,0,0))
		print(self.time_of_death, 'time_of_death')
		print(self.is_shot, 'is_shot')


	def __wait_to_die ( self ):
		now = pygame.time.get_ticks()
		if now - self.time_of_death >= self.death_delay: self.kill()


	def die ( self ):
		self.__update_death_properties()
		self.__set_death_frame()

	def update ( self, give: dict[str, Any] ):
		if self.is_shot: self.__wait_to_die()

		self.__get_direction()
		self._animate(give['dt'])
		self._on_collide(give['dt'], give['groups']['collision_sprites'])
		self._move()