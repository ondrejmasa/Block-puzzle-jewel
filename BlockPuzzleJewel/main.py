import pygame
from parameters import *
from game import Game

pygame.init()


font = pygame.font.Font(None, 40)

score_surface = font.render("Score", True, Colors.white)
score_surface_rect = score_surface.get_rect(midtop=(520, 20))

score_rect = pygame.Rect(435, 50, 170, 60)

game_over_surface = font.render("Game over!", True, Colors.white)
game_over_surface_rect = game_over_surface.get_rect(midtop=(520, 200))

restart_button_back = pygame.Rect(435, 240, 170, 60)
restart_button = pygame.Rect(435, 240, 168, 58)
restart_surface = font.render("Restart", True, Colors.white)
restart_surface_rect = restart_surface.get_rect(center=(520, 270))


screen = pygame.display.set_mode((620, 560))
pygame.display.set_caption("Block Puzzle Jewel")

FPS = 60
clock = pygame.time.Clock()

game = Game()


run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            if restart_button.collidepoint(event.pos):
                game.restart()

        if event.type == pygame.KEYDOWN:
            if not game.game_over:
                if game.choosing:
                    if event.key == pygame.K_RIGHT:
                        game.change_chosen_block()

                    if event.key == pygame.K_UP:
                        game.get_current_block()
                else:
                    if event.key == pygame.K_UP:
                        game.move_up()

                    if event.key == pygame.K_DOWN:
                        game.move_down()

                    if event.key == pygame.K_LEFT:
                        game.move_left()

                    if event.key == pygame.K_RIGHT:
                        game.move_right()

                    if event.key == pygame.K_KP_ENTER:
                        game.lock_block()

    pygame.display.update()

    # drawing
    score_value_surface = font.render(str(game.score), True, Colors.white)
    score_value_surface_rect = score_value_surface.get_rect(center=(520, 80))

    screen.fill(Colors.dark_blue)

    screen.blit(score_surface, score_surface_rect)
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface_rect)

    if game.game_over:
        screen.blit(game_over_surface, game_over_surface_rect)
        pygame.draw.rect(screen, (0, 0, 0), restart_button_back, 0, 0)
        pygame.draw.rect(screen, Colors.red, restart_button, 0, 0)
        screen.blit(restart_surface, restart_surface_rect)

    game.draw(screen)

pygame.quit()
