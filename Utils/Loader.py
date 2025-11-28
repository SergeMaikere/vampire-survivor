from pytmx import TiledMap
from settings import *
from typing import Callable
from pygame.surface import Surface
from Utils.Helper import pipe, curry
from pytmx.util_pygame import load_pygame


PLAYER_ANIMS_PATHS = {
	'UP': [ 'assets', 'images', 'player', 'up' ],
	'RIGHT': [ 'assets', 'images', 'player', 'right' ],
	'DOWN': [ 'assets', 'images', 'player', 'down' ],
	'LEFT': [ 'assets', 'images', 'player', 'left' ],
}


load_image: Callable[ [str, str], Surface ] = lambda path, filename: pygame.image.load( join(path, filename) )

load_animation_image: Callable[ [str, int], Surface ] = lambda path, n: pygame.image.load(join(path, f'{n}.png'))

convert_image: Callable[ [Surface, bool], Surface ] = lambda image, alpha=True: image.convert_alpha() if alpha else image.convert()

image_loader: Callable[ [str, str], Surface ] = lambda path, filename: pipe( curry(load_image)(path), convert_image )(filename)

load_map: Callable[ [str], TiledMap ] = lambda layer: load_pygame(layer)

get_frames: Callable[ [list[str], int], list[Surface] ] = lambda path, length: [ get_frame(join(*path), i) for i in range(length) ]

def get_frame ( path: str, n: int ) -> Surface:
	return pipe(
		curry(load_animation_image)(path),
		convert_image
	)(n)
