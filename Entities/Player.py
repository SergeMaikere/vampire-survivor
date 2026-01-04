from settings import *
from typing import Any
from pygame.key import ScancodeWrapper
from pygame.sprite import Group
from Entities.Entity import Entity
from Utils.Loader import image_loader, load_frames

class Player ( Entity ):
	def __init__( self, group: Group, pos: tuple[float, float] ):
		super().__init__(group, image_loader(join('assets', 'images', 'player', 'down'), '0.png'), center=pos)

		self.hitbox_rect = self.rect.inflate(-60, -90)
		self.direction = pygame.Vector2()
		self.speed = 500

		self.state = 'down'
		self.frames_i = 0
		self.frames = load_frames( join('assets', 'images', 'player') )

	def __set_direction( self, keys: ScancodeWrapper ):
		self.direction.x = int(keys[pygame.K_f]) - int(keys[pygame.K_s])
		self.direction.y = int(keys[pygame.K_d]) - int(keys[pygame.K_e])
		self.direction = self.direction.normalize() if self.direction else self.direction


	def __set_state ( self ):
		if self.direction.x > 0: self.state = 'right'
		if self.direction.x < 0: self.state = 'left'
		if self.direction.y > 0: self.state = 'down'
		if self.direction.y < 0: self.state = 'up'
		

	def __animate ( self, dt: float ):
		self.frames_i = self.frames_i + 5 * dt if self.direction else 0
		self.image = self.frames[self.state][int(self.frames_i) % len(self.frames[self.state])]

	def __game_over ( self, game_over: int ):
		pygame.event.post(pygame.event.Event(game_over))

	def __on_collide_with_enemy ( self, enemy_sprites: Group, game_over: int ):
		if pygame.sprite.spritecollide(self, enemy_sprites, True, pygame.sprite.collide_mask): 
			self.__game_over(game_over)

	def update ( self, give: dict[str, Any] ):
		self.__set_direction(pygame.key.get_pressed())
		self.__set_state()
		self.__animate(give['dt'])
		self._on_collide(give['dt'], give['groups']['collision_sprites'])
		self.__on_collide_with_enemy(give['groups']['enemy_sprites'], give['events']['game_over'])
		self._move()