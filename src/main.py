import pygame
import time
from Player import Player
from Meteor import Meteor

# Constants
WIDTH, HEIGHT = 1000, 600
FONT_HEADING_SIZE, FONT_TEXT_SIZE = 30, 15
WIN_TIME = 40
DELAY_TIME = 4000
INITIAL_METEOR_LIMIT = 2000
MIN_METEOR_LIMIT = 200
FPS = 60


# Game Setup Function
def setup():
    """
    Initialize the Pygame environment and load necessary resources.

    Returns:
        dict: A dictionary containing loaded resources, including window, background,
              icons, fonts, clock, and sounds.
    """
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.set_caption("Meteor Dash")
    try:
        icon = pygame.image.load("assets/graphics/Icon.png")
        pygame.display.set_icon(icon)

        return {
            "WIN": pygame.display.set_mode((WIDTH, HEIGHT)),
            "BG": pygame.transform.smoothscale(
                pygame.image.load("assets/graphics/Background Image.png"),
                (WIDTH, HEIGHT),
            ),
            "FONT_HEADING": pygame.font.SysFont("comicsansms", FONT_HEADING_SIZE),
            "FONT_TEXT": pygame.font.SysFont("comicsansms", FONT_TEXT_SIZE),
            "CLOCK": pygame.time.Clock(),
            "BG_MSC": pygame.mixer.Sound("assets/audio/BGM.mp3"),
            "SLIDE_SFX": pygame.mixer.Sound("assets/audio/Slide SFX.mp3"),
            "LOST_SFX": pygame.mixer.Sound("assets/audio/Lose SFX.mp3"),
            "WIN_SFX": pygame.mixer.Sound("assets/audio/Win SFX.mp3"),
        }
    except (pygame.error, FileNotFoundError) as e:
        print(f"Error loading resources: {e}")
        pygame.quit()


