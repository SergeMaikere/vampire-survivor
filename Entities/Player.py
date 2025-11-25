import pygame
from pygame.sprite import Group
from Utils.Sprite import Sprite
from Utils.Loader import image_loader

class Player ( Sprite ):
	def __init__( self, group: Group, **anchor ):
		super().__init__(group, image_loader('0.png'), **anchor)

		self.position = (0,0)

	def __set_position( self ):
		self.position = pygame.mouse.get_pos()

	def __move ( self, dt ):
		self.rect.center = self.position

	def update ( self, dt: int ):
		self.__set_position()
		self.__move(dt)