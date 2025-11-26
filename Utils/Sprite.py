from settings import *
from pygame.sprite import Group

class Sprite ( pygame.sprite.Sprite ):
	def __init__(self, group: Group, image: pygame.Surface, **anchor: tuple):
		super().__init__(group)
		self._og_image = image
		self.image = self._og_image
		self.rect = self.image.get_frect(**anchor)