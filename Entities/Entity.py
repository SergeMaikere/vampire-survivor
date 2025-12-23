from pygame import Surface, Vector2
from pygame.sprite import Group
from settings import *
from Utils.Sprite import Sprite
from Utils.Helper import split_path, get_into_folder
from Utils.Loader import get_frame

class Entity ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], image: Surface, **anchor: tuple[float, float] | Vector2):
		super().__init__(group, image, **anchor)

		self.hitbox_rect = self.rect.inflate(-50, -50)
		self.speed = 100
		self.direction = pygame.Vector2()

	# 	self._path: list[str] = []
	# 	self.frames_i = 0
	# 	self.frames = {}
	# 	self.state: str = 'state'

	# @property
	# def path ( self ):
	# 	return self._path

	# @path.setter
	# def path ( self, value: list[str] ):
	# 	self._path = value
	# 	self.frames = self.__make_player_frames()

	# def __make_player_frames ( self ) -> dict[str, list[Surface]]:
	# 	frames = {}
	# 	for root, _directories, files in get_into_folder(*self._path):
	# 		if files: frames[ split_path(root).pop() ] = [ get_frame(root, file) for file in files ]
	# 	return frames

	
	# def _animate ( self, dt: float ):
	# 	self.frames_i += dt * 5 
	# 	self.image = self.frames[self.state][int(self.frames_i) % len(self.frames[self.state])]


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
