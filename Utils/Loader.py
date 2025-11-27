from pygame.sprite import Group
from pytmx import TiledElement, TiledMap, TiledObject
from Utils.Sprite import Sprite
from settings import *
from typing import Callable
from pygame.surface import Surface
from Utils.Helper import pipe
from pytmx.util_pygame import load_pygame


load_image: Callable[ [str], Surface ] = lambda filename: pygame.image.load( join('assets', 'images', 'player', 'right', filename) )

convert_image: Callable[ [Surface, bool], Surface ] = lambda image, alpha=True: image.convert_alpha() if alpha else image.convert()

image_loader: Callable[ [str], Surface ] = pipe( load_image, convert_image )

load_map: Callable[ [str], TiledMap ] = lambda layer: load_pygame(layer)
