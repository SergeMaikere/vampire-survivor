from settings import *
from types import FunctionType
from typing import Any, Callable, Iterable
from functools import reduce
from inspect import signature
from pathlib import Path

pipe = lambda *funcs: lambda arg: reduce( lambda g, f: f(g), funcs, arg )

def curry ( fn: FunctionType ):
	def curried ( *args: Any ):
		if len(args) >= len(signature(fn).parameters):
			return fn(*args)
		else:
			return lambda *args2: curried( *args, *args2 )
	return curried

def foreach ( func: FunctionType, iter: Iterable ):
	for x in iter:
		func(x)
	return iter

split_path: Callable[ [str], list[str] ] = lambda path: list(Path(path).parts)



