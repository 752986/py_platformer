import pygame
import constants

# pygame init:
pygame.init()
screen = pygame.display.set_mode(constants.SCREEN_SIZE)
pygame.display.set_caption("Platformer")

def main():
	# game setup:
	clock = pygame.time.Clock()

	# main loop:
	running = True
	while running:
		delta = clock.tick(constants.FRAMERATE) / 1000

		# input:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		# draw:
		screen.fill("#000000")

		pygame.display.flip()

if __name__ == "__main__":
	main()