class MeteorDash:
    """
    Main game class for managing the Meteor Dash game.

    Attributes:
        win (pygame.Surface): The game window surface.
        clock (pygame.time.Clock): The game clock for managing frame rate.
        bg (pygame.Surface): The background image surface.
        font_heading (pygame.font.Font): Font for headings.
        font_text (pygame.font.Font): Font for smaller text.
        bg_msc (pygame.mixer.Sound): Background music sound.
        slide_sfx (pygame.mixer.Sound): Sound effect for sliding.
        win_sfx (pygame.mixer.Sound): Sound effect for winning.
        lose_sfx (pygame.mixer.Sound): Sound effect for losing.
        run (bool): Flag to indicate if the game is running.
        hit (bool): Flag to indicate if a meteor hits the player.
        paused (bool): Flag to indicate if the game is paused.
        start_time (float): The starting time of the game.
        player (Player): The player object.
        meteor (Meteor): The meteor object.
        meteor_counter (int): Counter for meteor generation.
        meteor_limit (int): Time limit between meteor generations.
    """

    def __init__(self, resources):
        """
        Initialize the MeteorDash game with resources.

        Args:
            resources (dict): A dictionary containing game resources.
        """
        self.win: pygame.Surface = resources["WIN"]
        self.clock: pygame.time.Clock = resources["CLOCK"]
        self.bg: pygame.Surface = resources["BG"]
        self.font_heading: pygame.font.Font = resources["FONT_HEADING"]
        self.font_text: pygame.font.Font = resources["FONT_TEXT"]
        self.bg_msc: pygame.mixer.Sound = resources["BG_MSC"]
        self.slide_sfx: pygame.mixer.Sound = resources["SLIDE_SFX"]
        self.win_sfx: pygame.mixer.Sound = resources["WIN_SFX"]
        self.lose_sfx: pygame.mixer.Sound = resources["LOST_SFX"]

        self.run: bool = True
        self.hit: bool = False
        self.paused: bool = False
        self.start_time: float = time.time()
        self.player: Player = Player()
        self.meteor: Meteor = Meteor()
        self.meteor_counter: int = 0
        self.meteor_limit: int = INITIAL_METEOR_LIMIT

    def process_events(self):
        """
        Process Pygame events such as quitting or pausing the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.pause_game()

    def draw(self, elapsed_time):
        """
        Draw all game elements onto the game window.

        Args:
            elapsed_time (int): The time elapsed since the start of the game.
        """
        self.win.blit(self.bg, (0, 0))
        time_text = self.font_heading.render(f"Time: {elapsed_time}s", True, "white")
        goal_text = self.font_text.render("survive 40s to win!", True, "white")

        self.win.blit(time_text, (30, 30))
        self.win.blit(goal_text, (35, 75))
        self.win.blit(self.player.get_image(), self.player.get_rect())

        for meteor in self.meteor.get_meteors():
            self.win.blit(self.meteor.get_image(), meteor)
        pygame.display.update()

    def end_game(self, sound, message, color, elapsed_time=None):
        """
        Handle game-ending events and display the end message.

        Args:
            sound (pygame.mixer.Sound): The sound to play during the end event.
            message (str): The message to display on the screen.
            color (str): The color of the message text.
            elapsed_time (int, optional): The time survived by the player.
        """
        self.handle_end_game_audio(sound)
        elapsed_message = f" TIME SURVIVED: {elapsed_time}s" if elapsed_time else ""
        self.display_end_game_message(message + elapsed_message, color)

    def handle_end_game_audio(self, sound, fadeout_duration=2000):
        """
        Play the end game audio and fade out the background music.

        Args:
            sound (pygame.mixer.Sound): The sound to play.
            fadeout_duration (int): Duration to fade out the background music.
        """
        sound.play()
        self.bg_msc.fadeout(fadeout_duration)

    def display_end_game_message(self, message, color):
        """
        Display the end game message on the screen.

        Args:
            message (str): The message to display.
            color (str): The color of the text.
        """
        end_game_text = self.font_heading.render(message, True, color)
        self.win.fill("black")
        self.win.blit(
            end_game_text,
            (
                (WIDTH - end_game_text.get_width()) / 2,
                (HEIGHT - end_game_text.get_height()) / 2,
            ),
        )
        pygame.display.update()
        pygame.time.delay(DELAY_TIME)
        self.run = False

    def handle_pause_events(self):
        """
        Handle events during the pause state.

        Returns:
            bool: True if the game should resume, False otherwise.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True
        return False

    def pause_game(self):
        """
        Pause the game and display the paused message.
        """
        self.paused = True
        pause_start_time = time.time()
        pause_text = self.font_heading.render("PAUSED", True, "white")
        self.win.blit(
            pause_text,
            (
                (WIDTH - pause_text.get_width()) / 2,
                (HEIGHT - pause_text.get_height()) / 2,
            ),
        )
        pygame.display.update()

        while self.paused:
            self.clock.tick(FPS)
            if self.handle_pause_events():
                pause_duration = time.time() - pause_start_time
                self.start_time += pause_duration
                self.paused = False

    def update_game_state(self, elapsed_time):
        """
        Update the game state, including meteor generation and win/loss conditions.

        Args:
            elapsed_time (int): The time elapsed since the start of the game.
        """
        if self.hit:
            self.end_game(self.lose_sfx, "YOU LOST!", "red", elapsed_time)
        if elapsed_time == WIN_TIME:
            self.end_game(self.win_sfx, "YOU WON!", "green")

        if not self.paused:
            self.meteor_counter += self.clock.get_time()
            if self.meteor_counter >= self.meteor_limit:
                self.meteor.generate_meteors()
                self.meteor_counter = 0
                self.meteor_limit = max(MIN_METEOR_LIMIT, self.meteor_limit - 50)

    def run_game(self):
        """
        Run the main game loop.
        """
        self.bg_msc.play(-1)

        while self.run:
            self.clock.tick(FPS)
            elapsed_time = round(time.time() - self.start_time)
            self.player.move(self.slide_sfx)
            self.hit = self.meteor.move_meteors(self.player)
            self.update_game_state(elapsed_time)
            self.process_events()
            self.draw(elapsed_time)
        pygame.quit()


if __name__ == "__main__":
    resources = setup()
    game = MeteorDash(resources)
    game.run_game()
