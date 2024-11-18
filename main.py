# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updateable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = (updateable_group, drawable_group)

    Asteroid.containers = (asteroid_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updateable in updateable_group:
            updateable.update(dt)
        
        for asteroid in asteroid_group:
            if asteroid.check_collision(player):
                print("Game Over!")
                sys.exit()

        screen.fill("black")
        for drawable in drawable_group:
            drawable.draw(screen)
        
        pygame.display.flip()

        # limit framerate 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()