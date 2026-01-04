from pygame import Surface
from pygame.sprite import Group
from settings import *
from Utils.Sprite import Sprite

class Ground ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], image: Surface, **anchor: tuple):
		super().__init__(group, image, **anchor)
		self.ground = True