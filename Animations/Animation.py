from settings import *
from typing import Any
from pygame import Surface
from pygame.sprite import Group
from Utils.Loader import get_frame

class Animation ( pygame.sprite.Sprite ):
	def __init__(self, groups: Group | tuple[Group, ...], frames: list[Surface], **anchor: tuple[float, float]) -> None:
		super().__init__(groups)

		self.frames_i = 0
		self.frames = frames
		self.image = self.frames[0]
		self.rect = self.image.get_frect(**anchor)

	def _increment_frames_i ( self, n: int, dt: float ):
		self.frames_i += int( dt * n ) or 1

	def _on_animation_end ( self ):
		if self.frames_i >= len(self.frames): self.kill()

	def _set_image ( self ):
		if self.frames_i < len(self.frames):
			self.image = self.frames[self.frames_i]

	def update ( self, give_me: dict[str, Any] ):
		self._increment_frames_i(1, give_me['dt'])
		self._on_animation_end()
		self._set_image()