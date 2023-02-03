import pygame

WIDTH, HEIGHT = 1500, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG: The Game of the Gods")


def main():
    run = True

    while run:
        for event in pygame.event.get():
