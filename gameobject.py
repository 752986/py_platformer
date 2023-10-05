import pygame
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface

class GameState:
	# future class for storing progression data, such as powerups or current level
	pass

class GameObject:
	def update(
		self, 
		delta: float, 
		surface: Surface, 
		keys: pygame.key.ScancodeWrapper, 
		gameobjects: list["GameObject"], 
		gamestate: GameState
	):
		pass

class Object2D(GameObject):
	def __init__(self, pos: Vector2, size: Vector2):
		self.pos = pos
		self.size = size

	def getRect(self) -> Rect:
		return Rect(self.pos, self.size)