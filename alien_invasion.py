import sys

import pygame

from settings import Settings

def run_game():
  # 初始化
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption('Alien Invasion')

  while True:

    for envent in pygame.event.get():
      if envent.type == pygame.QUIT:
        sys.exit()

    screen.fill(ai_settings.bg_color)

    pygame.display.flip()

run_game()