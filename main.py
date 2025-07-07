import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        print(asteroids)

        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("GAME OVER")
                sys.exit()


        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        tick = clock.tick(60)
        dt = tick / 1000


if __name__ == "__main__":
    main()
