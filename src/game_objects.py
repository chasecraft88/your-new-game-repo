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
        self.quest = None

    def set_quest(self, quest):
        self.quest = quest

    def interact(self):
        if self.quest:
            if self.quest.is_completed():
                print(f"NPC: 'You have completed the quest: {self.quest.description}'")
                return 'quest_complete'
            else:
                print(f"NPC: 'Quest in progress: {self.quest.description}'")
                return 'quest_in_progress'
        else:
            print("NPC: 'I have nothing for you.'")
            return 'no_quest'


class Quest:
    def __init__(self, description, objective_type, objective_count):
        self.description = description
        self.objective_type = objective_type
        self.objective_count = objective_count
        self.progress = 0

    def update_progress(self):
        self.progress += 1

    def is_completed(self):
        return self.progress >= self.objective_count

    def get_progress(self):
        return self.progress, self.objective_count
