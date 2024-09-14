import pygame
import time

class Cutscene:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

    def display_cutscene(self, images, texts, duration=3):
        """Displays a cutscene with a series of images and texts."""
        for i, image_file in enumerate(images):
            image = pygame.image.load(image_file).convert()
            text = self.font.render(texts[i], True, (255, 255, 255))

            # Blit the image and text to the screen
            self.screen.blit(image, (0, 0))
            self.screen.blit(text, (20, 500))

            pygame.display.flip()
            time.sleep(duration)

    def display_text_cutscene(self, texts, duration=3):
        """Displays a cutscene with text only."""
        for text in texts:
            self.screen.fill((0, 0, 0))
            rendered_text = self.font.render(text, True, (255, 255, 255))
            self.screen.blit(rendered_text, (50, 300))

            pygame.display.flip()
            time.sleep(duration)
