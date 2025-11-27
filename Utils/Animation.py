from settings import *
from typing import Any
from pygame import Surface
from pygame.sprite import _GroupOrGroups
from Utils.Loader import load_animation_image, convert_image
from Utils.Helper import pipe, curry

class Animation ( pygame.sprite.Sprite ):
	def __init__(self, *groups: _GroupOrGroups[Any], path: str, length: int, **anchor: tuple[float, float]) -> None:
		super().__init__(*groups)

		self.path = path
		self.frames_i = 0
		self.frames = [ self.__get_frame(i) for i in range(length) ]
		self.image = self.__get_frame(0)
		self.rect = self.image.get_frect(**anchor)


	def __get_frame ( self, n: int ) -> Surface:
		return pipe(
			curry(load_animation_image)(self.path),
			convert_image
		)(n)

	def update ( self, give_me: dict[str, Any] ):
		self.frames_i += int( give_me['dt'] * 20 ) or 1

		if self.frames_i >= len(self.frames): self.kill()
		self.image = self.frames[self.frames_i]