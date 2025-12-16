from settings import *
from typing import Any
from pygame import Surface
from pygame.key import ScancodeWrapper
from pygame.sprite import Group
from Utils.Sprite import Sprite
from Utils.Helper import split_path, get_into_folder
from Utils.Loader import get_frame, image_loader

class Player ( Sprite ):
	def __init__( self, group: Group, pos: tuple[float, float] ):
		super().__init__(group, image_loader(join('assets', 'images', 'player', 'down'), '0.png'), center=pos)

		self.hitbox_rect = self.rect.inflate(-60, -90)
		self.direction = pygame.Vector2()
		self.speed = 500

		self.state = 'down'
		self.frames_i = 0
		self.frames = self.__make_player_frames()

	def __make_player_frames ( self ) -> dict[str, list[Surface]]:
		frames = {}
		for root, _directories, files in get_into_folder('assets', 'images', 'player'):
			if files: frames[ split_path(root).pop() ] = [ get_frame(root, file) for file in files ]
		return frames

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


	def __set_state ( self ):
		if self.direction.x > 0: self.state = 'right'
		if self.direction.x < 0: self.state = 'left'
		if self.direction.y > 0: self.state = 'down'
		if self.direction.y < 0: self.state = 'up'
		

	def __animate ( self, dt: float ):
		self.frames_i = self.frames_i + 5 * dt if self.direction else 0
		self.image = self.frames[self.state][int(self.frames_i) % len(self.frames[self.state])]

	def __move ( self ):
		self.rect.center = self.hitbox_rect.center

	def __on_collide ( self, dt: float, collision_sprites: Group ):
		self.hitbox_rect.x += self.direction.x * self.speed * dt
		self.__collision_handler(collision_sprites, 'horizontal')

		self.hitbox_rect.y += self.direction.y * self.speed * dt
		self.__collision_handler(collision_sprites, 'vertical')


	def update ( self, give_me: dict[str, Any] ):
		self.__set_direction(pygame.key.get_pressed())
		self.__set_state()
		self.__animate(give_me['dt'])
		self.__on_collide(give_me['dt'], give_me['groups']['collision_sprites'])
		self.__move()