import pygame
import sys
from game_manager import GameManager

def main():
    pygame.init()
    game = GameManager()
    game.run()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()