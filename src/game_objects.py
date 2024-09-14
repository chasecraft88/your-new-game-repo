import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Red square
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass  # Update object state
