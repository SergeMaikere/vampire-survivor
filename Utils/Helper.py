from functools import reduce
from inspect import signature
from numpy import random
import pygame

pipe = lambda *funcs: lambda arg: reduce( lambda g, f: f(g), funcs, arg )

def curry ( fn ):
	def curried ( *args ):
		if len(args) >= len(signature(fn).parameters):
			return fn(*args)
		else:
			return lambda *args2: curried( *args, *args2 )
	return curried

adjust_func_for_list_map = lambda func: lambda my_list: [ func(x) for x in my_list ]

remove_format_from_file_name = lambda file: file.split('.')[0]

add_keys_to_list = lambda my_keys, my_list: [ [ my_keys[i], item ] for i, item in enumerate(my_list) ]

def add_to_obj ( obj, item ):
	obj[item[0]] = item[1]
	return obj

get_random_pos = lambda w, h: ( random.randint(0, w), random.randint(0, h) )

def set_rect ( anchor, position, surface ):

	if anchor == 'topleft':
		rect = surface.get_rect(topleft=position)
	elif anchor == 'midtop':
		rect = surface.get_rect(midtop=position)
	elif anchor == 'topright':
		rect = surface.get_rect(topright=position)
	elif anchor == 'midright':
		rect = surface.get_rect(midright=position)
	elif anchor == 'bottomright':
		rect = surface.get_rect(bottomright=position)
	elif anchor == 'midbottom':
		rect = surface.get_rect(midbottom=position)
	elif anchor == 'bottomleft':
		rect = surface.get_rect(bottomleft=position)
	elif anchor == 'midleft':
		rect = surface.get_rect(midleft=position)
	else:
		rect = surface.get_rect(center=position)

	return rect

is_out_of_bound = lambda rect, width, height: is_out_of_bound_x(rect, width) or is_out_of_bound_y(rect, height)
is_out_of_bound_x = lambda rect, width: rect.left <= 0 or rect.right >= width
is_out_of_bound_y = lambda rect, height: rect.top <= 0 or rect.bottom >= height

def add_to_surface (surface, game_obj): 
	surface.blit(game_obj.image, game_obj.rect) 
	return game_obj

def set_repeating_event ( every ):
	event = pygame.event.custom_type()
	pygame.time.set_timer(event, every)
	return event