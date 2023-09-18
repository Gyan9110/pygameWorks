import pygame
import random
import pygame.font

pygame.mixer.init()


pygame.init()

#Defining colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)


#creating Window Screen
screen_width = 1000
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()                   # why did we use this
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()


#Defining score in the window
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

#Creating Welcome page
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 150, 45))
        text_screen("Welcome to SNAKES!!", black, 260, 250)
        text_screen("Please space to continue", black, 230, 290)
        pygame.mixer.music.load('intro.mp3')
        pygame.mixer.music.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)

#Game Loop
def gameloop():
    #Game Specific Variables
    snake_x  = 60  #here x and y defines the start point of the snake
    snake_y = 30
    snake_size = 10
    vel_x = 0
    vel_y = 0
    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)
    fps = 30
    score = 0
    snk_list = []
    snk_length = 1
    exit_game = False
    game_over = False
    #Reading the high score
    with open("highScore.txt", "r") as f:
        hiscore = f.read()   #here the value is in string
    while not exit_game:
        if game_over:
            with open("highScore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over!Press Enter to continue", red, 200, 250)

            for event in pygame.event.get():
                    if event.type == pygame.QUIT: #to quit the game
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:   #here K_RETURN is the ENTER button
                            gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #to quit the game
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        vel_x = 5
                        vel_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        vel_x = 0
                        vel_y = 6

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        vel_x = -5
                        vel_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        vel_x = 0
                        vel_y = -5

            snake_x += vel_x
            snake_y += vel_y
            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
                score += 1
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length += 5
                if score>int(hiscore):
                    hiscore = score

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()
                game_over = True


            gameWindow.fill(white)
            text_screen("Score : "+ str(score) + "  High Score : "+ str(hiscore), red, 5, 5)  #adding the score in the screen
            pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, snake_size])  #food

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()
                game_over = True

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])  #creating the head of the snake and defining the start pos
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
