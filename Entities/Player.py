from typing import Any
from pygame import Surface
from pygame.key import ScancodeWrapper
from settings import *
from pygame.sprite import Group
from Utils.Sprite import Sprite
from Utils.Loader import PLAYER_ANIMS_PATHS, get_frames, image_loader
from Animations.Animation import Animation

class Player ( Sprite ):
	def __init__( self, group: Group, pos: tuple[float, float] ):
		super().__init__(group, image_loader(join(*PLAYER_ANIMS_PATHS['UP']), '0.png'), center=pos)

		self.hitbox_rect = self.rect.inflate(-80, 0)
		self.direction = pygame.Vector2()
		self.speed = 500

		self.frames_i = 0
		self.frames_go_right = get_frames(PLAYER_ANIMS_PATHS['RIGHT'], 4)
		self.frames_go_left = get_frames(PLAYER_ANIMS_PATHS['LEFT'], 4)
		self.frames_go_up = get_frames(PLAYER_ANIMS_PATHS['UP'], 4)
		self.frames_go_down = get_frames(PLAYER_ANIMS_PATHS['DOWN'], 4)


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

	def __set_animation ( self, dt: float, frames: list[Surface] ):
		self.frames_i += int(dt * 65)
		if self.frames_i >= len(frames): self.frames_i = 0
		self.image = frames[self.frames_i]

	def __lauch_animation ( self, dt: float ):
		if self.direction.x > 0: self.__set_animation(dt, self.frames_go_right)
		if self.direction.x < 0: self.__set_animation(dt, self.frames_go_left)
		if self.direction.y > 0: self.__set_animation(dt, self.frames_go_down)
		if self.direction.y < 0: self.__set_animation(dt, self.frames_go_up)

	def __move ( self, dt: float, collision_sprites: Group ):
		self.hitbox_rect.x += self.direction.x * self.speed * dt
		self.__collision_handler(collision_sprites, 'horizontal')

		self.hitbox_rect.y += self.direction.y * self.speed * dt
		self.__collision_handler(collision_sprites, 'vertical')

		self.rect.center = self.hitbox_rect.center

	def update ( self, give_me: dict[str, Any] ):
		keys = pygame.key.get_pressed()
		self.__set_direction(keys)
		self.__lauch_animation(give_me['dt'])
		self.__move(give_me['dt'], give_me['groups']['collision_sprites'])