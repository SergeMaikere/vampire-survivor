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

image_loader = pipe( load_image, convert_image )

load_map: Callable[ [str], TiledMap ] = lambda layer: load_pygame(layer)

make_tile: Callable[ [Group, float, float, Surface], Sprite ] = lambda group, x, y, image : Sprite(group, image, topleft=(x * TILE_SIZE, y * TILE_SIZE))

make_obj: Callable[ [Group, TiledObject], Sprite ] = lambda group, obj : Sprite(group, obj.image, topleft=(obj.x, obj.y))
