import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 255, 0))  # Green color for player
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Starting position in the center
        self.speed = size  # Speed is the size of a tile (moves one tile at a time)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((50, 50, 50))  # Dark color for tiles
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 0, 0))  # Red color for goal
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 0, 255))  # Blue color for NPC
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def interact(self):
        print("NPC: 'Hello, adventurer! How do you handle challenges?'")
        print("1. Face them with courage (Good)")
        print("2. Avoid them whenever possible (Bad)")
        choice = input("Choose (1 or 2): ")
        if choice == '1':
            print("NPC: 'Good choice, the world around you brightens!'")
            return 'good'
        elif choice == '2':
            print("NPC: 'Avoidance leads to darkness in your path.'")
            return 'bad'
