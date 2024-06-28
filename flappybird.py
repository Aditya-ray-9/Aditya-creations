import pygame
import sys
import random

# Initialize Pygame
pygame.init()

WIDTH = 1366
HEIGHT = 700
PIPE_WIDTH = 80
PIPE_HEIGHT = 600
BIRD_WIDTH = 40
BIRD_HEIGHT = 40
GRAVITY = 0.5
PIPE_GAP = random.randint(150, 190)
# PIPE_GAP = 400
PIPE_VEL = -4  # Define the pipe velocity

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load the background image
background_image = pygame.image.load('C:\\code matrial\\images\\flappy bird background.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Change the window logo/icon
icon_image = pygame.image.load('C:\\code matrial\\images\\flappy bird image.png')
pygame.display.set_icon(icon_image)

# Load the bird image
bird_image = pygame.image.load('C:\\code matrial\\images\\flappy bird image.png')
bird_image = pygame.transform.scale(bird_image, (int(BIRD_WIDTH * 2.0), int(BIRD_HEIGHT * 2.0)))

# Load the starting page image
start_image = pygame.image.load('C:\\code matrial\\images\\Flappy-Bird-Transparent.png')
start_image = pygame.transform.scale(start_image, (WIDTH, HEIGHT // 3))  # Adjust the size if needed

# Font for displaying text
font = pygame.font.Font(None, 48)

def show_start_menu():
    global about_button_rect, play_button_rect
    screen.fill(WHITE)
    
    # Blit the starting image onto the screen
    screen.blit(start_image, (0, HEIGHT // 6))  # Adjust the position if needed
    
    # Draw the Play button
    play_button = font.render("Play", True, BLACK)
    play_button_rect = play_button.get_rect(center=(WIDTH / 2, HEIGHT - 150))  # Move up from the bottom and make larger
    pygame.draw.rect(screen, BLACK, play_button_rect.inflate(40, 20), 2)  # Inflate more to make it larger
    screen.blit(play_button, play_button_rect)
    
    # Draw the About button
    about_button = font.render("About", True, BLACK)
    about_button_rect = about_button.get_rect(topright=(WIDTH - 20, 20))
    pygame.draw.rect(screen, BLACK, about_button_rect.inflate(10, 10), 2)
    screen.blit(about_button, about_button_rect)

    # Draw the help button
    help_button = font.render("help", True, BLACK)
    help_button_rect = help_button.get_rect(topright=(WIDTH - 150, 20))
    pygame.draw.rect(screen, BLACK, help_button_rect.inflate(30, 30), 2)
    screen.blit(help_button, help_button_rect)
    
    
    pygame.display.flip()

def show_help_window():
    global exit_button_rect
    help_running = True
    while help_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    pos = pygame.mouse.get_pos()
                    if exit_button_rect.collidepoint(pos):
                        help_running = False
        
        screen.fill(WHITE)
        about_text = [
            "Press space key or arrow up key to take this sprite up",
            "aditya is the developer os this game",
            "Press 'Exit' to return."
        ]

        y_offset = 100
        for line in about_text:
            text = font.render(line, True, BLACK)
            text_rect = text.get_rect(center=(WIDTH / 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 40
        
        # Draw the Exit button
        exit_button = font.render("Exit", True, BLACK)
        exit_button_rect = exit_button.get_rect(center=(WIDTH / 2, HEIGHT - 50))
        pygame.draw.rect(screen, BLACK, exit_button_rect.inflate(20, 20), 2)
        screen.blit(exit_button, exit_button_rect)
        
        pygame.display.flip()

def show_about_window():
    global exit_button_rect
    about_running = True
    while about_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    pos = pygame.mouse.get_pos()
                    if exit_button_rect.collidepoint(pos):
                        about_running = False
        
        screen.fill(WHITE)
        about_text = [
            "This game is developed using",
            "Python and its version 2",
            "Aditya ray is the devloper of this game ",
            "and i am giving a challange to you",
            "that is if you can score 300 or more than then ",
            "you are master in this game ",
            "good luck gamerz for this game ",
            "Press 'Exit' to return."
        ]
        y_offset = 100
        for line in about_text:
            text = font.render(line, True, BLACK)
            text_rect = text.get_rect(center=(WIDTH / 2, y_offset))
            screen.blit(text, text_rect)
            y_offset += 40
        
        # Draw the Exit button
        exit_button = font.render("Exit", True, BLACK)
        exit_button_rect = exit_button.get_rect(center=(WIDTH / 2, HEIGHT - 50))
        pygame.draw.rect(screen, BLACK, exit_button_rect.inflate(20, 20), 2)
        screen.blit(exit_button, exit_button_rect)
        
        pygame.display.flip()

def show_game_over(score):
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, BLACK)
    game_over_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 30))
    screen.blit(game_over_text, game_over_rect)
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    score_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 30))
    screen.blit(score_text, score_rect)
    
    pygame.display.flip()

def reset_game():
    global bird_x, bird_y, bird_vel, pipe_x, pipe_y, score
    bird_x = WIDTH / 4
    bird_y = HEIGHT / 2
    bird_vel = 0
    pipe_x = WIDTH
    pipe_y = random.randint(100, HEIGHT - 100 - PIPE_GAP)
    score = 0

# Main game loop
def game_loop():
    global bird_x, bird_y, bird_vel, pipe_x, pipe_y, score

    reset_game()
    running = True
    game_over = False
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        return  # Exit the game loop to show the start menu again
                    else:
                        bird_vel = -10  # Reset the bird's velocity
                elif event.key == pygame.K_UP:
                    if game_over:
                        return  # Exit the game loop to show the start menu again
                    else:
                        bird_vel = -10  # Reset the bird's velocity
                elif event.key == pygame.K_b:
                    if game_over:
                        return  # Exit the game loop to show the start menu again
                    else:
                        bird_vel = -10
                elif event.key == pygame.K_v:
                    if game_over:
                        return  # Exit the game loop to show the start menu again
                    else:
                        bird_vel = -10
                else :
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    pos = pygame.mouse.get_pos()
                    if about_button_rect.collidepoint(pos):
                        show_about_window()
                        show_help_window()
                        show_start_menu()
                        break

        if not game_over:
            # Move the bird
            bird_y += bird_vel
            bird_vel += GRAVITY

            # Move the pipes
            pipe_x += PIPE_VEL

            # Check for collisions
            if bird_y + BIRD_HEIGHT > HEIGHT or bird_y < 0:
                game_over = True
            elif (pipe_x < bird_x + BIRD_WIDTH and pipe_x + PIPE_WIDTH > bird_x) and \
                 (bird_y < pipe_y or bird_y + BIRD_HEIGHT > pipe_y + PIPE_GAP):
                game_over = True

            if pipe_x < -PIPE_WIDTH:
                pipe_x = WIDTH
                pipe_y = random.randint(100, HEIGHT - 100 - PIPE_GAP)
                score += 1

            # Draw everything
            screen.blit(background_image, (0, 0))  # Draw the background
            pygame.draw.rect(screen, DARK_GREEN, (pipe_x - 2, 0, PIPE_WIDTH + 4, pipe_y + 2))  # Dark green border for top pipe
            pygame.draw.rect(screen, DARK_GREEN, (pipe_x - 2, pipe_y + PIPE_GAP - 2, PIPE_WIDTH + 4, HEIGHT - pipe_y - PIPE_GAP + 4))  # Dark green border for bottom pipe
            pygame.draw.rect(screen, GREEN, (pipe_x, 0, PIPE_WIDTH, pipe_y))  # Top pipe
            pygame.draw.rect(screen, GREEN, (pipe_x, pipe_y + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe_y - PIPE_GAP))  # Bottom pipe
            screen.blit(bird_image, (bird_x, bird_y))

            # Render live score
            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (10, 10))
            
            pygame.display.flip()

        else:
            show_game_over(score)

        # Cap the framerate
        pygame.time.Clock().tick(60)

if __name__ == '__main__':
    while True:
        # Show the start menu
        show_start_menu()

        # Wait for the player to press the space key to start the game
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False  # Exit the waiting loop and start the game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        pos = pygame.mouse.get_pos()
                        if about_button_rect.collidepoint(pos):
                            show_about_window()
                            show_help_window()
                            show_start_menu()
                        elif play_button_rect.collidepoint(pos):
                            waiting = False  # Exit the waiting loop and start the game

        # Start the game loop
        game_loop()
