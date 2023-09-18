import pygame
pygame.init()
gameWindow = pygame.display.set_mode((1200, 500))  # gameWindow is the window display screen for the game and set mode takes tuple values
pygame.display.set_caption("My First Game")

#Game specific variables
exit_game = False
game_over = False

#Creating game loop - this loop will continue until the game has been quit. It also handles all the events in the game
while not exit_game:
    for event in pygame.event.get():  #this handles all the events happening in the game eg. where the cursor moves or which keyboard letter is pressed
        if event.type == pygame.QUIT: #to quit the game
            exit_game = True

        if event.type == pygame.KEYDOWN:  #if any key is pressed in the keyboard
            if event.key == pygame.K_RIGHT:   #if the key pressed is the right arrow key
                print("You have pressed right arrow key")
pygame.quit()
quit()
