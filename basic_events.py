import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Event Handling Example")

# Game loop
running = True
while running:
    # 1. Get all events that have occurred since the last loop iteration
    for event in pygame.event.get():
        # 2. Check the type of the event
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Handle key presses
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                print("Spacebar pressed!")
            elif event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
        elif event.type == pygame.KEYUP:
            # Handle key releases (optional)
            if event.key == pygame.K_SPACE:
                print("Spacebar released!")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse button presses
            if event.button == 1:  # Left mouse button
                print(f"Left mouse button clicked at: ({event.pos[0]}, {event.pos[1]})")
            elif event.button == 3:  # Right mouse button
                print(f"Right mouse button clicked at: ({event.pos[0]}, {event.pos[1]})")
        elif event.type == pygame.MOUSEBUTTONUP:
            # Handle mouse button releases (optional)
            pass
        elif event.type == pygame.MOUSEMOTION:
            # Handle mouse movement
            # print(f"Mouse moved to: ({event.pos[0]}, {event.pos[1]})")
            pass

    # Game logic goes here (updating game state, etc.)

    # Drawing code goes here (drawing objects on the screen)
    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.display.flip()

# Quit Pygame
pygame.quit()
