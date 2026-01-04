from pygame import FRect, Surface, Vector2
from settings import *
from pygame.sprite import Group

class Sprite ( pygame.sprite.Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], image: Surface, **anchor: tuple[float, float] | Vector2):
		super().__init__(group)
		self.group = group
		self._og_image: Surface = image
		self.image: Surface = self._og_image.copy()
		self.rect: FRect = self.image.get_frect(**anchor)

