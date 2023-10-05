import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from gameobject import GameState, GameObject, Object2D
from tile import Tile, TileType
import constants

class Player(Object2D):
	def __init__(self, pos: Vector2):
		super().__init__(pos, Vector2(constants.TILE_SIZE, constants.TILE_SIZE * 2))
		self.vel = Vector2(0, 0)

	def onGround(self, gameobjects: list[GameObject]) -> TileType | None:
		for obj in gameobjects:
			if (
				isinstance(obj, Tile) 
				and obj.getRect().collidepoint(self.pos + Vector2(self.size.x / 2, self.size.y))
			):
				return obj.type
		return None

	def update(
		self, 
		delta: float, 
		surface: Surface, 
		keys: pygame.key.ScancodeWrapper, 
		gameobjects: list[GameObject], 
		gamestate: GameState
	):
		if keys[pygame.K_UP]:
			self.vel.y = -constants.JUMP_HEIGHT
		if keys[pygame.K_LEFT]:
			self.vel.x = -10
		elif keys[pygame.K_RIGHT]:
			self.vel.x = 10


		self.vel.y += constants.GRAVITY * delta

		self.pos += self.vel * delta