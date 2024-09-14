import pygame
import random
import json
import os
from game_objects import Player, Tile, Goal, NPC, Quest
from cutscenes import Cutscene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Adventurer's Journey")
        self.clock = pygame.time.Clock()
        self.tile_size = 30
        self.player = Player(self.tile_size)
        self.tiles = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.quests = []
        self.current_quest = None
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.level = 1

        self.cutscene = Cutscene(self.screen, self.font)  # Add Cutscene object

        # Attempt to load the saved game
        if os.path.exists('save_game.json'):
            self.load_game()
        else:
            self.generate_level()

        # Play an introductory cutscene when the game starts
        self.play_intro_cutscene()

    def play_intro_cutscene(self):
        """Plays the introductory cutscene."""
        cutscene_images = ["cutscene1.png", "cutscene2.png", "cutscene3.png"]  # Replace with actual images
        cutscene_texts = [
            "In a world torn by chaos, a lone adventurer rises.",
            "Monsters lurk in every corner, and only courage will prevail.",
            "Will you be the one to restore peace?"
        ]
        self.cutscene.display_cutscene(cutscene_images, cutscene_texts, duration=4)

    def play_quest_complete_cutscene(self):
        """Plays a cutscene when a quest is completed."""
        cutscene_texts = ["You have completed your quest!", "Your journey continues..."]
        self.cutscene.display_text_cutscene(cutscene_texts, duration=3)

    def generate_level(self):
        self.tiles.empty()
        self.goals.empty()
        self.npcs.empty()
        self.generate_tiles()
        self.generate_goals()
        self.generate_npcs()
        self.assign_quests()

    def assign_quests(self):
        # Example quests
        quest1 = Quest("Collect 5 goals scattered around the map.", "collect", 5)
        quest2 = Quest("Talk to 3 NPCs.", "visit_npc", 3)

        self.quests = [quest1, quest2]
        self.current_quest = self.quests[0]  # Start with the first quest

        for i, npc in enumerate(self.npcs):
            if i < len(self.quests):
                npc.set_quest(self.quests[i])

    def check_collisions(self):
        if pygame.sprite.spritecollide(self.player, self.goals, True):
            self.score += 10
            if self.current_quest and self.current_quest.objective_type == 'collect':
                self.current_quest.update_progress()

        for npc in self.npcs:
            if pygame.sprite.collide_rect(self.player, npc):
                result = npc.interact()

                if result == 'quest_complete':
                    self.play_quest_complete_cutscene()  # Play cutscene after completing the quest
                    self.current_quest = None
                elif result == 'quest_in_progress' and self.current_quest.objective_type == 'visit_npc':
                    self.current_quest.update_progress()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.save_game()

            self.player.update()
            self.check_collisions()

            self.screen.fill((200, 200, 200))
            self.tiles.draw(self.screen)
            self.goals.draw(self.screen)
            self.npcs.draw(self.screen)
            self.player.draw(self.screen)

            score_text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
            level_text = self.font.render(f'Level: {self.level}', True, (0, 0, 0))
            quest_text = "No active quest" if not self.current_quest else f"Quest: {self.current_quest.get_progress()[0]} / {self.current_quest.get_progress()[1]}"
            quest_display = self.font.render(quest_text, True, (0, 0, 0))

            self.screen.blit(score_text, (10, 10))
            self.screen.blit(level_text, (10, 50))
            self.screen.blit(quest_display, (10, 90))

            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()

    def save_game(self):
        data = {
            "score": self.score,
            "level": self.level,
            "current_quest": self.current_quest.description if self.current_quest else None
        }
        with open('save_game.json', 'w') as f:
            json.dump(data, f)
        print("Game saved!")

    def load_game(self):
        with open('save_game.json', 'r') as f:
            data = json.load(f)
            self.score = data.get("score", 0)
            self.level = data.get("level", 1)
            quest_desc = data.get("current_quest", None)
            if quest_desc:
                for quest in self.quests:
                    if quest.description == quest_desc:
                        self.current_quest = quest
                        break
        print("Game loaded!")
