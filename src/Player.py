import pygame

# Game Configuration
WIDTH, HEIGHT = 1000, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_VEL = 5
SLIDE_VOLUME = 0.5
SLIDE_MAXTIME = 40
SLIDE_FADE = 30

# Load Assets
try:
    UFO_IMG = pygame.transform.smoothscale(
        pygame.image.load("assets/graphics/UFO.png"), (PLAYER_WIDTH, PLAYER_HEIGHT)
    )
except (pygame.error, FileNotFoundError) as e:
    print(f"Error loading image: {e}")
    UFO_IMG = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
    UFO_IMG.fill("red")


class Player:
    """
    Class representing the player in the game.

    Attributes:
        rect (pygame.Rect): Rectangle representing the player's position and size.
    """

    def __init__(self):
        """
        Initialize the Player class by setting the player's starting position and size.
        """
        self.rect = UFO_IMG.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - PLAYER_HEIGHT)

    def move(self, SLIDE_SFX):
        """
        Handle player movement based on keyboard input and play sliding sound if moved.

        Args:
            SLIDE_SFX (pygame.mixer.Sound): The sound effect to play when the player moves.
        """
        keys = pygame.key.get_pressed()
        moved = False

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= PLAYER_VEL
            moved = True
        elif keys[pygame.K_RIGHT] and self.rect.x + PLAYER_WIDTH + PLAYER_VEL <= WIDTH:
            self.rect.x += PLAYER_VEL
            moved = True

        if moved:
            self._play_slide_sound(SLIDE_SFX)

    def _play_slide_sound(self, SLIDE_SFX):
        """
        Play the sliding sound effect.

        Args:
            SLIDE_SFX (pygame.mixer.Sound): The sound effect to play.
        """
        SLIDE_SFX.set_volume(SLIDE_VOLUME)
        SLIDE_SFX.play(maxtime=SLIDE_MAXTIME, fade_ms=SLIDE_FADE)

    def get_rect(self):
        """
        Get the rectangle representing the player's position and size.

        Returns:
            pygame.Rect: The player's rectangle.
        """
        return self.rect

    def get_image(self):
        """
        Get the image representing the player.

        Returns:
            pygame.Surface: The player's image surface.
        """
        return UFO_IMG
