import pygame
import random
from game_objects import Player, Tile, Goal, NPC

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Classic Grid Game')
        self.clock = pygame.time.Clock()
        self.tile_size = 30
        self.player = Player(self.tile_size)
        self.tiles = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.generate_tiles()
        self.generate_goals()
        self.generate_npcs()
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.level = 1
        self.quest_active = False
        self.quest_progress = 0
        self.cutscene_active = False

    def generate_tiles(self):
        for x in range(0, self.screen.get_width(), self.tile_size):
            for y in range(0, self.screen.get_height(), self.tile_size):
                tile = Tile(x, y, self.tile_size)
                self.tiles.add(tile)

    def generate_goals(self):
        for _ in range(5):
            x = random.randint(0, (self.screen.get_width() - self.tile_size) // self.tile_size) * self.tile_size
            y = random.randint(0, (self.screen.get_height() - self.tile_size) // self.tile_size) * self.tile_size
            goal = Goal(x, y, self.tile_size)
            self.goals.add(goal)

    def generate_npcs(self):
        for _ in range(2):
            x = random.randint(0, (self.screen.get_width() - self.tile_size) // self.tile_size) * self.tile_size
            y = random.randint(0, (self.screen.get_height() - self.tile_size) // self.tile_size) * self.tile_size
            npc = NPC(x, y, self.tile_size)
            self.npcs.add(npc)

    def check_collisions(self):
        if pygame.sprite.spritecollide(self.player, self.goals, True):
            self.score += 10
            if not self.goals:
                self.level += 1
                self.generate_goals()
            return True
        return False

    def run_cutscene(self):
        self.screen.fill((0, 0, 0))  # Black background for cutscene
        cutscene_text = "Welcome to the new level! Press any key to continue."
        text_surf = self.font.render(cutscene_text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_surf, text_rect)
        pygame.display.flip()
        self.wait_for_keypress()

    def wait_for_keypress(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def check_npc_interactions(self):
        for npc in self.npcs:
            if pygame.sprite.collide_rect(self.player, npc):
                if not self.quest_active:
                    npc.interact()
                    self.quest_active = True
                return

    def update_quest_progress(self):
        if self.quest_active:
            self.quest_progress += 1
            if self.quest_progress >= 5:  # Complete quest after 5 interactions
                print("Quest Complete!")
                self.quest_active = False
                self.quest_progress = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.player.update()
            self.check_collisions()
            self.check_npc_interactions()
            self.update_quest_progress()

            if self.level > 1 and not self.cutscene_active:
                self.cutscene_active = True
                self.run_cutscene()

            self.screen.fill((200, 200, 200))  # Background color
            self.tiles.draw(self.screen)
            self.goals.draw(self.screen)
            self.npcs.draw(self.screen)
            self.player.draw(self.screen)

            score_text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
            level_text = self.font.render(f'Level: {self.level}', True, (0, 0, 0))
            self.screen.blit(score_text, (10, 10))
            self.screen.blit(level_text, (10, 50))

            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()
