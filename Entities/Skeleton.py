from pygame.sprite import Group
from settings import *
from Utils.Sprite import Sprite
from Utils.Loader import image_loader
from Utils.Helper import get_random_pos

class Skeleton ( Sprite ):
	def __init__(self, group: Group | tuple[Group, ...], dimensions: tuple[float, float]):
		super().__init__(
			group, 
			image_loader(join('assets', 'images', 'enemies', 'skeleton'), '0.png'), 
			center = get_random_pos(dimensions[0], dimensions[1])
		)