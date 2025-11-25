from typing import Callable
import pygame
from pygame.surface import Surface
from os.path import join
from Utils.Helper import pipe


load_image: Callable[ [str], Surface ] = lambda filename: pygame.image.load( join('assets', 'images', 'player', 'right', filename) )

convert_image: Callable[ [Surface, bool], Surface ] = lambda image, alpha=True: image.convert_alpha() if alpha else image.convert()

image_loader = pipe( load_image, convert_image )