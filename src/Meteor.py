import pygame
import random

# Game Configuration
WIDTH, HEIGHT = 1000, 600
METEOR_WIDTH, METEOR_HEIGHT = 25, 25
METEOR_VEL = 3
MIN_METEORS, MAX_METEORS = 4, 10

# Load Assets
try:
    METEOR_IMG = pygame.transform.smoothscale(
        pygame.image.load("assets/graphics/Meteor.png"), (METEOR_WIDTH, METEOR_HEIGHT)
    )
except (pygame.error, FileNotFoundError) as e:
    print(f"Error loading image: {e}")
    METEOR_IMG = pygame.Surface((METEOR_WIDTH, METEOR_HEIGHT))  # Fallback surface
    METEOR_IMG.fill("yellow")  # Fill with yellow color


class Meteor:
    """
    Class for managing meteors in the game.

    Attributes:
        meteors (list[pygame.Rect]): List of meteor rectangles representing their positions and sizes.
    """

    def __init__(self):
        """
        Initialize the Meteor class with an empty list of meteors.
        """
        self.meteors = []

    def generate_meteors(self):
        """
        Generate a random number of meteors within the range [MIN_METEORS, MAX_METEORS].
        Each meteor is placed randomly at the top of the screen and added to the list of meteors.
        """
        for _ in range(random.randint(MIN_METEORS, MAX_METEORS)):
            meteor = METEOR_IMG.get_rect()
            meteor.left = random.randint(0, WIDTH - METEOR_WIDTH)
            meteor.top = -METEOR_HEIGHT
            meteor.width = METEOR_WIDTH
            meteor.height = METEOR_HEIGHT
            self.meteors.append(meteor)

    def move_meteors(self, player):
        """
        Move all meteors downward and check for collisions with the player or if meteors leave the screen.

        Args:
            player (Player): The player object to check for collisions.

        Returns:
            bool: True if a meteor collides with the player, False otherwise.
        """
        for meteor in self.meteors[:]:
            meteor.y += METEOR_VEL
            if meteor.y >= HEIGHT:
                self.meteors.remove(meteor)
            elif self._check_collision(meteor, player):
                self.meteors.remove(meteor)
                return True
        return False

    def _check_collision(self, meteor, player):
        """
        Check if a meteor collides with the player.

        Args:
            meteor (pygame.Rect): The meteor's rectangle.
            player (Player): The player's object, expected to have a get_rect() method.

        Returns:
            bool: True if the meteor collides with the player, False otherwise.
        """
        return meteor.y + METEOR_HEIGHT >= player.get_rect().y and meteor.colliderect(
            player
        )

    def get_meteors(self):
        """
        Get the list of current meteors.

        Returns:
            list[pygame.Rect]: List of meteor rectangles.
        """
        return self.meteors

    def get_image(self):
        """
        Get the meteor image.

        Returns:
            pygame.Surface: The surface representing the meteor image.
        """
        return METEOR_IMG
