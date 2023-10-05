import pygame
from pygame.math import Vector2
from pygame.color import Color
from pygame.rect import Rect
from pygame.surface import Surface
from enum import Enum
from gameobject import  GameState, GameObject, Object2D
import constants

class TileType(Enum):
	Ground = 0
	Ice = 1
	Bouncy = 2
	Gravity = 3
	Dream = 4

	def color(self) -> Color:
		match self:
			case self.Ground:
				return Color("#444444")
			case self.Ice:
				return Color("#b2dbe0")
			case self.Bouncy:
				return Color("#c050a4")
			case self.Gravity:
				return Color("#8235e7")
			case self.Dream:
				return Color("#47db91")

class Tile(Object2D):
	def __init__(self, pos: Vector2, type: TileType):
		super().__init__(pos, Vector2(constants.TILE_SIZE, constants.TILE_SIZE))
		self.type = type

	def update(
		self, 
		delta: float, 
		surface: Surface, 
		keys: pygame.key.ScancodeWrapper, 
		gameobjects: list[GameObject], 
		gamestate: GameState
	):
		pygame.draw.rect(
			surface, 
			self.type.color(), 
			self.getRect()
		)
