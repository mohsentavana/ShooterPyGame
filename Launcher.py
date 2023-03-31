  # t.me/MohsenLinux
  # https://github.com/mohsentavana
  # Enjoy for Free 
  
  # first import  

import pygame

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 30)

# Set up the menu
class Menu:
    def __init__(self, items, x, y):
        self.items = items
        self.font = pygame.font.SysFont(None, 30)
        self.x = x
        self.y = y
        self.selected_item = 0

    def draw(self, screen):
        for index, item in enumerate(self.items):
            if self.selected_item == index:
                label = self.font.render(item, True, WHITE)
            else:
                label = self.font.render(item, True, BLACK)
            width = label.get_width()
            height = label.get_height()
            x = self.x - (width / 2)
            y = self.y + index * height * 1.5
            screen.blit(label, (x, y))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_item -= 1
            elif event.key == pygame.K_DOWN:
                self.selected_item += 1
            elif event.key == pygame.K_RETURN:
                # Return the index of the selected item
                return self.selected_item
        # Make sure selected item is within bounds
        self.selected_item = max(min(self.selected_item, len(self.items) - 1), 0)

# Set up the main menu
main_menu = Menu(["Start", "About", "Exit"], SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Set up the game
def game():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Update screen
        screen.fill(WHITE)
        pygame.display.update()

    # Quit pygame properly
    pygame.quit()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if main_menu.selected_item == 0:
                game()
            elif main_menu.selected_item == 1:
                print("This is a simple game made with pygame.")
            elif main_menu.selected_item == 2:
                running = False

        # Handle menu events
        main_menu.handle_event(event)

    # Update screen
    screen.fill(WHITE)
    main_menu.draw(screen)
    pygame.display.update()

# Quit pygame properly
pygame.quit()

  # t.me/MohsenLinux
  # https://github.com/mohsentavana
