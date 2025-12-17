from settings import *
from Utils.Sprite import Sprite
from types import FunctionType
from typing import Any, Callable, Iterable, Iterator
from functools import reduce
from inspect import signature
from pathlib import Path
import random

pipe = lambda *funcs: lambda arg: reduce( lambda g, f: f(g), funcs, arg )

def curry ( fn: FunctionType ):
	def curried ( *args: Any ):
		if len(args) >= len(signature(fn).parameters):
			return fn(*args)
		else:
			return lambda *args2: curried( *args, *args2 )
	return curried

get_into_folder: Callable[ ..., Iterator[tuple[str, list[str], list[str]]] ] = lambda *path: walk(join(*path))

split_path: Callable[ [str], list[str] ] = lambda path: list(Path(path).parts)

get_random_pos: Callable[ [float, float], tuple[float, float] ] = lambda width, height : ( random.uniform(0, width), random.uniform(0, height) )


