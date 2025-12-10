from pytmx import TiledMap
from settings import *
from typing import Callable
from pygame.surface import Surface
from Utils.Helper import pipe, curry
from pytmx.util_pygame import load_pygame


load_image: Callable[ [str, str], Surface ] = lambda path, filename: pygame.image.load( join(path, filename) )

convert_image: Callable[ [Surface, bool], Surface ] = lambda image, alpha=True: image.convert_alpha() if alpha else image.convert()

image_loader: Callable[ [str, str], Surface ] = lambda path, filename: pipe( curry(load_image)(path), convert_image )(filename)

load_map: Callable[ [str], TiledMap ] = lambda layer: load_pygame(layer)

get_frame: Callable[ [str, str], Surface ] = lambda path, filename: pipe( curry(load_image)(path), convert_image )(filename)
