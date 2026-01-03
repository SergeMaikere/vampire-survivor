from pygame import Sound
from pytmx import TiledMap
from settings import *
from typing import Callable
from pygame.surface import Surface
from Utils.Helper import pipe, curry, get_into_folder, split_path
from pytmx.util_pygame import load_pygame


load_sound: Callable[ [str], Sound ] = lambda filename: pygame.mixer.Sound( join('assets', 'audio', filename) )

load_image: Callable[ [str, str], Surface ] = lambda path, filename: pygame.image.load( join(path, filename) )

convert_image: Callable[ [Surface, bool], Surface ] = lambda image, alpha=True: image.convert_alpha() if alpha else image.convert()

image_loader: Callable[ [str, str], Surface ] = lambda path, filename: pipe( curry(load_image)(path), convert_image )(filename)

load_map: Callable[ [], TiledMap ] = lambda : load_pygame( join('assets', 'data', 'maps', 'world.tmx') )

get_frame: Callable[ [str, str], Surface ] = lambda path, filename: pipe( curry(load_image)(path), convert_image )(filename)

def load_frames ( *path: str ) -> dict[str, list[Surface]]:
	frames = {}
	for root, _directories, files in get_into_folder(*path):
		if files: frames[ split_path(root).pop() ] = [ get_frame(root, file) for file in files ]
	return frames

