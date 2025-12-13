from settings import *
from typing import Any
from pygame import Surface, Vector2
from pygame.sprite import Group
from Utils.Sprite import Sprite
from Utils.Bullet import Bullet
from Entities.Player import Player
from Utils.Loader import image_loader
from Utils.Helper import pipe
from math import atan2, degrees


class Gun ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], player: Player):

		self.player = player
		self.player_position = pygame.Vector2( (WINDOW_WIDTH/2, WINDOW_HEIGHT/2) )
		self.player_distance = 140
		self.player_direction = pygame.Vector2(1,0)

		super().__init__(
			group, 
			image_loader(join('assets', 'images', 'gun'), 'gun.png'), 
			center= self.player.rect.center + self.player_direction * self.player_distance
		)


	def __get_mouse_vector ( self ):
		return pygame.Vector2( pygame.mouse.get_pos() )

	def __set_player_direction ( self , mouse_position: Vector2 ):
		self.player_direction = (mouse_position - self.player_position).normalize()
		return self.player_direction

	def __get_angle ( self, direction: Vector2 ):
		return degrees( atan2(direction.x, direction.y) ) - 90

	def __rotate ( self, angle: float ):
		if self.player_direction.x > 0: return pygame.transform.rotozoom(self._og_image, angle, 1)
		if self.player_direction.x <= 0: return pygame.transform.rotozoom(self._og_image, abs(angle), 1)

	def __flip_gun ( self, image: Surface ):
		if self.player_direction.x > 0: return image
		return pygame.transform.flip(image, False, True)

	def __image_handler ( self ):
		self.image = pipe(
			self.__set_player_direction,
			self.__get_angle,
			self.__rotate,
			self.__flip_gun,
		)(self.__get_mouse_vector())

	def __is_player_shooting ( self ):
		return pygame.mouse.get_just_released()[0]

	def __shoot ( self ):
		if not self.__is_player_shooting(): return
		Bullet(self.group, self.rect.midright, self.player_direction)

	def __move ( self ):
		self.rect.center = self.player.rect.center + self.player_direction * self.player_distance

	def update ( self, give: dict[str, Any] ):
		self.__image_handler()
		self.__shoot()
		self.__move()
