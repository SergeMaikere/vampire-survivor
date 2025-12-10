from typing import cast
from pygame import FRect, Surface
from settings import *
from pygame.sprite import Group

class Sprite ( pygame.sprite.Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], image: Surface, **anchor: tuple):
		super().__init__(group)
		self._og_image = image
		self.image = self._og_image.copy()
		self.rect = self.image.get_frect(**anchor)

